__author__ = 'kiarash'

#
#  mian
#
#  Created by kiarash on 9/29/14.
#  Copyright (c) 2014 Kiarash. All rights reserved.



import datetime
from urllib import urlopen, urlretrieve
from xml.dom import minidom
import os


#Variables:
idx = '0' #defines the day of the picture: 0 = today, 1 = yesterday, ... 20.
saveDir = Desktop = os.path.expanduser("~") + '/Desktop/'

usock = urlopen('http://www.bing.com/HPImageArchive.aspx?format=xml&idx=' + idx + '&n=1&mkt=ru-RU') #ru-RU, because they always have 1920x1200 resolution pictures
xmldoc = minidom.parse(usock)
#Parsing the XML File
for element in xmldoc.getElementsByTagName('url'):
    url = 'http://www.bing.com' + element.firstChild.nodeValue

    #Get Current Date as fileName for the downloaded Picture
    now = datetime.datetime.now()
    picPath = saveDir + now.strftime('bing') + '.jpg'

    #Download and Save the Picture
    #Get a higher resolution by replacing the file name
    urlretrieve(url.replace('_1366x768', '_1920x1200'), picPath)
    os.system('osascript << EOF\ntell application "Finder"\nset desktop picture to file "bing.jpg" of desktop\nend tell\nEOF')