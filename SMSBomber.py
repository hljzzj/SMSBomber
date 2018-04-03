import requests
import json
import time



telphone = input('输入电话号码: ')

headers = {
    'user-agent': 'NBorrowMoney/1.2 (iPhone; iOS 11.2.6; Scale/2.00)',
    'Accept-Language': 'zh-Hans-CN;q=1',
    'Accept-Encoding': 'gzip, deflate',
    'Connection': 'keep-alive'
}
# 任性贷
# requests.get('http://115.29.40.93/api/user/getSMSCode?phone=18876116811&type=1&validcode=1234',headers=headers)

# 贷款侠

cookies = requests
headers = {
    'user-agent': 'NBorrowMoney/1.2 (iPhone; iOS 11.2.6; Scale/2.00)',
    'Accept-Language': 'zh-Hans-CN;q=1',
    'Accept-Encoding': 'gzip, deflate',
    'Connection': 'keep-alive',
    'Host': 'mgapi.dalujinrong.cn',
    'channel': 'appstore',
    'app_version': '2.0.0',
    'timestamp': ttt,
    'source': '2',
    'signature': 'F08972B81B1FE8563F53579CF13D877A',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Content-Length': '29',
    'client_id': 'C4779CDD-C343-4EAC-9C15-93C88C61F8B5',
    'public_key': '040CD66A84025B94CEAC3EC1B49C92D0',
    'Cookie': int(round(time.time() * 1000)),
    'app_key': 'ZQXQ-MGDKX',

}
'code_type=2&phone=' + telphone