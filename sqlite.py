import sqlite3
import sys
import StringIO
import os
conn = sqlite3.connect('/home/justzx/.local/share/webkit/databases/file__0.localstorage')
c = conn.cursor()
c.execute("select value from ItemTable where key = 'dict' ")
r= c.fetchone()
os.system("/bin/echo -e  \'"+ "".join(str(r[0]).split('\x00')) + "\' >> cache/history.cache")
#output=StringIO.StringIO()
#print >> output,r[0]
#url=""
##print output.getvalue()
##print "SQLite version: %s" % output.getvalue()
##text1=''.join(output)
##print text1
#url="".join("%s" % tup for tup in output.getvalue())
#url=url.strip()
##print url >> cache/history.cache
##os.system("/bin/echo -e  \'"+ url  + "\' >> cache/history.cache")
#oldStdout = sys.stdout
#sys.stdout= open("cache/history.cache", "w+")
#print >> sys.stdout,url.strip()
#output.close()
