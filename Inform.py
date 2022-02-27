#coding = utf-8
import os
import configparser
import sendmail
import json
import inform_mail
import time

def read_userdata_json():
    json_filename = 'user_data_test.json'
    with open(json_filename,encoding='UTF-8') as f:
        user_data = json.load(f)
    return user_data

fs = open('Inform.txt',encoding='UTF-8')
inform_content = fs.read()
email = inform_mail.mail()
user_data = read_userdata_json()
for user in user_data:
    time.sleep(100)
    e_mail = user['mail']
    email.mail(inform_content,e_mail)

# json_filename = './post_data.json'
# post_data = {}
# post_data['uid'] = '20177710735'
# post_data['upw'] = '11042513'
# post_data['smbtn'] = '进入健康状况上报平台'
# post_data['hh28'] = '686'
# with open(json_filename,'w',encoding='UTF-8') as f:
#     json.dump(post_data,f)
# with open(json_filename,encoding='UTF-8') as f:
#     test = json.load(f)
#     print(test)

#print(submit_data['myvs_13a'])
# proDir = os.path.split(os.path.realpath(__file__))[0]
# configPath = os.path.join(proDir,"config.ini")
# parser = configparser.ConfigParser()
# parser.read(configPath,encoding='UTF-8')
# send_mail = {}
# send_mail = parser.items('sendmail')
# host_server = send_mail[0][1]
# print(send_mail[0][1])
# print(parser.get("userdata",'username'))