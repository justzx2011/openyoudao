from BeautifulSoup import BeautifulSoup
import StringIO
import pycurl
#html = StringIO.StringIO()
#c = pycurl.Curl()
#muyrl = raw_input('Enter the url:')
#myurl = 'http://' + myurl
#c.setopt(pyurl.URL,myurl)
#c.setopt(pyurl.WRITEFUNCTION,html.write)
#c.setopt(pyurl.FOLLOWLOCATION,1)
#c.setopt(pyurl.MAXREDIRS,5)
#c.setopt(pyurl.CONNECTTOMEOUT,60)
#c.setopt(pyurl.TIMEOUT,300)
#c.setopt(pyurl.USERAGENT,"Mozilla/4.0 (compatible;MSIE 6.0;Windows NT 5.1;SV1;.NET CLR 1.1.4322)")
#c.perform()
#soup = BeautifulSoup(open("index.html"),fromEncoding="gbk")
soup = BeautifulSoup(open("index.html"))
#sousuo=soup.findAll('span',{'class':'s-input-w'})
for i in range(3):
    #title = soup.findAll('div,{'class':'tit'})[i+1].next.next.string
    title = soup.findAll(['title'])
    print title





