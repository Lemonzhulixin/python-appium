# -*- coding: utf-8 -*-
"""主脚本运行测试用例"""
import pytest
from Android.script_ultils import path_lists


def test_start():
    """启动测试."""
    report_para_list = ['--html=', path_lists[2], 'report.html']
    report_para = ''.join(report_para_list)
    case_path = 'Android/VivaVideo/'
    test_args = ['-s', '-q', case_path, report_para, '--self-contained-html']

    pytest.main(test_args)


if __name__ == '__main__':
    test_start()
