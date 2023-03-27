import os #导入操作系统接口模块
import sys 
import time #用于计算时间
import datetime

import requests
import bs4 


import parsel   #xpath
#from bs4 import BeautifulSoup

#url编码
from urllib.parse import quote
#url解码
from urllib.parse import unquote

import shutil #用到复制函数

import colorama
#colorama.init(autoreset=True)

#自动颜色需要执行
os.system('')

'''
print('\033[1;31;40m''测试')
print('\033[1;32;41m''测试')
print('\033[1;33;42m''测试')
print('\033[1;34;43m''测试')
print('\033[1;36;44m''测试')
print('\033[1;36;45m''测试')
print('\033[1;37;46m''测试')
print('\033[1;30;47m''测试')

print('\033[1;32;40m', end="")
'''










#-----------------------------------------------------------------------------------------------------
def detection_path(path):
    if os.path.exists(path):
        if os.path.getsize(path):
            #print('文件存在且有数据', path)
            return 0
        else:
            print('文件存在且为空', path)
            return 1
    else:
        print('文件不存在', path)
        return 2

#-----------------------------------------------------------------------------------------------------
#运行main函数
def runmain():

    #inurl="https://www.crrcgo.cc/admin/crr_supplier.html?page="
    #inurl="https://mikanani.me/"
    #inurl="https://mikanani.me/Home/Classic"
    inurl="https://weibo.com/hot/search"

    try:
        path = "test.txt"
        #if detection_path(path) != 0: #检测路径
        #    return 1

        with open(path, "w", encoeding="utf-8") as file1:

            #因为页数是通过js获取的 暂时无法取得

            #读取最大页数
            #outurl=inurl+str(1)
            outurl=inurl
            req = requests.get(url=outurl)
            req.encoding = "utf-8"
            #html=req.text
            #print(req.text)
            soup = bs4.BeautifulSoup(req.text, features="html.parser")
            #print(soup)
            #print(soup, file=file1)

            #company_item = soup.find("div", class_ = "detail_head")
            #company_items = soup.find_all("div",class_="main wrapper")
            company_items = soup.find_all("div")
            #company_items = soup.find_all("div", class_="main_cont")
            #company_items = soup.find_all("div", class_="detail_js")
            #company_items = soup.find_all("div", class_="detail_head")
            #company_items = soup.find_all("div", class_="detail_message")


            #print(company_items)
            for company_item in company_items:

                dd = company_item.text.strip()
                strtmp = str(dd)
                strtmp = strtmp.replace("\xa0", "")
                listtmp = strtmp.split()
                print(listtmp)

                #print(dd, file=file1)

            return
            ''''''

            for num in range(1,20):
                #print("================正在爬虫第"+str(num)+"页数据==================")
                outurl=inurl+str(num)
                req = requests.get(url=outurl)
                req.encoding = "utf-8"
                #html=req.text
                soup = bs4.BeautifulSoup(req.text,features="html.parser")
                #company_item = soup.find("div", class_ = "detail_head")
                company_items = soup.find_all("div",class_="detail_head")
                for company_item in company_items:
                    dd = company_item.text.strip()
                    print(dd)
                    print(dd, file=file1)
    finally:
        pass

#-----------------------------------------------------------------------------------------------------

def runmain2():
    url = "https://mikanani.me/Home/Classic"

    # 网页上 F12 -> Network -> CSS -> F5刷新网页 -> Name选择一个包 -> Headers -> Request Headers -> User-Agent
    #{'键名': '键值'}
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36'}
    html_data = requests.get(url=url, headers=headers).text     #字符串只能正则表达式 或者xpath
    #print(html_data)

    selector = parsel.Selector(html_data)
    MAX_page = selector.xpath('//div[2]/ul/li[14]/@data-lp').get()  #获取最大页数

    print(MAX_page)

    #for x in range(MAX_page):
    for x in range(2):
        page = str(x+1)
        url_one = url+"/"+page

        html_data1 = requests.get(url=url_one, headers=headers).text     #字符串只能正则表达式 或者xpath
        selector1 = parsel.Selector(html_data)
        a_s = selector1.xpath('//tr/td[3]/a[1]/@href').getall()  #获取全部(getall) 根据xpath得到的 列表

        #print(a_s)

        '''
        for a in a_s:


            url_head = "https://mikanani.me"
            all_url = url_head + a

        url
        https://mikanani.me/Home/Classic/1
        '''











    return
    for a in a_s:
        url_head = "https://mikanani.me"
        all_url = url_head + a

        #a_s = selector.xpath('//p[@class="episode-title"]/text()').getall()  #获取全部(getall) 根据xpath得到的 列表
        #print(all_url)

        response2 = requests.get(url=all_url, headers=headers).text
        selector2 = parsel.Selector(response2)

        source_title = selector2.xpath('//p[@class="episode-title"]/text()').get()
        #source_url = selector2.xpath("//div[@class='leftbar-nav']/a[@class='btn episode-btn'][1]/@href").get()
        source_url = selector2.xpath('//div[1]/div[1]/@style').get()
        source_file_name = selector2.xpath('//*[@id="sk-container"]/div[1]/p[1]/a[1]/text()').get()
        
        #print(source_title)
        #print(source_url)

        #11111111111111111111111111
        '''
        source_data = requests.get(url=url_head+source_url, headers=headers).content

        file_name = source_url.split('/')[-1]
        print(file_name)
        with open(file_name, mode='wb') as f:
            f.write(source_data)
        '''

        #2222222222222222222222222222
        '''
        file_url = source_url.split('\'')[1]
        print(file_url)

        if source_file_name == None:
            print()
            continue

        print(source_file_name)
        file_name = source_file_name + file_url.split('/')[-1]
        print(file_name)

        source_jpg_data = requests.get(url=url_head+file_url, headers=headers).content
        with open(file_name, mode='wb') as f:
            f.write(source_jpg_data)

        '''
        #33333333333333333333333333333333

        print()

#-----------------------------------------------------------------------------------------------------

def runmain3():
    #url="https://weibo.com/"
    #url="https://s.weibo.com/top/summary"
    url="https://www.baidu.com"
    url_temp="https://www.baidu.com/s?"

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36'}
    #response = requests.get(url=url, headers=headers)
    
    params = {"wd" : "中文"}

    #esponse = requests.get(url=url, headers=headers ,params=params)
    response = requests.get(url=url_temp, headers=headers ,params=params)
    #response.encoding = 'utf-8'
    #response.encoding = 'gbk'

    if response.status_code != 200:
        print("status_code:"+response.status_code)
        return

    #报错 【'utf-8' codec can't decode byte 0xca in position 339: invalid continuation byte】的话尝试填值'gbk'
    #print(response.content.decode('gbk'))


    #打印相关信息
    #print(response.request.headers)
    print(response.url)
    print(response.request.url)
    #print(response.headers)
    


    #response.content.encode()
    #r.content.encode("gbk")

    html_data = response.text

    
    #print(html_data)
    #print(html.encoding)

    #html_data.encode(html.encoding)
    
    selector = parsel.Selector(html_data)
    a_s = selector.xpath('//tbody/tr/td[2]/a').get()  #获取全部(getall) 根据xpath得到的 列表
    #print(a_s)
    

    #jar.set('tasty_cookie', 'yum', domain='httpbin.org', path='/cookies')
    pass



#-----------------------------------------------------------------------------------------------------
'''
def getall(self) -> List[str]:
    """
    Call the ``.get()`` method for each element is this list and return
    their results flattened, as a list of strings.
    """
    return [x.get() for x in self]
'''


def runmain4():

    list1 =  [x*10 for x in range(10)]
    print(list1)

    pass




#-----------------------------------------------------------------------------------------------------

#class 定义
#Spider = 蜘蛛
#reptile = 爬虫
class Spider:

    def __init__(self, url_name) -> None:
        self.url_name = url_name
        self.url_temp = "https://tieba.baidu.com/f?kw="+url_name+"&ie=utf-8&pn={}"
        self.domain_name = self.get_domain_name(self.url_temp)
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36'}

    #获取域名
    def get_domain_name(self, url):
        if url.startswith('http://'): 
            url = url[7:]
        if url.startswith('https://'): 
            url = url[8:]
        if url.startswith('www.'): 
            url = url[4:]
        #取第一个'/' 前面的字符
        if'/'in url:
            url = url[:url.find('/')] 
        return url
    
    #构建url列表
    def get_url_list(self,number=5):
        # url_list = []
        # for i in range(number):
        #     url_list.append(self.url_temp.format(i*50))
        # return url_list
        return [self.url_temp.format(i*50) for i in range(number)]

    #发送请求 获取响应
    def send_url(self, url):
        print(url)
        response = requests.get(url=url, headers=self.headers)
        return response.content.decode()

    #保存
    def save_html(self, html_str, page_num):
        #判断是否需要创建文件夹
        #self.mkdir(self.url_name)
        self.mkdir(self.domain_name)#用域名创建文件夹

        file_path = "{}/{}-第{}页.html".format(self.domain_name, self.url_name, page_num)
        with open(file_path, mode="w", encoding="utf-8") as f:
            f.write(html_str)

    #创建文件夹
    def mkdir(self, mkdir_path):
        #判断文件夹是否存在

        #如果存在退出 如果不存在创建后退出
        if (os.path.exists(mkdir_path)) == True:
            # 结果 True
            #print("文件夹存在")
            pass
        else:
            print("文件夹不存在,创建[{}]文件夹".format(mkdir_path))
            #os.mkdir(mkdir_path)       #仅创建一级文件夹
            os.makedirs(mkdir_path)     #可创建多级文件夹

    def run(self):
        #print(self.url)
        #print(self.headers)

        url_all_list = self.get_url_list(5)
        for url in url_all_list:
            html_data = self.send_url(url)
            page_num = url_all_list.index(url)+1
            self.save_html(html_data, page_num)

def runmain5():
    Spider_tieba = Spider("贴吧")
    Spider_tieba.run()


#-----------------------------------------------------------------------------------------------------
def runmain6():
    print("\n\n")

    i = 0
    while True:
        start = time.perf_counter()
        runmain6_url_get()
        end = time.perf_counter()
        runTime = end - start
        #runTime_ms = runTime * 1000
        #print("运行时间：", runTime_ms, "毫秒")
        #print("运行时间：" + str(int(runTime_ms)) + "毫秒。")
        #print("等待刷新")
        time.sleep(30)
        
        #https://s.weibo.com/

        """
        start = time.perf_counter()
        while True:
            '''
            i+=1
            if i>=3:
                i=0
            if i==0:
                print("[.  ]",end="")
            if i==1:
                print("[ . ]",end="")
            if i==2:
                print("[  .]",end="")
            '''
            time.sleep(1)
            end = time.perf_counter()
            runTime = end - start
            #print("\b\b\b\b\b",end="")

            if runTime >= 5:
                runTime = 0
                #print(int(runTime))
                break
        """

#-----------------------------------------------------------------------------------------------------
def runmain6_url_get():
    #print("\n\n\n")
    #CMD运行.py sys.argv[0]==文件名 [1]==参数1 以此类推...

    url = "https://s.weibo.com/top/summary"

    headers = {
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "zh-CN,zh;q=0.9",
        "cache-control": "max-age=0",
        "cookie": "SUB=_2AkMU4oQkf8NxqwJRmPAXzW7ibI10zgHEieKivnX_JRMxHRl-yT92qksEtRB6P2Kqy8Y8RaIEnAgGVw3FIuPGpr8_O-Eh; SUBP=0033WrSXqPxfM72-Ws9jqgMF55529P9D9WhkrzNzcFQ8ds6KO695md2-; _s_tentry=passport.weibo.com; Apache=2363573330258.5195.1673399057173; SINAGLOBAL=2363573330258.5195.1673399057173; ULV=1673399057179:1:1:1:2363573330258.5195.1673399057173:",
        #"sec-ch-ua": ""Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99""
        "sec-ch-ua-mobile": "?0",
        "sec-fetch-dest": "document",
        "sec-fetch-mode": "navigate",
        "sec-fetch-site": "none",
        "sec-fetch-user": "?1",
        "upgrade-insecure-requests": "1",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36",
    }

    domain_name = get_domain_name(url)

    response = requests.get(url=url, headers=headers)

    #response.encoding = "utf-8"
    #response.encoding = "gbk"

    #response.content.encode("gbk")
    #response.content.encode("ISO-8859-1")
    #response.content.encode("utf-8")

    #response.encoding = 'gbk'
    #response.encoding = 'ISO-8859-1'
    #response.encoding = 'utf-8'

    #WB_data = response.content.decode()
    #WB_data.content.encode("gbk")

    #print(WB_data)
    #WB_data.

    html_data = response.text
    selector = parsel.Selector(html_data)

    WB_str = selector.xpath('//tr/td/a/text()').getall()  #获取全部(getall) 根据xpath得到的 列表
    WB_num = selector.xpath('//tr/td/span/text()').getall()  #获取全部(getall) 根据xpath得到的 列表
    WB_url = selector.xpath('//tr/td/a/@href').getall()  #获取全部(getall) 根据xpath得到的 列表

    #print(WB_str)
    #print(WB_num)
    #print(WB_url)

    #处理掉数字前面的字符串 剧集 盛典 综艺
    #print("处理掉数字前面的字符串")
    for i in range(len(WB_num)):
        str_temp = WB_num[i].split()
        if len(str_temp) > 1:
            #print(WB_num[i].split())
            WB_num[i] = str_temp[1]
            #print(WB_num[i])

    #去掉数字前面的空格
    for i in range(len(WB_num)):
        WB_num[i] = WB_num[i].strip()

    #把url "%E5%9C%B0%E7%A3%81%E6%9A%B4" 解码为 "地磁暴"
    #print("把url 解码为 字符串")
    for i in range(len(WB_url)):
        #print(WB_url[i])
        WB_url[i] = "https://s.weibo.com" + unquote(WB_url[i])
        WB_url[i] = WB_url[i].replace("#", "")
        #print(WB_url[i])

    
    #长度不一估计是获取的数据出了问题 直接退出
    if not(len(WB_str) == len(WB_url) and len(WB_str) == len(WB_num) + 1):
        #WB_time = 
        print(WB_str)
        print(WB_num)
        print(WB_url)

        print(len(WB_str))
        print(len(WB_num))
        print(len(WB_url))

        print("长度不一")
        return
    
    mkdir(domain_name)
    file_path = domain_name + "/" + domain_name + "全部列表.txt"
    #print(file_path)
    #读取列表
    with open(file_path, mode="w+", encoding="utf-8") as f:
        for i in range(len(WB_str)):
            #第一行是指定 无数字内容
            if i == 0:
                continue
            #print(WB_str[i], WB_num[i-1], WB_url[i])

            #print(WB_str[i])
            #print(WB_num[i-1])
            #print(WB_url[i])
            '''
            #文本在前 数字在后
            str_temp = WB_str[i] + "\t" + \
                        WB_num[i-1] + "\t" + \
                        WB_url[i] + "\n"
            '''
            #数字在前 文本在后
            str_temp = WB_num[i-1] + "\t" + \
                        WB_str[i] + "\t" + \
                        WB_url[i] + "\n"
            
            #print(str_temp)
            f.write(str_temp)

    file_path2 = domain_name + "/" + domain_name + "爆炸列表.txt"
    file_path3 = file_path2 + ".bak"
    file_path4 = file_path2 + ".cp"
    #print(file_path)

    if detection_path(file_path2) == 2:
        with open(file_path2, mode="w", encoding="utf-8") as f2:
            f2.write("")

    with open(file_path , mode="r", encoding="utf-8") as f1:
        for x in f1.readlines():
            line_list = x.split("\t")
            #print(line_list)
            if len(line_list) <= 2:
                continue

            #词条数目 词条名称 词条url
            if is_number(line_list[0]):
                entry_number = line_list[0]
                entry_name = line_list[1]
            #词条名称 词条数目 词条url
            elif is_number(line_list[1]):
                entry_number = line_list[1]
                entry_name = line_list[0]
            else:
                #print("位置错误")
                #print(line_list)
                #entry_number = line_list[0]
                #entry_name = line_list[1]
                pass#忽略

            if is_number(entry_number):
                #if int(entry_number) >= 1000000:   #100万
                #if int(entry_number) >= 100000:    #10万
                if int(entry_number) >= 1000:      #1万
                    #print()
                    #print(time.time())
                    #print(time.strftime('%Y%m%d',time.localtime(time.time())))
                    #print(time.strftime('%Y%m%d%H%M%S',time.localtime(time.time())))
                    Ymd = time.strftime('%Y-%m-%d-%H:%M',time.localtime(time.time()))
                    #print(Ymd)

                    str_flag = 0

                    with open(file_path2, mode="r", encoding="utf-8") as f2,\
                        open(file_path3, mode="w", encoding="utf-8") as f3 :

                        #创建的时间
                        creation_time = 0
                        #更新的时间
                        updated_time = 0
                        #相差的时间 = updated_time - creation_time
                        differ_time = 0

                        #最后出现的时间
                        end_time = 0
                        #存活的时间 = end_time - creation_time
                        survive_time = 0


                        for y in f2.readlines():
                            line_list3 = y.split("\t")
                            #print(line_list3)

                            if is_number(line_list3[1]):
                                old_number = line_list3[1]
                                print("line_list3[1]")
                            elif is_number(line_list3[2]):
                                old_number = line_list3[2]
                                print("line_list3[2]")
                            elif is_number(line_list3[3]):
                                
                                differ_time = 0
                                updated_time = 1
                                creation_time = 2
                                old_number = 3

                            else:
                                print("词条数目位置错误")
                                return

                            if entry_name in y :
                                str_flag = 1

                                #print(entry_name)

                                if int(entry_number) > int(line_list3[old_number]):
                                #if True:
                                    #print(int(entry_number))
                                    #print(int(line_list3[old_number]))

                                    '''
                                    #更新数量
                                    #字符串替换
                                    tempStr = str(y)
                                    tempStr2 = tempStr.replace(line_list3[old_number], entry_number)
                                    y = tempStr2
                                    '''
                                    #更新数量
                                    #列表替换
                                    line_list3[old_number] = int(entry_number)

                                    #计算时间
                                    t1 = datetime.datetime.strptime(line_list3[creation_time],'%Y-%m-%d-%H:%M')
                                    t2 = datetime.datetime.strptime(Ymd,'%Y-%m-%d-%H:%M')
                                    t3 = t2-t1
                                    day = int(t3.days)
                                    hour = int(t3.seconds/60/60%24)
                                    min = int(t3.seconds/60%60)
                                    times_hm = (str(day)+":"+str(hour).zfill(2)+":"+str(min).zfill(2))
                                    #sec = int(t3.seconds)
                                    #print(day, hour, min, sec)

                                    '''
                                    #更新差异时间
                                    #字符串替换
                                    tempStr = str(y)
                                    tempStr2 = tempStr.replace(line_list3[differ_time], times_hm, 1)
                                    y = tempStr2
                                    '''

                                    #更新差异时间
                                    #列表替换
                                    line_list3[differ_time] = times_hm



                                    '''
                                    #更新最新时间
                                    #字符串替换
                                    #tempStr = str(y)
                                    tempStr2 = tempStr.replace(line_list3[updated_time], Ymd, 1)
                                    y = tempStr2
                                    '''
                                    #更新  更新的时间
                                    #列表替换
                                    line_list3[updated_time] = Ymd

                                    y = "\t".join(map(str, line_list3))

                                    print()
                                    print('\033[1;32;40m', end="")
                                    print("更新***", y, end="")
                                    print("\033[0m", end="")
                                
                                if True:    #存活的时间
                                    pass

                                f3.write(y)
                            else:
                                #网页没有文件中的该词条,该行保持不动
                                f3.write(y)

                        if str_flag == 0:
                            #计算时间 新增的词条 差异时间为0
                            t1 = datetime.datetime.strptime(Ymd,'%Y-%m-%d-%H:%M')
                            t2 = datetime.datetime.strptime(Ymd,'%Y-%m-%d-%H:%M')
                            t3 = t2-t1
                            day = int(t3.days)
                            hour = int(t3.seconds/60/60%24)
                            min = int(t3.seconds/60%60)
                            times_hm = (str(day)+":"+str(hour).zfill(2)+":"+str(min).zfill(2))
                            #sec = int(t3.seconds)
                            #print(day, hour, min, sec)

                            #tempStr = Ymd +"\t"+ x
                            #tempStr = Ymd +"\t"+ x.rstrip() + "\t"+ Ymd + "\n"
                            #tempStr = Ymd +"\t"+ Ymd + "\t"+  x
                            #tempStr = times_hm + "\t" + Ymd + "\t" + Ymd + "\t"+  x
                            tempStr = times_hm + "\t" + Ymd + "\t" + times_hm + "\t" + Ymd + "\t" + Ymd + "\t"+  x

                            print()
                            print('\033[1;33;40m', end="")
                            print("+++新增", tempStr, end="") 
                            print("\033[0m", end="")

                            f3.write(tempStr)
                        elif str_flag == 1:
                            #f3.write(str_y)
                            pass

                    #把旧文件删除 重命名新文件
                    #os.remove(file_path3)
                    #os.rename(file_path2, file_path3)
                    
                    shutil.copy2(file_path2, file_path4)  #复制不会覆盖修改时间

                    os.remove(file_path2)
                    os.rename(file_path3, file_path2)

                    #print("热度大于阈值:" , line_list) 
                    #print(line_list)
            else:
                #print("no number:", line_list)
                pass
    pass

#-----------------------------------------
#获取域名
def get_domain_name(url):
    if url.startswith('http://'): 
        url = url[7:]
    if url.startswith('https://'): 
        url = url[8:]
    if url.startswith('www.'): 
        url = url[4:]
    #取第一个'/' 前面的字符
    if'/'in url:
        url = url[:url.find('/')] 
    return url

#-----------------------------------------
#创建文件夹
def mkdir(mkdir_path):
    #判断文件夹是否存在

    #如果存在退出 如果不存在创建后退出
    if (os.path.exists(mkdir_path)) == True:
        # 结果 True
        #print("文件夹存在")
        pass
    else:
        print("文件夹不存在,创建[{}]文件夹".format(mkdir_path))
        #os.mkdir(mkdir_path)       #仅创建一级文件夹
        os.makedirs(mkdir_path)     #可创建多级文件夹
#-----------------------------------------------------------------------------------------------------
#判断字符串能否转换为数字
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass
 
    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass
 
    return False


#-----------------------------------------------------------------------------------------------------

if __name__ == '__main__':
    #开始编写时间 20221205
    

    #资料：https://requests.readthedocs.io/projects/cn/zh_CN/latest/


    # time.clock()默认单位为s
    # 获取开始时间
    #start = time.process_time()
    start = time.perf_counter()

    #打印运行的py文件名称
    print("Run " + os.path.join(os.getcwd(), os.path.basename(__file__)))

    #runmain()#运行主程序
    #runmain2()
    #runmain3()
    #runmain4()
    #runmain5()
    runmain6()

    print("Run End------------------------------")

    #显示运行时间
    while True:
        # 获取结束时间
        #end = time.process_time()
        end = time.perf_counter()
        
        # 计算运行时间
        runTime = (end - start)
        #runTime_ms = runTime * 1000
        # 输出运行时间
        print("运行时间：" + str(int(runTime/60)) + "分" + str(int(runTime%60)) + "秒。")
        #print("运行时间：", runTime_ms, "毫秒")
        #input('输入Enter退出程序。\n\n\n\n\n\n\n')
        print("\n\n\n")
        break









