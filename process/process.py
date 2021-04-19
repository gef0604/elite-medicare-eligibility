import json
from copy import deepcopy

from utils.field_mappers import basic_info_parser, inpatient_parser, deductible_caps_parser, QMB_Status_parser, \
    msp_parser, plan_coverage_parser, part_d_parser, hospice_parser, home_health_parser, snf_parser
from med_connector.med_api_connector import med_api_connector
from sf_connector.sf_api_connector import sf_api_connector


class processor:
    def __init__(self):
        # sf = Salesforce(password='Toronto360', username='eip@accelerize360.com.uat', organizationId='00D6s0000008aQV',
        #                     security_token='Xkeuinwc9Rb3xVk67Fb7xTojE',domain='test')
        self.sf_connector = sf_api_connector(username='eip@accelerize360.com.uat',
                                             password='Toronto360',
                                             organizationId='00D6s0000008aQV',
                                             security_token='Xkeuinwc9Rb3xVk67Fb7xTojE',
                                             domain='test')
        self.med_api_connector = med_api_connector(1, 2, 1)

    def process(self, data_points):
        # get xml and parse into json
        raw_response = self.med_api_connector.execute(data_points)
        print(raw_response)

        # if error, send back
        # print('error')

        if isinstance(raw_response['Result']['Section'], dict):
            if 'Error' in raw_response['Result']['Section'].keys():
                print(raw_response['Result']['Section']['Error'])
                print(raw_response['Result']['Section']['Note'])
                res = {}
                res['success'] = False
                res['Error'] = raw_response['Result']['Section']['Error']
                res['Note'] = raw_response['Result']['Section']['Note']
                return json.dumps(res)

        """
        seperate sections in different obj,
        for example:
        raw:
        {
        ...
        'section' : []
        ...
        },
        processed: [{
        ....
        section:{}
        ...
        },
        {
        ...
        'section':{}
        ...
        }
        ]
        """

        res_array = self.seperate_sections(raw_response)
        print(res_array)
        # {'objectName1' : {body}, 'objectName2' : {body}}
        # dataset = self.field_mapping(raw_response)

        sf_model_array = []
        for res in res_array:
            sf_model_array.append(self.field_mapping(res))
            # print(self.field_mapping(res))

        print(sf_model_array)

        # final result for sf model
        merge_res = self.merge(sf_model_array)

        print(merge_res)
        return json.dumps(self.sf_connector.create_medicare_object(merge_res, acctid=data_points['acctid']))
        # self.sf_connector.create_or_update_objects_by_dict(merge_res, acctid=data_points['acctid'])

    """
    def merge({key1:val1}, {key2, val2}) => {key1:val1, key2:val2}
    """

    def merge(self, aggr):
        res = {}
        for obj in aggr:
            res = {**res, **obj}
        return res

        # keep it in case, [{obj1:{}, obj2:{}}, {obj1:....}] => {'obj1':{}, ...}
        # res = {}
        # for b in aggr:
        #     for key in b.keys():
        #         if key not in res.keys():
        #             res[key] = b[key]
        #         else:
        #             res[key] = {**res[key], **b[key]}
        #
        # return res

    """
    seperate_section:
    convert from {section:[{},{}]}
    => {section:{}}, {'section':{}}
    """

    def seperate_sections(self, aggr_body):
        res = []
        sections = deepcopy(aggr_body['Result']['Section'])

        # aggr is "base"
        del aggr_body['Result']['Section']

        for section in sections:
            # print(section)
            base = deepcopy(aggr_body)
            base['Result']['Section'] = section
            res.append(base)

        return res

    """
    {'section:{}'} => sf_model
    note: just one section, call the seperate section first
    """

    def field_mapping(self, raw_response):
        # this is for seperate obj, keep it just in case
        # objects =  {
        #     'MedicareEligibility__c' : basic_info_parser().parse(raw_response),
        #     'Inpatient__c' : inpatient_parser().parse(raw_response),
        #     'DeductibleCap__c' : deductible_caps_parser().parse(raw_response),
        #     'QmbStatus_c' : QMB_Status_parser().parse(raw_response),
        #     # look at msp later
        #     # 'MSP__c' : msp_parser().parse(raw_response),
        #     'PlanCoverage__c' : plan_coverage_parser().parse(raw_response),
        #     'PartD__c' : part_d_parser().parse(raw_response)
        # }
        #
        # res = {}
        # for key in objects.keys():
        #     if objects[key] != None:
        #         res[key] = objects[key]
        #
        # return res

        res = {}
        basic = basic_info_parser().parse(raw_response)
        inpatient = inpatient_parser().parse(raw_response)
        deductible = deductible_caps_parser().parse(raw_response)
        qmb = QMB_Status_parser().parse(raw_response)
        # look at msp later
        # 'MSP__c' : msp_parser().parse(raw_response),
        msp = msp_parser().parse(raw_response)
        plan_coverage = plan_coverage_parser().parse(raw_response)
        part_d = part_d_parser().parse(raw_response)
        homehealth = home_health_parser().parse(raw_response)
        hospice = hospice_parser().parse(raw_response)
        snf = snf_parser().parse(raw_response)
        if basic != None:
            res = {**res, **basic}
        if inpatient != None:
            res = {**res, **inpatient}
        if deductible != None:
            res = {**res, **deductible}
        if qmb != None:
            res = {**res, **qmb}
        if plan_coverage != None:
            res = {**res, **plan_coverage}
        if part_d != None:
            res = {**res, **part_d}
        if msp != None:
            res = {**res, **msp}
        if homehealth != None:
            res = {**res, **homehealth}
        if hospice != None:
            res = {**res, **hospice}
        if snf != None:
            res = {**res, **snf}
        # if MSP__c != None:
        #     res = {**res, **MSP__c}

        return res

# d = {
#   "hic": "1ER8H40AV28",
#   "firstname": "Betty",
#   "lastname": "WInslett",
#   "dob": "19370407",
#   "npi": "9120929238",
#   "service": "270_271_ElgTransactions",
#   "api_key": "d01aefa6-45e6-403e-b0dc-9d4907e8eba8",
#   "acctid" : '0013m00002BWZ51AAH'
# }
# #
# # med_api_connector(1,1,1).execute(d)
# # #
# # # # print(med_api_connector(1,1,1).execute(d))
# print(processor().process(d))
# a= 1
