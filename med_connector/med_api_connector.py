import json

from utils.xml_parser import xml_parser
import requests

class med_api_connector:
    def __init__(self, username, password, access_key):
        self.username = username
        self.password = password
        self.access_key = access_key

    def get_response(self, data_points):
        url = 'https://2lkdff1u2a.execute-api.us-east-1.amazonaws.com/sf-med-api'
        r = requests.post(url=url, data=json.dumps(data_points))
        return r.content.decode('utf-8')

    def execute(self, data_points):
        raw_xml_response = self.get_response(data_points)
        # print(raw_xml_response)
        return xml_parser().xml_to_json(raw_xml_response)

    def change_credential(self, username, password, api_key, accesskey):
        body = {'username': username,
                'password': password,
                'api': api_key,
                'accesskey' : accesskey}

        print(body)
        
        r = requests.post(url='https://fxo48mt8q6.execute-api.us-east-1.amazonaws.com/med-credential',
                          data=json.dumps(body))

        # update aws
        return r.content.decode('utf-8')
