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

def apkUnpack(malware, outDir):
    run = 'apktool d ' + malware + " -o " + outDir
    os.system(run)
    cert(testOutDir)


def cert(outDir):
    list = os.listdir(outDir + "/original/META-INF/")
    for files in list:
        if files.endswith('.RSA'):
            run = "keytool --printcert -file " + outDir + "/original/META-INF/" + files
            os.system(run)
    dex2jar(testMalware,testOutDir)


def dex2jar(malware, outOut):
    run = 'unzip ' + malware + ' -d /tmp/malwareTmp'
    os.system(run)
    run = "d2j-dex2jar.sh /tmp/malwareTmp/classes.dex -o " + outOut + "/SourceCode.jar"
    os.system(run)

    nicePermissions(testOutDir)

def nicePermissions(outDir):

    manifest = outDir + '/AndroidManifest.xml'

    tree = etree.parse(manifest)
    root = tree.getroot()
    permissions = root.findall('uses-permission')

    for i in range(0, len(permissions)):
        print(permissions[i].attrib['{http://schemas.android.com/apk/res/android}name'])

apkUnpack(testMalware,testOutDir)