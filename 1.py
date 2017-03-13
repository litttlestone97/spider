# -*- coding: utf-8-*-
import re
import requests
import math
##过滤HTML中的标签
#将HTML中标签等信息去掉
#@param htmlstr HTML字符串.
def filter_tags(htmlstr):
  #先过滤CDATA
  re_cdata=re.compile('//<!\[CDATA\[[^>]*//\]\]>',re.I) #匹配CDATA
  re_script=re.compile('<\s*script[^>]*>[^<]*<\s*/\s*script\s*>',re.I)#Script
  re_style=re.compile('<\s*style[^>]*>[^<]*<\s*/\s*style\s*>',re.I)#style
  re_br=re.compile('<br\s*?/?>')#处理换行
  re_h=re.compile('</?\w+[^>]*>')#HTML标签
  re_comment=re.compile('<!--[^>]*-->')#HTML注释
  s=re_cdata.sub('',htmlstr)#去掉CDATA
  s=re_script.sub('',s) #去掉SCRIPT
  s=re_style.sub('',s)#去掉style
  s=re_br.sub('\n',s)#将br转换为换行
  s=re_h.sub('',s) #去掉HTML 标签
  s=re_comment.sub('',s)#去掉HTML注释
  #去掉多余的空行
  blank_line=re.compile('\n+')
  s=blank_line.sub('\n',s)
  s=replaceCharEntity(s)#替换实体
  return s
##替换常用HTML字符实体.
#使用正常的字符替换HTML中特殊的字符实体.
#你可以添加新的实体字符到CHAR_ENTITIES中,处理更多HTML字符实体.
#@param htmlstr HTML字符串.
def replaceCharEntity(htmlstr):
  CHAR_ENTITIES={'nbsp':' ','160':' ',
        'lt':'<','60':'<',
        'gt':'>','62':'>',
        'amp':'&','38':'&',
        'quot':'"','34':'"',}
    
  re_charEntity=re.compile(r'&#?(?P<name>\w+);')
  sz=re_charEntity.search(htmlstr)
  while sz:
    entity=sz.group()#entity全称，如>
    key=sz.group('name')#去除&;后entity,如>为gt
    try:
      htmlstr=re_charEntity.sub(CHAR_ENTITIES[key],htmlstr,1)
      sz=re_charEntity.search(htmlstr)
    except KeyError:
      #以空串代替
      htmlstr=re_charEntity.sub('',htmlstr,1)
      sz=re_charEntity.search(htmlstr)
  return htmlstr

def repalce(s,re_exp,repl_string):
  return re_exp.sub(repl_string,s)

if __name__=='__main__':
  #dist_url='http://www.31zzw.com/news/detail-20160914-14792.html'
  #dist_url='http://www.31zzw.com/news/detail-20170311-15226.html?source=1'
  dist_url='http://news.wto168.net/zixun/guowaixinwen/2017/0311/1703748.html'
  headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.118 Safari/537.36'}
  html = requests.get(dist_url,headers = headers)

  #写入文档
  fp = open('news.txt','w',encoding='utf-8')
  fp.write(html.text)
  fp.close()

  a=filter_tags(html.text)
  fp2 = open('news1.txt','w',encoding='utf-8')
  fp2.write(a)
  fp2.close()