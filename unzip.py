'''from zipfile import *
f = ZipFile('compressed.zip', 'w', ZIP_DEFLATED)
f.write('F:/Avd/Python/programs/myfile.txt')'''

#Unzip

from zipfile import *
f = ZipFile('"F:\Avd\Python\Pythonproject\compressed.zip"','r')
f.extract('myfile.txt', 'F:\Avd\Python\Pythonproject\compressed.unzipped')
