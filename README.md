# xijiu
习酒官方微信小程序自动签到
## 食用方法
1、抓包请求中的token值

示例：
```bash
token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJtZW1iZXJJbmZvIjp7ImlkIjo2ODI3MjY5fSwiZXhwaXJlVGltZSI6MTY1MDgxNDM2NH0.phfp40CA5MuXFfPyR7ee_tHZEIOhAOAfi93vM_C1vio
```

可在登陆get请求的网址中找到
```bash
https://mallwm.exijiu.com/?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJtZW1iZXJJbmZvIjp7ImlkIjo2ODI3MjY5fSwiZXhwaXJlVGltZSI6MTY1MDgxNDM2NH0.phfp40CA5MuXFfPyR7ee_tHZEIOhAOAfi93vM_C1vio&ts=1650254716983#/
```
或者抓包post请求的`Authorization`值

2、填入sign.py文件中
```bash
if __name__ == '__main__':
    #这里填入token，需要抓包获得
    token = ''
    start = xijiu(token=token)
    start.main()
```
最后运行脚本
```bash
python3 sign.py
```
