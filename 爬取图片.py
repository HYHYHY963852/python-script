import requests
from lxml import etree
import re
import os
from multiprocessing.dummy import Pool as ThreadPool
 
def gethtml(url,encode): #获取网页源码
    r = requests.get(url)
    r.encoding = encode
    return r.text
 
def filterFName(FName): #文件名过滤特殊字符
    rstr = r"[\/\\\:\*\?\"\<\>\|]"
    new_name = re.sub(rstr, "_", FName)
    return new_name
 
def mkdir(path): #创建文件夹
    path = path.strip()
    isExists = os.path.exists(path)
    if not isExists:
        os.makedirs(path)
 
def geturl(url): #获取网站各个分类链接、分类名称
    html = gethtml(url,'utf-8')
    ehtml = etree.HTML(html)
    nurl = ehtml.xpath('//*[@id="chenxing_menu"]/li/a/@href')
    ntitle = ehtml.xpath('//*[@id="chenxing_menu"]/li/a/text()')
    urldata=[]
    for i in range(1,len(nurl)-1):
        urldata.append(nurl[i]+'|'+ntitle[i])
    return urldata
 
def downPic(url,savepath):  #下载图片
    picname=url.split('/')[-1]
    print('download: ' + url)
    picdata = requests.get(url)
    with open(savepath + picname, 'wb') as file:
        file.write(picdata.content)
 
def getdata(ulist): #根据网站分类链接、名称进一步解析  这段代码是下载图片主体代码
    url = ulist.split('|')[0]
    til = ulist.split('|')[1]
    html = gethtml(url,'utf-8')
    ehtml = etree.HTML(html)
    count = ''.join(ehtml.xpath('//*[@class="more r"]/em/text()'))
    page = int(count) // 20
    if int(count) % 20 > 0 :
        page+=1
    for i in range(1,page+1):#获取各分类下面所有图集链接
        nurl = url+'page/'+str(i)
        html = gethtml(nurl, 'utf-8')
        ehtml = etree.HTML(html)
        lvurl = ehtml.xpath('//*[@class="img"]/@href')
        for j in lvurl:  #获取每个图集页数和链接
            html = gethtml(j, 'utf-8')
            ehtml = etree.HTML(html)
            lvurl = ''.join(ehtml.xpath('//*[@id="imagecx"]/h1/span/text()'))  # 获取图集页数
            title = ''.join(ehtml.xpath('//*[@id="imagecx"]/h1/text()'))  #获取图集名称
            title = title.replace('()','')
            lvurl = lvurl.replace('1/','')
            path = savepath+'\\'+til+'\\'+filterFName(title)+'\\'
            mkdir(path)
            for k in range(1,int(lvurl)):  #获取每个图集页面的图片
                zurl = j.replace('.html','_'+str(k)+'.html')
                html = gethtml(zurl,'urf-8')
                ehtml = etree.HTML(html)
                picurl = ehtml.xpath('//*[@class="image_cx_cont"]/img/@src')
                for l in picurl:
                    downPic(l,path) #下载图片
 
if __name__ == '__main__':
    url = 'http://mzsock.com'
    savepath='D:\谷歌下载'   #保存位置
    urllist=geturl(url)
    pool = ThreadPool(4)
    results = pool.map(getdata, urllist)
    pool.close()
    pool.join()
    print('任务全部完成~！')
