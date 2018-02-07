# -*- coding:UTF-8 -*-

#使用说明：
#step1，chmod 777 thisfilename.py
#step2，在terminal下执行 >python thisfilename.py

import os,re;

# str = raw_input('请输入：');
# print 'your input content is ',str


#扫描指定文件的本地化字符串

localizedStrs = [] #存储扫描到的本地化字符串
#扫描源文件的本地化字符串
def scanlocalizestring(path):
    f = open(path);
    str = f.read();  # 读文件 如果没有参数，将尽可能的读取更多
    #print 'read file ', str

    result1 = re.findall(r'NSLocalizedString\(@"(.+?)"', str)  # NSLocalizedString(@"门铃", nil)
    for r in result1:
        if localizedStrs.count(r) == 0:
            localizedStrs.append(r)

     #@"Alarm delay".localizedString
    result1 = re.findall(r'@"(.+?)".localizedString', str)  # NSLocalizedString(@"门铃", nil)
    for r in result1:
        if localizedStrs.count(r) == 0:
            localizedStrs.append(r)

#本地化字符串写入文件
def write2file():
    f = open('Localizable.strings', 'wb');
    for str in localizedStrs:
        localizedStr = '"' + str + '" = "";\n'
        f.write(localizedStr)
    f.close();


#遍历指定目录的.m源文件
allfile = []
def getallfile(path):
    allfilelist = os.listdir(path)
    for file in allfilelist:
        filepath = os.path.join(path, file)
        # 判断是不是文件夹
        if os.path.isdir(filepath):
            getallfile(filepath)

        if os.path.splitext(filepath)[1] == '.m':#只读取.m源文件
            allfile.append(filepath)
    return allfile

#指定需要扫描的工程目录地址
path = '/Users/tans/Documents/git/S1-3G/S1-3G'
allfiles=getallfile(path)
for item in allfiles:
   scanlocalizestring(item)

write2file()