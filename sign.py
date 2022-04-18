# author: viiber
# date: 2022/4/18
# version: 1.0
# description: 习酒微信小程序每日签到

import datetime
import requests
import re
import time

class xijiu():
    def __init__(self, token):
        timestamp = round(time.time())
        self.token = token
        self.url = f'https://mallwm.exijiu.com/?token={self.token}&ts={timestamp}#/'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 MicroMessenger/7.0.9.501 NetType/WIFI MiniProgramEnv/Windows WindowsWechat',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Accept-Language': 'en-us,en',
            'Accept-Encoding': 'gzip, deflate, br',
        }
        self.session = requests.session()
        
    def getpage(self):
        headers1 = {
            'Connection': 'keep-alive',
            'Host': 'mallwm.exijiu.com',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'sec-fetch-user': '?1',
            'Upgrade-Insecure-Requests': '1',
        }
        headers1.update(self.headers)
        response = self.session.get(self.url, headers=headers1)
        title = re.findall('<title>\s*(.*?)\s*?</title>', response.text)
        if title[0] == '习酒积分商城':
            print('登录成功')
            return True
        else:
            print('登录失败')
    
    def sign(self):
        headers2 = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Referer': self.url,
            'Authorization':self.token,
            'Sec-Fetch-Dest':'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-site',
            'Host': 'apimallwm.exijiu.com',
            'Content-Length': '22',
        }

        body = {
            'from':'miniprogram_index',
        }
        headers2.update(self.headers)
        time.sleep(2)

        response = self.session.post('https://apimallwm.exijiu.com/member/signin/sign', headers=headers2, data=body)
        print(response.text)
        try:
            data = response.json()
            print(data.get("msg"))
        except:
            print('签到失败')

    def get_sign_info(self):
        headers3 = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Referer': self.url,
            'Authorization':self.token,
            'Sec-Fetch-Dest':'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-site',
            'Host': 'apimallwm.exijiu.com',
        }

        headers3.update(self.headers)
        time.sleep(2)
        response = self.session.get('https://apimallwm.exijiu.com/member/Signin', headers=headers3)
        print(response.text)
    
        data = response.json()
        total = data.get("total")
        print(f'累计签到{total}天')

        try:
            contentdata = data.get("data")
            for content in contentdata:
                create_time = content.get("create_time")
                create_day = re.findall('(.*?)\s+?', create_time)[0]
                if create_day == datetime.datetime.now().strftime('%Y-%m-%d'):
                    print(f'今日已签到{create_day}')
                else:
                    continue
        except:
            print('获取签到信息失败')

    def main(self):
        flag = self.getpage()
        if flag:
            self.sign()
            self.get_sign_info()


if __name__ == '__main__':
    #这里填入token，需要抓包获得
    token = ''
    start = xijiu(token=token)
    start.main()