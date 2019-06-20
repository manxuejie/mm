import urllib.request
proxy_handle=[
    {'http':'http://163.204.240.162:9999'},{'http':'http://61.183.233.6:54896'},{'http':'http://175.44.154.85:9000'}
]
proxy = urllib.request.ProxyHandler(proxy_handel)
urls = 'http://www.kuaidaili.com'
for url in urls:
    opener = urllib.request.build_opener(proxy)
    response = opener.open('http://163.204.240.162:9999','http://61.183.233.6:54896','http://175.44.154.85:9000')
    print(response.status)
    if response.status!=200:
        random.sample(response)
    else:
        print('该网站爬取失败')