# -*- coding:utf-8 -*- ＃
import requests
import re
import os
import ssl
import random

mwebname = "xinggan" # 特征（类型）
mdirname = "model" # 目录名
page_id_s = 3000 # 起始id
page_id_e = 3016 # 结束id
ssl._create_default_https_context = ssl._create_unverified_context
uapools = ["Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
           "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
           "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
           "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
           "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
           "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
           "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
           "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
           "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
           "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
           "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
           "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5",
           "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6",
           "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
           "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20",
           "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52"]
mheaders = {
              'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
              'Accept-Encoding': 'gzip, deflate',
              'Accept-Language': 'zh-CN,zh;q=0.8',
              'Cache-Control': 'no-cache',
              'Connection': 'keep-alive',
              'Cookie': 'UM_distinctid=15fa02251e679e-05c01fdf7965e7-5848211c-144000-15fa02251e7800; bdshare_firstime=1510220189357; CNZZDATA1263415983=1653134122-1510216223-null%7C1510216223; CNZZDATA3866066=cnzz_eid%3D376479854-1494676185-%26ntime%3D1494676185; Hm_lvt_9a737a8572f89206db6e9c301695b55a=1510220189; Hm_lpvt_9a737a8572f89206db6e9c301695b55a=1510220990',
              'Host': 'img1.mm131.me',
              'Pragma': 'no-cache',
              'Referer': 'http://www.mm131.com/'+mwebname+"/",
              'User-Agent': random.choice(uapools)
          }

if __name__ == "__main__":
  for page_id in range(page_id_s,page_id_e):
    purl ='http://www.mm131.com/'+mwebname+'/'+str(page_id)+'.html'
    print(purl)
    try:
      res = requests.get(purl)
    except requests.exceptions.ConnectionError:
      print('error_0')
    res.encoding = "gb2312"
    if(res.status_code==200):
      mtitle = re.findall(r'<title>(.*?)</title>', res.text)[0].replace('_美女图片 www.mm131.com', '') # 得到文件夹名
      mpath = "保存目录"+mdirname+"/"+mtitle
      if(os.path.exists(mpath)):
        print("已存在"+mtitle+",跳过")
        continue
      os.makedirs(mpath, 0o755)
      print (str(page_id)+"_"+mpath+mtitle+",准备下载...")
      for pic_id in range(1,100000):#单个模特单次拍摄几乎不可能超过10^5张 捕捉到异常即结束
        mfilename = str(pic_id)+'.jpg'
        purl = 'http://img1.mm131.me/pic/' + str(page_id) + '/'+ mfilename
        try:
          res = requests.get(purl, headers=mheaders, timeout=10)
        except requests.exceptions.ConnectionError:
          print('error_1')
        if (res.status_code == 200):
          print ("正在下载_"+mwebname+"_"+str(page_id)+"_" + mfilename + "," + mtitle)
          open(mpath+"/"+mfilename, 'wb').write(res.content)
        else:
          break
    else:
       print (purl + "不存在")