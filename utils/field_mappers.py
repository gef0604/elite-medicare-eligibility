import properties.field_mapping as field_mapping
from datetime import datetime

from properties import sample
from utils.xml_parser import xml_parser


class parser(object):
    def __init__(self):
        self.field_mapping = {}
        self.condition_map = {}

    def parse_condition(self, map):
        return {}

    def parse(self, json_content):
        condition_fields = self.parse_condition(json_content)
        if condition_fields == None:
            return None

        # print('basic parser, need to extend it to customize field mapping')
        flat_field_mapping = self.flatten_json(self.field_mapping)
        flat_json_content = self.flatten_json(json_content)

        # print(flat_field_mapping)
        # print(flat_json_content)
        res = {}

        for key in flat_field_mapping:
            if key in flat_json_content:
                res[flat_field_mapping[key]] = flat_json_content[key]


        return {**res, **condition_fields}

    def flatten_json(self, y):
        out = {}

        def flatten(x, name=''):
            if type(x) is dict:
                for a in x:
                    flatten(x[a], name + a + '_')
            elif type(x) is list:
                i = 0
                for a in x:
                    flatten(a, name + str(i) + '_')
                    i += 1
            else:
                out[name[:-1]] = x

        flatten(y)
        return out

    def format_date(self, date_str):
        if date_str == 'Ongoing':
            return date_str
        year = date_str[0:4]
        month = date_str[4:6]
        day = date_str[6:]

        return year + '-' + month + '-' + day

# corresponding to medicare eligibility in sf
class basic_info_parser(parser):
    def __init__(self):
        self.field_mapping = field_mapping.get_basic_info_field_mapping()
        self.condition_map = field_mapping.get_basic_info_condition_field_mapping()
    def parse_condition(self, json_content):
        flat_field_mapping = self.flatten_json(self.condition_map)
        flat_json = self.flatten_json(json_content)
        res = {}

        if 'Result_Date_Date01_@value' in flat_json.keys():
            if flat_json['Result_Date_Date01_@value'] == "Date of Death":
                res['DOD__c'] = self.format_date(flat_json["Result_Date_Date03_@value"])

        if 'Result_Section_Eligibility_Eligibility03_@value' in flat_json.keys():

            if flat_json['Result_Section_Eligibility_Eligibility03_@value'] == 'Part A':
                if 'Result_Section_Date_Date03_@value' in flat_json.keys():
                    if len(flat_json['Result_Section_Date_Date03_@value']) < 17:
                        res['PartAEligibilityStart__c'] = flat_json['Result_Section_Date_Date03_@value']
                        res['PartAEnd__c'] = "Ongoing"
                    else:
                        dates = flat_json['Result_Section_Date_Date03_@value'].split('-')
                        res['PartAEligibilityStart__c'] = self.format_date(dates[0])
                        res['PartAEnd__c'] = self.format_date(dates[1])


                if flat_json['Result_Section_Eligibility_Eligibility03_@value'] == 'Part B':
                    if len(flat_json['Result_Section_Date_Date03_@value']) < 17:
                        res['PartBEligibilityStart__c'] = self.format_date(flat_json['Result_Section_Date_Date03_@value'])
                        res['PartBEnd__c'] = "Ongoing"
                    else:
                        dates = flat_json['Result_Section_Date_Date03_@value'].split('-')
                        res['PartBEligibilityStart__c'] = self.format_date(dates[0])
                        res['PartBEnd__c'] = self.format_date(dates[1])



        return res
    def parse(self, json_content):
        tmp = super(basic_info_parser, self).parse(json_content)
        if 'DOB__c' in tmp.keys():
            tmp['DOB__c'] = self.format_date(tmp['DOB__c'])

        return tmp

class inpatient_parser(parser):
    def __init__(self):
        self.field_mapping = field_mapping.get_inpatient_field_mapping()

    def parse_condition(self, map):
        flat_json = self.flatten_json(map)
        res = {}
        # print(map['Section'])
        # print(flat_json)
        if 'Result_Section_Eligibility_Eligibility01_@value' not in flat_json.keys() or flat_json['Result_Section_Eligibility_Eligibility01_@value'] != 'Deductible' or \
                'Result_Section_Eligibility_Eligibility03_@value' not in flat_json.keys() or flat_json['Result_Section_Eligibility_Eligibility03_@value'] != 'Plan Waiting Period' or \
                'Result_Section_Eligibility_Eligibility04_@value' not in flat_json.keys() or flat_json['Result_Section_Eligibility_Eligibility04_@value'] != 'Medicare Part A' or \
                'Result_Section_Eligibility_Eligibility06_@value' not in flat_json.keys() or flat_json['Result_Section_Eligibility_Eligibility06_@value'] != 'Remaining':
            return None
        else:
            res['PartADeductibleLeft__c'] = float(flat_json['Result_Section_Eligibility_Eligibility07_@value'])

        if 'Result_Section_Date_Date03_@value' not in flat_json.keys():
            return None

        date_str = flat_json['Result_Section_Date_Date03_@value']

        start_year = date_str[0:4]
        end_year = date_str[9:13]
        current_year = str(datetime.now().year)
        # print(start_year)
        # print(current_year)
        if start_year != current_year and end_year != current_year:
            # should I send email
            return None
        else:
            res['InpatientStartDate__c'] = self.format_date(date_str[0:8])
            try:
                res['InpatientEndDate__c'] = self.format_date(date_str[9:17])
            except:
                res['InpatientEndDate__c'] = 'Ongoing'

        # print('inpa')
        # print(flat_json)
        return res

class deductible_caps_parser(parser):
    def __init__(self):
        self.field_mapping = field_mapping.get_deductible_caps_field_mapping()

    def parse_condition(self, map):
        flat_json = self.flatten_json(map)
        res = {}
        if 'Result_Section_Eligibility_Eligibility01_@value' not in flat_json.keys() or flat_json[
            'Result_Section_Eligibility_Eligibility01_@value'] != 'Deductible' or \
                'Result_Section_Eligibility_Eligibility03_@value' not in flat_json.keys() or flat_json[
            'Result_Section_Eligibility_Eligibility03_@value'] != 'Plan Waiting Period' or \
                'Result_Section_Eligibility_Eligibility04_@value' not in flat_json.keys() or flat_json[
            'Result_Section_Eligibility_Eligibility04_@value'] != 'Medicare Part B' or \
                'Result_Section_Eligibility_Eligibility06_@value' not in flat_json.keys() or flat_json[
            'Result_Section_Eligibility_Eligibility06_@value'] != 'Remaining':
            return None
        else:
            res['PartBDeductibleLeft__c'] = float(flat_json['Result_Section_Eligibility_Eligibility07_@value'])

        date_str = flat_json['Result_Section_Date_Date03_@value']

        start_year = date_str[0:4]
        end_year = date_str[9:13]
        current_year = str(datetime.now().year)
        # print(start_year)
        # print(current_year)
        if start_year != current_year and end_year != current_year:
            # should I send email
            return None
        else:
            res['PartBYear__c'] = int(current_year)

        return res

class QMB_Status_parser(parser):
    def __init__(self):
        self.field_mapping = field_mapping.get_qmb_field_mapping()

    def parse_condition(self, map):
        flat_json = self.flatten_json(map)
        # print(flat_json)
        res = {}
        if 'Result_Section_Eligibility_Eligibility01_@value' not in flat_json.keys() or flat_json[
            'Result_Section_Eligibility_Eligibility01_@value'] != 'Other or Additional Payor' or \
                'Result_Section_Eligibility_Eligibility04_@value' not in flat_json.keys() or flat_json[
            'Result_Section_Eligibility_Eligibility04_@value'] != 'QMB' or \
                'Result_Section_Eligibility_Eligibility05_@value' not in flat_json.keys() or 'QMB Plan' not in flat_json[
            'Result_Section_Eligibility_Eligibility05_@value']:
            return None
        else:
            date_str = flat_json['Result_Section_Date_Date03_@value']
            res['QmbStartDate__c'] = self.format_date(date_str[0:8])
            try:
                res['QmbEndDate__c'] = self.format_date(date_str[9:17])
            except:
                res['QmbEndDate__c'] = 'Ongoing'

        return res



# what if address is null, then no date? msp type, policy number, insurer name pending
class msp_parser(parser):
    def __init__(self):
        self.field_mapping = field_mapping.get_msp_static_field_mapping()
        self.condition_map = field_mapping.get_msp_conditional_field_mapping()

    def parse_condition(self, map):
        flat_json = self.flatten_json(map)
        # flat_mapping = self.flatten_json(self.condition_map)
        # print('response')
        # print(flat_json)
        # print(flat_mapping)
        if 'Result_Section_Date_Date03_@value' not in flat_json.keys():
            return {}
        start_date = flat_json['Result_Section_Date_Date03_@value'][0:8]
        end_date = flat_json['Result_Section_Date_Date03_@value'][9:] if len(flat_json['Result_Section_Date_Date03_@value']) == 17 else 'Ongoing'
        end_date = self.format_date(end_date)
        start_date = self.format_date(start_date)
        return {'StartDate':start_date, 'EndDate':end_date}

class plan_coverage_parser(parser):
    def __init__(self):
        self.field_mapping = field_mapping.get_plan_coverage_static_field_mapping()
        self.condition_map = field_mapping.get_plan_coverage_conditional_field_mapping()

    def parse_condition(self, map):
        flat_json = self.flatten_json(map)
        flat_map = self.flatten_json(self.condition_map)
        # print(flat_json)
        # print(flat_map)
        res = {}
        plan_type = []


        # collect all the plan types
        for key in flat_map.keys():
            if key.startswith('Result_Section_Eligibility_Eligibility04_@value'):
                plan_type.append(flat_map[key])

        # if there is no this key means invalid
        if 'Result_Section_Eligibility_Eligibility04_@value' not in flat_json.keys():
            return None

        if flat_json['Result_Section_Eligibility_Eligibility04_@value'] in plan_type:
            res['PlanType__c'] = flat_json['Result_Section_Eligibility_Eligibility04_@value']

        if 'Result_Section_Date_Date03_@value' in flat_json.keys():
            if len(flat_json['Result_Section_Date_Date03_@value']) == 17:
                res['PlanCoverageStartDate__c'] = self.format_date(flat_json['Result_Section_Date_Date03_@value'].split('-')[0])
                res['PlanCoverageEndDate__c'] = self.format_date(flat_json['Result_Section_Date_Date03_@value'].split('-')[1])
            else:
                res['PlanCoverageStartDate__c'] = self.format_date(flat_json['Result_Section_Date_Date03_@value'][0:8])
                res['PlanCoverageEndDate__c'] = 'Ongoing'

        return res

    def parse(self, json_content):
        tmp =  super(plan_coverage_parser, self).parse(json_content)

        # if no plan type means it's invalid
        if tmp == None or 'PlanType__c' not in tmp.keys():
            return None
        else:
            return tmp

class part_d_parser(parser):
    def __init__(self):
        self.field_mapping = field_mapping.get_part_d_static_field_mapping()
        self.condition_map = field_mapping.get_part_d_conditional_field_mapping()

    def parse_condition(self, map):
        flat_json = self.flatten_json(map)
        flat_mapping = self.flatten_json(self.condition_map)

        res = {}

        # get info 3 key, in case the data structure is different
        # plan_name_key = ''
        for key in flat_json.keys():
            if 'Info03' in key:
                if flat_json['Result_Section_Eligibility_Eligibility04_@value'] == 'Medicare Part D':
                    res['PartDName__c'] = 'Medicare Part D'
                    res['PlanId__c'] = flat_json[key]

        if 'Result_Section_Date_Date03_@value' in flat_json.keys():

            date_str = flat_json['Result_Section_Date_Date03_@value']

            if len(date_str) == 17:
                res['PartDStartDate__c'] = self.format_date(date_str.split('-')[0])
                res['PartDEndDate__c'] = self.format_date(date_str.split('-')[1])
            else:
                res['PartDStartDate__c'] = self.format_date(date_str[0:8])
                res['PartDEndDate__c'] = 'Ongoing'
        # print(flat_json)
        # print(flat_mapping)

        return res

    def parse(self, json_content):
        tmp = super(part_d_parser, self).parse(json_content)

        # if no plan type means it's invalid
        if 'PartDName__c' not in tmp.keys():
            return None
        else:
            return tmp

class error_parser(parser):
    def __init__(self):
        self.field_mapping = field_mapping.get_error_mapping()

