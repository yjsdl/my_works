# -*- coding: utf-8 -*-
# @Time    : 2022/10/25 21:25
# @Author  : Liuyijie
# @File    : one.py
import random

import ddddocr
import requests


t = random.random()
over_url = f'https://oversea.cnki.net/kns/Brief/VerifyCode?t={t}'
headers = {
        "Cookie": "cangjieStatus_OVERSEA2=false; Ecp_ClientId=b221016173201619969; Ecp_ClientIp=121.237.217.55; UM_distinctid=183eaf91a078b6-0c646a46d4ef1e-977173c-144000-183eaf91a08c18; dperpage=50; dsorder=pubdate; ASPSESSIONIDQARDTRTA=LPJKPPEBBEJLHPJBNIGPDOEN; eng_k55_id=123103; Ecp_IpLoginFail=221022121.237.217.55; ASP.NET_SessionId=nouspgfcgudat5b5ytbojb02; knsLeftGroupSelectItem=1%3B2%3B; CurrSortField=Publication+Date%2f(%e5%8f%91%e8%a1%a8%e6%97%b6%e9%97%b4%2c%27TIME%27); CurrSortFieldType=desc; CNZZDATA1279462118=1508356872-1666091275-https%253A%252F%252Foversea.cnki.net%252F%7C1666430456; dblang=ch; _pk_ref=%5B%22%22%2C%22%22%2C1666433370%2C%22https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3Di8Csp0pHLNmJkJFYN8G10bb-N3B5mxZamgcvGnirAfe%26wd%3D%26eqid%3D945bf58100058a7d00000004634ea68a%22%5D; _pk_id=3fc3a8d4-1b31-416b-86a9-60da97b77b4f.1665912785.4.1666433370.1666433370.; _pk_ses=*",
        "Referer": "https://oversea.cnki.net/kns/AdvSearch?dbcode=CFLS&crossDbcodes=CJFQ,CDMD,CIPD,CCND,CYFD,CCJD,BDZK,CISD,CJFN",
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    }

res = requests.get(over_url, headers=headers)

ocr = ddddocr.DdddOcr()

# with open('../test/img_2.png', 'rb') as f:
#     img_btyes = f.read()

res = ocr.classification(res.content)
print(res)