import json
import time

from flask import Flask, request, render_template
from process.process import processor
from med_connector.med_api_connector import med_api_connector
import yagmail
import traceback
application = Flask(__name__)


@application.route('/medicare',methods=['GET', 'POST'])
def medicare():
    try:
        request_body = request.get_data().decode('utf-8')

        request_paras = json.loads(request_body)

        data_points = {}
        data_points['hic'] = request_paras['hic']
        data_points['firstname'] = request_paras['firstname']
        data_points['lastname'] = request_paras['lastname']
        data_points['dob'] = request_paras['dob']
        data_points['npi'] = request_paras['npi']
        data_points['service'] = request_paras['service']
        data_points['api_key'] = request_paras['api_key']
        data_points['acctid'] = request_paras['acctid']

        return processor().process(data_points)
    except Exception as e:
        body = str(traceback.format_exc())

        yag = yagmail.SMTP("yang.wuxuan@accelerize360.com", password="@Ywx19950604")
        yag.send(
            to=["elite@accelerize360.com"],
            subject='Medicare AWS Internal Error' + ' ' + time.strftime("%Y-%m-%d-%H%M%S", time.localtime()),
            contents=body
        )

        return 'Internal Error'

@application.route('/credential',methods=['GET', 'POST'])
def credential():
    username = request.form['username']
    password = request.form['password']
    api = request.form['apiKey']
    accesskey = request.form['accesskey']
    res = med_api_connector(1,1,1).change_credential(username, password, api, accesskey)
    return res



@application.route('/',methods=['GET', 'POST'])
def index():
    return render_template('index.html')


if __name__ == '__main__':
    application.run()
