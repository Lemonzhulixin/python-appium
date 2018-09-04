import os
import shutil

class FileFilt:
    fileList = [ ]
    counter = 0
    def __init__(self):
        pass
    def FindFile(self, find_str,file_format, path, filtrate=1):
        for s in os.listdir(path):#返回指定目录下的所有文件和目录名
            newDir = os.path.join(path, s) #将多个路径组合后返回，第一个绝对路径之前的参数将被忽略；os.path.join('路径','文件名.txt')
            if os.path.isfile(newDir): #如果path是一个存在的文件，返回True。否则返回False。
                if filtrate:
                    if newDir and (os.path.splitext(newDir)[1] in file_format) \
                            and (find_str in os.path.splitext(newDir)[0]): #os.path.splitext():分离文件名与扩展名
                        self.fileList.append(newDir)
                        self.counter += 1
                else:
                    self.fileList.append(newDir)
                    self.counter += 1

    def MoveFile(self, find_str, file_format, path, newpath, filtrate=1):
        for s in os.listdir(path):  # 返回指定目录下的所有文件和目录名
            newDir = os.path.join(path, s)  # 将多个路径组合后返回，第一个绝对路径之前的参数将被忽略；os.path.join('路径','文件名.txt')
            if os.path.isfile(newDir):  # 如果path是一个存在的文件，返回True。否则返回False。
                if filtrate:
                    if newDir and (os.path.splitext(newDir)[1] in file_format) \
                            and (find_str in os.path.splitext(newDir)[0]):  # os.path.splitext():分离文件名与扩展名
                        self.fileList.append(newDir)
                        self.counter += 1
                        shutil.move(newDir, newpath)
                else:
                    self.fileList.append(newDir)
                    self.counter += 1

    def DelFolder(self, delDir):
        delList = os.listdir(delDir)
        for f in delList:
            filePath = os.path.join(delDir, f)
            if os.path.isfile(filePath):
                os.remove(filePath)
                print(filePath + " was removed!")
            elif os.path.isdir(filePath):
                shutil.rmtree(filePath, True)
            print("Directory: " + filePath + " was removed!")

if __name__ == "__main__":
    pass
    find_str = 'XiaoYing-'
    file_format = '.ips'
    b = FileFilt()
    b.FindFile(find_str,file_format, path="/Users/zhulixin/new")
    for file in b.fileList:
        filepath = os.path.abspath(file) #绝对路径
        print(filepath)