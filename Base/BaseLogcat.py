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

        with open(path + '/logcat.log', 'rt', encoding="ISO-8859-1") as f:
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

# import os
# import re
#
# if __name__ == '__main__':
#     monkey_log_list = [log for log in os.listdir('./monkeylogs') if log.endswith('.log')]
#     devices_log_list = [log for log in os.listdir('./devicelogs') if log.endswith('.log')]
#     word_list = ['ANR', 'FATAL']
#     bug_count = 0
#     line_count = 0
#     flag = 0
#
#     for log in devices_log_list:
#         with open('./devicelogs/' + log, 'rt', encoding="ISO-8859-1") as f:
#             for line in f:
#                 line_count += 1
#                 temp = re.match(r'\w.(.\d*).', line)
#                 if flag > 0:
#                     if temp is None:
#                         flag -= 1
#                     elif pid != temp.group(1):
#                         flag -= 1
#                     else:
#                         flag = 5
#                     with open("crashInfo.txt", "a") as w:
#                         w.write(line)
#                         w.close()
#                     continue
#                 for word in word_list:
#                     if word in line:
#                         pid = re.match(r'\w.(.\d*).', line).group(1)
#                         with open("crashInfo.txt", "a") as w:
#                             w.write('\n=========================crash for {0} {1} {2}=========================\n'
#                                     .format(log, line_count, word))
#                             w.write(line)
#                             flag = 5
#                             bug_count += 1
#                             w.close()
#             line_count = 0
#
#     with open("\n\ncrashInfo.txt\n\n", "a") as w:
#         w.write('Total bugs: {0}'.format(bug_count))
#         w.close()
