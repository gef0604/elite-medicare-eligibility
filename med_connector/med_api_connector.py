import json

from utils.xml_parser import xml_parser
from properties import sample
import requests
import boto3

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

    def change_credential(self, username, password, api_key):
        body = {'username': username,
                'password': password,
                'api': api_key}

        print(body)
        # session = boto3.session.Session()
        # client = session.client(
        #     service_name='secretsmanager',
        #     region_name='us-east-1'
        # )
        #
        # response = client.put_secret_value(
        #     SecretId='medicare-eligibility-credentials',
        #     # ClientRequestToken='string',
        #     # Description='string',
        #     # KmsKeyId='string',
        #     # SecretBinary=b'bytes',
        #     SecretString=json.dumps(body))

        # print(response)

        # update aws
        return 'Succeeded'
