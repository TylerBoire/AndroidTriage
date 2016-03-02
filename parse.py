import xml.etree.ElementTree as etree
import re

manifest = '/home/tyler/Desktop/com.exmaple.zolts/AndroidManifest.xml' 


def nicePermissions():

	tree = etree.parse(manifest)
	root = tree.getroot()
	permissions = root.findall('uses-permission')

	i = 0
	for test in permissions:
		stepOne = (permissions[i].attrib['{http://schemas.android.com/apk/res/android}name'])
		i = i + 1
		print(stepOne)

#def niceActivities():


print('Here are the permissions used:')
nicePermissions()
