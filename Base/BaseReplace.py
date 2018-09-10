#!/usr/bin/python
# coding:utf-8
import os
from Base.BaseYaml import getYam


PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

def ReplaceYaml(yaml, newyaml, el_lists):
    el_lists= getYam(el_lists)
    resource = getYam(yaml)
    tc_list = resource[1]['testcase']
    tc_check = resource[1]['check']
    tc_key = []
    check_key = []
    tc_type_key =[]
    check_type_key = []

    for item in tc_list:
        if '$' in item['element_info']:
            tc_key.append(item['element_info'])

        if '$' in item['find_type']:
            tc_type_key.append(item['find_type'])

    for item in tc_check:
        if '$' in item['element_info']:
            check_key.append(item['element_info'])

        if '$' in item['find_type']:
            check_type_key.append(item['find_type'])

    with open(yaml, 'r', encoding='utf-8') as yml_file:
        with open(newyaml, 'wt') as yml_output:
            yml_file_lines = yml_file.readlines()
            for line in yml_file_lines:
                if '$' in line:
                    new_line = line
                    for tc_el_info in tc_key:
                        if tc_el_info in new_line:
                            replacement = ""
                            if tc_el_info in el_lists[1].keys():
                                replacement = el_lists[1][tc_el_info]
                            new_line = new_line.replace(tc_el_info, replacement)
                            yml_output.write(new_line)

                    for tc_type_info in tc_type_key:
                        if tc_type_info in new_line:
                            replacement = ""
                            if tc_type_info in el_lists[1].keys():
                                replacement = el_lists[1][tc_type_info]
                            new_line = new_line.replace(tc_type_info, replacement)
                            yml_output.write(new_line)

                    for check_el_info in check_key:
                        if check_el_info in new_line:
                            replacement = ""
                            if check_el_info in el_lists[1].keys():
                                replacement = el_lists[1][check_el_info]
                            new_line = new_line.replace(check_el_info, replacement)
                            yml_output.write(new_line)

                    for check_type_info in check_type_key:
                        if check_type_info in new_line:
                            replacement = ""
                            if check_type_info in el_lists[1].keys():
                                replacement = el_lists[1][check_type_info]
                            new_line = new_line.replace(check_type_info, replacement)
                            yml_output.write(new_line)
                else:
                    yml_output.write(line)

    yml_file.close()
    yml_output.close()


if __name__ == "__main__":
    yaml = PATH("../yamls/home/secondOpen.yaml")
    newyaml = PATH("../yamls/home/new.yaml")
    el_lists = PATH("../yamls/el_android.yaml")

    ReplaceYaml(yaml, newyaml, el_lists)

