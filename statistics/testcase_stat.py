from util.constant import std_in_path
import os


def get_testcase_results(records, std_in_path, q_name):
    testcase_path = os.path.join(std_in_path, q_name)
    file_list = os.listdir(testcase_path)
    testcases = {}

    for file_name in file_list:
        (shotname, extension) = os.path.splitext(file_name)
        if(extension == '.in'):
            testcases[shotname] = []

    print(len(records))
    for rec in records:
        if rec['testcase'] not in testcases:
            print('not found testcase', rec)
            continue
        testcase = {}
        testcase['name'] = rec['name']
        testcase['time'] = rec['time']
        testcase['memory'] = rec['memory']
        testcase['status'] = rec['status']
        testcase['exitcode'] = rec['exitcode']
        testcase['result'] = rec['result']
        testcases[rec['testcase']].append(testcase)

    return testcases


def read_testcase(std_in_path, q_name):
    testcase_path = os.path.join(std_in_path, q_name)
    file_list = os.listdir(testcase_path)
    testcases = {}

    for file_name in file_list:
        (shotname, extension) = os.path.splitext(file_name)
        if (extension == '.in'):
            testcases[shotname] = []
    return testcases






