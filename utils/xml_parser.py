import json
import xmltodict

class xml_parser:
    def xml_to_json(self, xml_content):
        # print(type(xml_content))
        # print(type(json.loads(xml_content)))
        res_dict = json.loads(xml_content)
        return json.loads(json.dumps(xmltodict.parse(res_dict['Root'])))
