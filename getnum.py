#!/usr/bin/python3
# coding=utf-8

import urllib3
import requests
import re
from bs4 import BeautifulSoup

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

host = 'jksb.v.zzu.edu.cn'

header = {"Origin": "https://jksb.v.zzu.edu.cn",
          "Referer": "https://jksb.v.zzu.edu.cn/vls6sss/zzujksb.dll/first0?fun2=s&door=63215i",
          # "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
          #               "Chrome/83.0.4103.116 Safari/537.36 Edg/83.0.478.56",
          "Host": "jksb.v.zzu.edu.cn"
          }

header2 = {"Referer": "https://jksb.v.zzu.edu.cn/vls6sss/zzujksb.dll/login",
           # "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
           #               "Chrome/83.0.4103.116 Safari/537.36 Edg/83.0.478.56",
           "Host": "jksb.v.zzu.edu.cn"
           }

post_data = {"uid": "", "upw": "", "smbtn": "领取郑州大学通行码", "hh28": "664", "fun2": "s",
             "door": "63215i"}

# verify_path = "/etc/ssl/certs"
verify_path = False


# Get SID and PTOPID from window.location/(post)
def re_sp(url):
    data = ''.join(url)
    data = data.split('=')
    sid = data[2]
    ptopid = data[1].split('&')
    ptopid = ptopid[0]
    return sid, ptopid


# get window.location
def url_window(html):
    html.encoding = 'utf-8'
    html = html.text
    soup = BeautifulSoup(html, 'html.parser')
    datas = soup.find('script')
    datas = datas.string
    pattern = re.compile(r'window.location="(http.*?)"', re.I | re.M)
    url = pattern.findall(datas)
    print(url)
    return url


# get number
def find_num(html):
    html.encoding = 'utf-8'
    html = html.text
    soup1 = BeautifulSoup(html, 'html.parser')
    pattern = re.compile(r"title316_\d{5}")
    pattern2 = re.compile(r"\d{5}")
    num = soup1.find(id="bak_0")
    num = pattern.search(str(num)).group()
    num = pattern2.search(str(num)).group()
    print(num)
    return num


# post at the first time
def post_url():
    session = requests.Session()
    html = session.post('https://jksb.v.zzu.edu.cn/vls6sss/zzujksb.dll/login', data=post_data, headers=header,
                        verify=verify_path)
    # html.encoding = 'utf-8'
    # print(html.text)
    return html


# get at the first time
def get_url(url):
    session = requests.Session()
    html = session.get(url, headers=header2, verify=verify_path)
    return html



