#!/usr/bin/env python

import sys
from os import listdir
from os.path import isfile, join
import dicom
import pylab

str_targetDir 	= sys.argv[1]
fileIndex 		= int(sys.argv[2])

print("The Directory you indicated was: %s" % str_targetDir)
print("The file in that directory that I will read is index: %d" % fileIndex)

l_files = [f for f in listdir(str_targetDir) if isfile(join(str_targetDir, f))]

str_targetFile = l_files[fileIndex]

print("The target DICOM I will load is: %s" % str_targetFile)
str_dicomFile = '%s/%s' % (str_targetDir, str_targetFile)
ds = dicom.read_file(str_dicomFile)

pylab.imshow(ds.pixel_array, cmap=pylab.cm.bone)
pylab.savefig('out.jpg')

htmlPage = """
<!DOCTYPE html>
<html>
<head>
  <title>DICOM MetaData</title>
</head>
<body>

<img src="out.jpg" >


<pre>%s</pre>

</body>
</html>
""" % (ds)

text_file = open("index.html", "w")
text_file.write("%s" % htmlPage)
text_file.close()

print("index.html generated!!")
