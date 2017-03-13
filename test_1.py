import requests
import math
import re      #正则表达式的库


dist_url='http://www.31zzw.com/news/detail-20160914-14792.html'
#dist_url='http://news.sohu.com/20131229/n392604462.shtml'
#hea是我们自己构造的一个字典，里面保存了user-agent
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.118 Safari/537.36'}
html = requests.get(dist_url,headers = headers)

#写入文档
fp = open('news.txt','w',encoding='utf-8')
fp.write(html.text)
fp.close()

all_title=('DIV','FORM','img','body','iframe','head','html','title','div','p','strong','span','lable','button','input','a','li','meta','link','em','style','!','base','ul','h1','h2','h3','h4','h5','h6','h7')
#all_title=('div','p','!','li','meta','link','script','style','!','base','ul')
#all_title=('title','p','!')
a=html.text

#去掉标签
'''
#不带属性
for i in all_title:
	#j=re.compile(r'</?%s>'%i)
	#a=j.sub('',a)
	j=re.compile(r'<(.*)?>')
	a=j.sub('',a)
'''
j=re.compile(r'</?\w+[^>]*>',re.S)
a=j.sub('',a)

'''
#带属性
for i in all_title:
	j=re.compile(r'<%s(.*)/?>'%i)
	#print('<"%s"(.*)>'%i)
	a=j.sub('',a)

#javascript
#去掉标签内的内容
j=re.compile(r'<\s*script[^>]*>[^<]*<\s*/\s*script\s*>',re.S)
a=j.sub('',a)

\t|\r|\n
'''
'''
#去掉换行
j=re.compile(r'&(.*)?;')
a=j.sub('',a)
'''
fp2 = open('news1.txt','w',encoding='utf-8')

fp2.write(a)
fp2.close()












