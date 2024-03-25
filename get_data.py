import requests
import base64
from time import time
import zlib
import urllib.parse
import pandas as pd


class meituan(object):
    def __init__(self):
        self.headers = {
            "Host": "yb.meituan.com",
            "Connection": "keep-alive",
            "Accept": "application/json",
            "Sec-Fetch-Dest": "empty",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36",
            "Sec-Fetch-Site": "same-origin",
            "Sec-Fetch-Mode": "cors",
            "Referer": "https://yb.meituan.com/meishi/rating/",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Cookie": "_lxsdk_cuid=185188cb19353-0eb39bc2e37afd-26021151-144000-185188cb194c8; iuuid=FAD86E30E0D08A6C8724DC3AFCFD37DD8B56046D81230E96D67D2EE079209085; _lxsdk=FAD86E30E0D08A6C8724DC3AFCFD37DD8B56046D81230E96D67D2EE079209085; _hc.v=46a71999-b43b-829f-11d0-30cc4e753289.1671154383; WEBDFPID=9617z7v5v4745z49yuwvuv11x004uwzy81481096y079795813z71w93-1986514383173-1671154382871UOUCIGGfd79fef3d01d5e9aadc18ccd4d0c95079239; lat=28.804902; lng=104.610499; mtcdn=K; _lx_utm=utm_source%3DBaidu%26utm_medium%3Dorganic; client-id=ec841b95-229f-48a4-9646-9e99d3ad7082; lt=AgE1JG9qcji2czrsvHzQGcS6hXspGVJXU1M6PM-dcbO7bHAgCXMAjoWdWd4Ryf5_v7hVVV-GgzVN2AAAAADnFQAA8Me7l6xHwfANnPArxNDJhxnV0UMEsr9c84CHZ3qkJV0ENyGLFFiyE6P5v5ofry_k; u=1916576532; n=XxJ796768323; token2=AgE1JG9qcji2czrsvHzQGcS6hXspGVJXU1M6PM-dcbO7bHAgCXMAjoWdWd4Ryf5_v7hVVV-GgzVN2AAAAADnFQAA8Me7l6xHwfANnPArxNDJhxnV0UMEsr9c84CHZ3qkJV0ENyGLFFiyE6P5v5ofry_k; unc=XxJ796768323; ci=313; rvct=313%2C59%2C1; firstTime=1672823212602; __mta=44390939.1671154197038.1672725388068.1672823212621.29; _lxsdk_s=1857c069870-06b-dd0-511%7C%7C26"
        }

    def get_query(self, page):
        # 地点名称
        cityName = '宜宾'
        # 美食类型
        cateId = 0
        # 地区类型
        areaId = 0
        # 分类方法
        sort = ''
        dinnerCountAttrId = ''
        # 查询页数
        page = page
        userId = ''
        uuid = '3bcf687243ae42cf94f2.1660875247.1.0.0'
        platform = 1
        partner = 126
        riskLevel = 1
        optimusCode = 10
        originUrl = 'https://yb.meituan.com/meishi/rating/'
        query = 'cityName=%s&cateId=%d&areaId=%d&sort=%s&dinnerCountAttrId=%s&page=%d&userId=%s&uuid=%s&platform=%d&partner=%d&originUrl=%s&riskLevel=%d&optimusCode=%d' % (
        cityName, cateId, areaId, sort, dinnerCountAttrId, page, userId, uuid, platform, partner, originUrl, riskLevel,
        optimusCode)
        query_after = query.split('&')
        "areaId=0&cateId=0&cityName=宜宾&dinnerCountAttrId=&optimusCode=10&originUrl=https://yb.meituan.com/meishi/rating/&page=1&partner=126&platform=1&riskLevel=1&sort=&userId=&uuid=3bcf687243ae42cf94f2.1660875247.1.0.0"
        query_all = []
        true_query = ''
        for i in query_after:
            i = i.split('=')
            if i == query_after[-1]:
                query_all.append(i[0] + '=' + i[1])
            else:
                query_all.append(i[0] + '=' + i[1] + '&')
        for j in sorted(query_all):
            true_query += j
        true_query = "\"" + true_query + "\""
        sign = self.algorithm(true_query)
        sign = sign[2:-1]
        token = self.get_token(sign)
        # 将token进行url编码,否则API后台不识别数据返回数据null
        token1 = urllib.parse.quote(token)
        return query + '&_token=' + token1

    def get_token(self, sign):
        refer = "https://yb.meituan.com/meishi/rating/"
        local_href = "https://yb.meituan.com/meishi/"
        token = {
            'rId': 100900,
            'ver': "1.0.6",
            'ts': int(round(time() * 1000) - 150 * 1000),
            'cts': int(round(time() * 1000)),
            'brVD': [406, 754],
            'brR': [[1536, 864], [1536, 824], 24, 24],
            'bI': [local_href, refer],
            'mT': [],
            'kT': [],
            'aT': [],
            'tT': [],
            'aM': "",
            'sign': "eJwljjFuwzAMRe+SQaMsxbGjFtBQeCpQZMsBmJixiVqSQVEFeoQsmXOUHKjoOSK0038g/v/8G2CE99EbdQbBfyD5PkBA//O4/t5vaqQYkYdUoryJcPWotAqFkoc0ordGJaaJ4pEXP4us+bVpctABSQpEfU6hqZxnatQKUw1UYamV3m57tS4gl8Shnpny5wd+4VI5JxavSsa/f6VQXQYn111w/+Kw28G2h1NrtO1c2ztr3U5bbbTZPAGMkUe8"
        }

        # print(str(token))
        result = self.algorithm(token)
        return result

    # 破解动态token
    def algorithm(self, inf):
        # 直接zlib压缩提示要转字节类型
        info = str(inf).encode()
        # 进行def压缩
        temp = zlib.compress(info)
        # 压缩后进行base64加密
        baseenco = base64.b64encode(temp)
        # 加密后转str文本
        result = str(baseenco, encoding='utf-8')
        return result

    def get_lis(self):
        dt = {'店铺评论数': [], '店铺名称': [], '评分': [], '店铺地址': [], '人均金额': []}
        for page in range(1, 4):
            resp = requests.get(url='https://yb.meituan.com/meishi/api/poi/getPoiList?' + self.get_query(page),
                                headers=self.headers, verify=False)
            response = resp.json()
            datas = response['data']['poiInfos']
            for data in datas:
                dt['店铺评论数'].append(data['allCommentNum'])
                dt['店铺名称'].append(data['title'])
                dt['评分'].append(data['avgScore'])
                dt['店铺地址'].append(data['address'])
                dt['人均金额'].append(data['avgPrice'])

        print(dt)
        dt = pd.DataFrame(dt)
        print(dt)
        dt.to_excel('美团数据.xlsx', encoding='gbk', index=False)

    def run(self):
        self.get_lis()


if __name__ == '__main__':
    parse = meituan()
    parse.run()
