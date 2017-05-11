import requests
from bs4 import BeautifulSoup

waybillNo_list =['810131162977', '810131167088', '810131151219', '810131166299']

headers = {
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding':'gzip, deflate',
    'Accept-Language':'en,en-US;q=0.8,zh;q=0.6,zh-CN;q=0.4',
    'Cache-Control':'max-age=0',
    'Connection':'keep-alive',
    'Content-Length':'46',
    'Content-Type':'application/x-www-form-urlencoded',
    'Host':'trace.yto.net.cn:8022',
    'Origin':'http://www.yto.net.cn',
    'Referer':'http://www.yto.net.cn/gw/index/index.html',
    'Upgrade-Insecure-Requests':'1',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
}

for waybillNo in waybillNo_list:

    payload = {
        'waybillNo': waybillNo
    }

    res = requests.post("http://trace.yto.net.cn:8022/TraceSimple.aspx",data = payload, headers = headers)

    result = BeautifulSoup(res.text,"html5lib").select('.data')[-1].text.strip()
    
    print waybillNo + "; "+ str(result.encode('utf8')).replace("感谢使用圆通速递，期待再次为您服务", "")
