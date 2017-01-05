# -*- coding:utf-8 -*-
import urllib

response=urllib.urlopen("http://132.32.22.9/public/cmschema/index.asp")
print response.read()
