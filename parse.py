import xml.etree.ElementTree as etree
from optparse import OptionParser
import os

'''
parser = OptionParser()

parser.add_option("-a","--apk", action="store", dest="malware", help="Used to specify Malware sample")
parser.add_option("-o", "--output", action="store", dest="outDir", help="Where would you like the output stored?")

(options, args) = parser.parse_args()
'''

testOutDir = "/home/tyler/testing"
testMalware = '/home/tyler/Downloads/malware'

def apk_unpack(malware, outDir):
    run = 'apktool d ' + malware + ' -o ' + outDir
    os.system(run)
    
def cert(outDir):
    meta_files = os.listdir(outDir + '/original/META-INF/')
    for meta_file in meta_files:
        if meta_file.endswith('.RSA'):
            run = 'keytool --printcert -file ' + outDir + '/original/META-INF/' + files
            os.system(run)

def dex2jar(malware, outOut):
    run = 'unzip ' + malware + ' -d /tmp/malwareTmp'
    os.system(run)
    run = 'd2j-dex2jar.sh /tmp/malwareTmp/classes.dex -o ' + outOut + '/SourceCode.jar'
    os.system(run)

def nice_permissions(outDir):

    manifest = outDir + '/AndroidManifest.xml'

    tree = etree.parse(manifest)
    root = tree.getroot()
    permissions = root.findall('uses-permission')

    for i in range(0, len(permissions)):
        print(permissions[i].attrib['{http://schemas.android.com/apk/res/android}name'])

if __name__ = '__main__':
	apk_unpack(testMalware,testOutDir)
	cert(testOutDir)
	dex2jar(testMalware, testOutDir)
	nice_permissions(testOutDir)
