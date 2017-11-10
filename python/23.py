import re
y = 'localpath C:\code\cnkiCrawl'
a = re.findall('(C.*)',y)
print(a)


