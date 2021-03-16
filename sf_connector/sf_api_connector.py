from simple_salesforce import Salesforce

class sf_api_connector:
    def __init__(self, username, password, security_token, organizationId, domain):
        self.connector = Salesforce(username=username,
                                    password=password,
                                    security_token=security_token,
                                    organizationId=organizationId,
                                    domain=domain) if domain != None \
                        else Salesforce(username=username,
                                        password=password,
                                        security_token=security_token,
                                        organizationId=organizationId)

    def create_objects_by_list(self, object_name, dataset):
        pass

    def create_medicare_object(self, data, acctid):
        data['Account__c'] = acctid
        return self.connector.MedicareEligibility__c.create(data)

    # data: {'ObjectName1':'body1', 'Object2':'body2'}
    def create_or_update_objects_by_dict(self, data, acctid):
        if 'MedicareEligibility__c' in data.keys() and data['MedicareEligibility__c'] != None:
            data['MedicareEligibility__c']['Account__c'] = acctid

            # if exist, extract the med id
            med_id = self.get_id_if_exist('MedicareEligibility__c', data['MedicareEligibility__c'])

            # operate sf db
            med_response = self.create_or_update_object('MedicareEligibility__c', data['MedicareEligibility__c'], med_id)

            # if it's creation, there will be id in the response, if it's update it'll respond 204 int
            if isinstance(med_response, int) == False:
                med_id = med_response['id']

            # print(med_response)

        # for objects not med
        for key in data.keys():
            if key != 'MedicareEligibility__c' and data[key] != None:
                # bind med id
                data[key]['MedicareEligibility__c'] = med_id
                # detect if cihld id exists, if yes update, if not create
                child_id = self.get_id_if_exist(key, data[key])
                print(self.create_or_update_object(key, data[key], child_id))

    def get_id_from_response(self, response):
        return response[0]['id']
    def query(self, sql):
        records = self.connector.query_all(sql)['records']
        return records

    def get_id_if_exist(self, object_name, body):
        query = """Select Id from obj where parentLookup='parentId'"""
        query = query.replace("obj", object_name)
        if object_name == 'MedicareEligibility__c':
            query = query.replace('parentLookup', 'Account__c')
            query = query.replace('parentId', body['Account__c'])
            result = self.query(query)

            return result[0]['Id'] if len(result) > 0 else None

        else:
            query = query.replace('parentLookup', 'MedicareEligibility__c')
            query = query.replace('parentId', body['MedicareEligibility__c'])
            result = self.query(query)

            return result[0]['Id'] if len(result) > 0 else None


    # detect if there is already a obj, of there is, update, otherwise create
    def create_or_update_object(self, object_name, body, id):
        if id == None:
            if object_name == 'MedicareEligibility__c':
                return self.connector.MedicareEligibility__c.create(body)
            elif object_name == 'Inpatient__c':
                return self.connector.Inpatient__c.create(body)
            elif object_name == 'DeductibleCap__c':
                return self.connector.DeductibleCap__c.create(body)
            elif object_name == 'QmbStatus_c':
                return self.connector.QmbStatus_c.create(body)
            elif object_name == 'MSP__c':
                return self.connector.MSP__c.create(body)
            elif object_name == 'PlanCoverage__c':
                return self.connector.MSP__c.create(body)
            elif object_name == 'PartD__c':
                return self.connector.MSP__c.create(body)
        else:
            if object_name == 'MedicareEligibility__c':
                return self.connector.MedicareEligibility__c.update(id, body)
            elif object_name == 'Inpatient__c':
                return self.connector.Inpatient__c.update(id, body)
            elif object_name == 'DeductibleCap__c':
                return self.connector.DeductibleCap__c.update(id, body)
            elif object_name == 'QmbStatus_c':
                return self.connector.QmbStatus_c.update(id, body)
            elif object_name == 'MSP__c':
                return self.connector.MSP__c.update(id, body)
            elif object_name == 'PlanCoverage__c':
                return self.connector.MSP__c.update(id, body)
            elif object_name == 'PartD__c':
                return self.connector.MSP__c.update(id, body)

