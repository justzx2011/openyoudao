from BeautifulSoup import BeautifulSoup
import os
import re
import popen2
soup = BeautifulSoup(open("index.html"))
head = soup.html.head.extract()
result = soup.find('div',{"id":"results"})
sousuo = soup.find('form',{"id":"f"})
sousuo  = str(sousuo).replace("action=\"/search\"","action=\"http://dict.youdao.com/search\"")
os.system("rm  history.html")
fin,fout = popen2.popen2("tee -a history.html")
fout.write("<html>")
fout.write(str(head))
fout.write("<div class=\"c-header\">")
fout.write(str(sousuo))
fout.write("</div>")
fout.write(str(result))
fout.write("</html>")
fout.close()
