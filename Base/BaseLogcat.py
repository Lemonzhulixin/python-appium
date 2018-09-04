# -*- coding: utf-8 -*-
import os

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

class getCrashText:
    def Count_crash(self, path):
        # 分析logcat日志
        count = 0
        count_line = 0
        word_list = ['ANR', 'FATAL']

        with open(path + '/logcat.log', 'rt') as f:
            for line in f:
                count_line += 1
                for word in word_list:
                    if word in line:
                        text = f.readlines(count_line)
                        with open(path + "/crashInfo.txt", "a") as w:
                            w.write('=========================crash=========================\n')
                            w.writelines(text)
                            count += 1
                            w.close()
        f.close()
        return count

if __name__ == '__main__':
    pass
    path = PATH("../Log/CrashInfo/Android/")
    count = getCrashText().Count_crash(path)
    print(count)
