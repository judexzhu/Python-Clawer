import requests
from bs4 import BeautifulSoup

waybillNo_list =['534222596899', '534222596904', '534222596911']

headers = {
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding':'gzip, deflate, sdch',
    'Accept-Language':'en,en-US;q=0.8,zh;q=0.6,zh-CN;q=0.4',
    'Connection':'keep-alive',
    'Host':'www.zto.com',
    'Referer':'http://www.zto.com/GuestService',
    'Upgrade-Insecure-Requests':'1',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
}

for waybillNo in waybillNo_list:

    payload = {
        'waybillNo': waybillNo
    }

    res = requests.get("http://www.zto.com/GuestService/BillNew?model.TxtBill="+str(waybillNo),headers = headers)

    result = BeautifulSoup(res.text,"html5lib").select('.on')[-1].text.strip()
    
    print waybillNo + "; "+ str(result.encode('utf8')).replace(",感谢您使用中通快递，期待再次为您服务!International delivery.", "")
