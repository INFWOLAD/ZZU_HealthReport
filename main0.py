#!/usr/bin/python3
#coding=utf-8

import jksb
import json
import requests
import base64
import time
import sys
import os
import configparser


def init():
    time.sleep(int(100))

def get_filepath():
    file_path = "/ql/scripts/INFWOLAD_zzujksb/"
    return file_path

def read_submitdata_json(file_path):
    json_filename = file_path + 'submit_data.json'
    with open(json_filename,encoding='UTF-8') as f:
        submit_data = json.load(f)
    return submit_data

def read_userdata_json(file_path):
    json_filename = file_path + 'user_data.json'
    with open(json_filename,encoding='UTF-8') as f:
        user_data = json.load(f)
    return user_data

def read_postdata_json(file_path):
    json_filename = file_path + 'post_data.json'
    with open(json_filename,encoding='UTF-8') as f:
        post_data = json.load(f)
    return post_data

def write_postdata_json(uid,upw):
    json_filename = file_path + 'post_data.json'
    post_data = {}
    post_data['uid'] = uid
    post_data['upw'] = upw
    post_data['smbtn'] = '进入健康状况上报平台'
    post_data['hh28'] = '686'
    with open(json_filename,'w',encoding='UTF-8') as f:
        json.dump(post_data,f)
    return submit_data
    
def send_to_wecom(text,wecom_cid,wecom_aid,wecom_secret,wecom_touid):
    get_token_url = f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={wecom_cid}&corpsecret={wecom_secret}"
    response = requests.get(get_token_url).content
    access_token = json.loads(response).get('access_token')
    if access_token and len(access_token) > 0:
        send_msg_url = f'https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token={access_token}'
        data = {
            "touser":wecom_touid,
            "agentid":wecom_aid,
            "msgtype":"text",
            "text":{
                "content":text
            },
            "duplicate_check_interval":600
        }
        response = requests.post(send_msg_url,data=json.dumps(data)).content
        return response
    else:
        return False

if __name__ == '__main__':
    file_path = get_filepath()
    submit_data = read_submitdata_json(file_path)
    user_data = read_userdata_json(file_path)
    for user in user_data:
        submit_data['myvs_13a']=user['province']
        submit_data['myvs_13b']=user['city']
        submit_data['myvs_13c']=user['p_c']
        submit_data['myvs_30']=user['school']
        
        write_postdata_json(user['uid'],user['upw'])
        post_data = read_postdata_json(file_path)
        post = jksb.jksb(user,post_data,submit_data)
        slipname=user["username"]

        url = post.post_url()
        if url != 0:
            url1 = post.get_url1(url)
            if url1 != 0:
                # hea3['Referer'] = url1
                if post.get_url2(url1)== True:
                    email_message = post.jksb()
                    print("用户名："+ user["username"] +"  打卡成功")
                    send_to_wecom("【⏰健康打卡程序⏰】\n用户名："+ user["username"] + "\n您今日已成功健康打卡\n请在遵守防疫规范的情况下使用本脚本\n程序版本：22.01.11\n更多设置访问：", "", "", "",user["wecomid"]);
                else:
                    print("用户名："+ user["username"] +"  重复打卡")
            else:
                 print("用户名："+ user["username"] +"  打卡错误/失败")
        else:
             print("用户名："+ user["username"] +"  打卡错误/失败")
        init()