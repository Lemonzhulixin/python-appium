#!/usr/bin/python
# -*- coding: UTF-8 -*-
import re
import sys, getopt
import subprocess
import os

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

def getUUID(text):
    uuid = re.findall('<(.*)>', text)[0].upper()
    UUID = uuid[0:8] + '-' + uuid[8:12] + '-' + uuid[12:16] + '-' + uuid[16:20] + "-" + uuid[20:32]
    return UUID


def analyzeCrashLog(inputfile, outputfile):
    crashlog = subprocess.getoutput('grep --after-context=1000 "Binary Images:" ' + inputfile + '  | grep "XiaoYing arm"')
    print(crashlog)
    uuid = getUUID(crashlog)
    print(uuid)
    # ttt = commands.getstatus('sshpass -p ios ssh iOS_Team@10.0.35.21')

    path = subprocess.getoutput('mdfind "com_apple_xcode_dsym_uuids == " ' + uuid)
    # path = path.replace(' ','\\ ')
    path = path + '/dSYMs/XiaoYing.app.dSYM'

    path = "'" + path + "'"
    print(path)
    analysisPath = PATH("../iOSCrashAnalysis/")
    outname = os.path.splitext(inputfile)[0]

    ttt = subprocess.getoutput(
        analysisPath + '/symbolicatecrash ' + inputfile + ' -d ' + path + ' -o ' + outname + '.crash')
    print(ttt)


def main(argv):
    inputfile = ''
    outputfile = ''
    try:
        opts, args = getopt.getopt(argv, "hi:o:", ["ifile=", "ofile="])
    except getopt.GetoptError:
        sys.exit(2)

    for opt, arg in opts:
        if opt == '-h':
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputfile = arg
        elif opt in ("-o", "--ofile"):
            outputfile = arg

    print('输入的文件为：', inputfile)
    print('输出的文件为：', outputfile)
    analyzeCrashLog(inputfile, outputfile)


if __name__ == "__main__":
    main(sys.argv[1:])