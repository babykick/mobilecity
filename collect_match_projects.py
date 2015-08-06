#coding=utf-8
"""
  收集所有参加海选的项目信息
"""
import requests
import lxml.html
import lxml.etree
import pprint

project_url = "http://zzkf.bigcloudsys.cn:8088/welcome/ajax_get/?&csrf_tname=0f3bbabaf48ad97496572d00d57453ae"
s = requests.Session()
s.headers.update({'User-Agent': 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; InfoPath.3; .NET4.0C; .NET4.0E)'})


class Item:
    def __repr__(self):
        return str(dict(self.__dict__.iteritems()))
       
def login():
    s.get("http://zzkf.bigcloudsys.cn:8088/user/login")
    cookies = dict(sign='CFj72NzSIr', csrf_cname='76e61f7e9e1b966f96b753ed5bb87dbe', session_name='20991504217384047261787419691597258114', spksrc_ut='61f06092747ae7f5b477998e7b931a72', session_flag='2', duoshuo_token='eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzaG9ydF9uYW1lIjoiY3JlYXRpdmUiLCJ1c2VyX2tleSI6IjI4NDg1MCIsIm5hbWUiOiIxMzkwNzMwOTIwNiJ9.xlMwz-ZyzdTz2qvHfAGSUCMRUQdGKY5M3TraZNlAL00', sso_token='e694513609d7392922144c753152f02e22175834')
    payload = {
        'ajax':	'2',
        'csrf_tname':	'76e61f7e9e1b966f96b753ed5bb87dbe',
        'loginName':	'13907309206',
        'loginPwd':	'Hacker1218',
    }
    r = s.post('http://zzkf.bigcloudsys.cn:8088/user/loginDo', cookies=cookies, data=payload)
    print r.content
 
def grab_all_project_links():
    numeachpage = 12
    page = 0
    links = []
    while True:
        print 'Scanning page', page + 1
        r = s.get(project_url, params={'start': numeachpage * page + 1
                               }
          )
        content = r.text
        #print content
        doc =lxml.html.fromstring(content)
        elems = doc.xpath("//ul[contains(@class,'project-one')]")
        if elems:
            for elem in elems:
                try:
                    item = Item()
                    item.link = elem.xpath(".//li[1]/a")[0].attrib.get('href').replace(r'\"', "").replace("\\", '')
                    item.title = elem.xpath(".//li[2]/a")[0].text#.replace(r"\r\n", "").strip()
                    item.summary = elem.xpath(".//li[3]/a")[0].text#.replace(r"\r\n", "").strip()
                    item.pubtime = elem.xpath(".//li[5]/a[2]")[0].text.replace(r"\r\n", "").strip()
                    pprint.pprint(item)
                except Exception, e:
                    print e
                
                #print elem.xpath("./li[contains(@class,'project-titile')]/a")[0].attrib.get('title').strip(r'\"')
        else: break
        page += 1
    return links

def process_link(link):
    print link
    
    
if __name__ == '__main__':
    login()
    for link in grab_all_project_links():
        process_link(link)
