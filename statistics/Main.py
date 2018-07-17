from util.constant import root_path, code_path, zip_path, cpp_record_path, product_path, root_java_path, code_java_path, \
    product_java_path, java_record_path, cpp_test_record_path, java_test_result_path, cpp_user_result_path, \
    java_user_result_path, cpp_xls_path, java_xls_path, std_in_path
import os
from statistics.export_excel import export_user_data, export_testcase_data
from statistics.testcase_stat import get_testcase_results, read_testcase


def read_record(record_path):
    if not os.path.exists(record_path):
        return []

    records = []
    header = {
        0: 'name',
        1: 'testcase',
        2: 'stdIn',
        3: 'stdOut',
        4: 'time',
        5: 'memory',
        6: 'status',
        7: 'exitcode',
        8: 'result',
    }

    rec_file = open(record_path, 'r')
    line = rec_file.readline()
    while line != '':
        line = line.strip()
        vals = line.split(',')
        item = {}
        for i in range(len(vals)):
            item[header[i]] = vals[i]
        records.append(item)
        line = rec_file.readline()

    return records


def get_user_result(records , total_testcase_count, q_namne):
    users = []

    result = {
        '0': 'acs',
        '1': 'was',
        '2': 'ties',
        '3': 'mes',
        '4': 'rtes',
    }

    for rec in records:
        user = find_user(users, rec['name'])
        if user is None:
            user = {}
            user['name'] = rec['name']
            user['records'] = []
            user['testcases'] = []
            user['acs'] = []
            user['was'] = []
            user['ties'] = []
            user['mes'] = []
            user['rtes'] = []
            user['build'] = 1
            user['score'] = 0
            user['q_name'] = q_namne
            users.append(user)

        if not find_testcase_in_user(user, rec['testcase']):
            user['testcases'].append(rec['testcase'])
            user['records'].append(rec)
            user[result[rec['result']]].append(rec['testcase'])
            user['score'] = len(user['acs'])/total_testcase_count

    return users


def extend_user_result(users, code_path, q_name):
    file_list = os.listdir(code_path)

    for file_name in file_list:
        file_full_path = os.path.join(code_path, file_name)
        if os.path.isdir(file_full_path):
            us = find_user(users, file_name)
            if us is None:
                user = {}
                user['name'] = file_name
                user['records'] = []
                user['testcases'] = []
                user['acs'] = []
                user['was'] = []
                user['ties'] = []
                user['mes'] = []
                user['rtes'] = []
                user['build'] = 0
                user['score'] = 0
                user['q_name'] = q_name
                users.append(user)
    return users


def find_testcase_in_user(user, testcase):
    if not testcase:
        return None
    for ts in user['testcases']:
        if ts == testcase:
            return True
    return False

def find_user(users, name):
    if name is None:
        return None
    for us in users:
        if us['name'] == name:
            return us
    return None


def create_q_submit_list(q_list):
    q_user_list = {}
    for q_name in q_list:
        empty_testcase = read_testcase(std_in_path, q_name)
        records = read_record(cpp_test_record_path.replace('<PROBLEM_ID>', q_name))
        users = get_user_result(records, len(empty_testcase), q_name)
        users = extend_user_result(users, code_path, q_name)
        export_user_data(users, cpp_user_result_path.replace('<PROBLEM_ID>', q_name))
        q_user_list[q_name] = users
    return q_user_list

    # testcases = get_testcase_results(records, std_in_path, q_name)
    # for key, value in testcases.items():
    #     export_testcase_data(value, os.path.join(cpp_xls_path, key+'.xls'))

    # records_java = read_record(java_test_result_path)
    # users_java = get_user_result(records_java)
    # users = extend_user_result(users_java, code_java_path)
    # export_user_data(users_java, java_user_result_path)
    #
    # testcases_java = get_testcase_results(records_java)
    # for key, value in testcases_java.items():
    #     export_testcase_data(value, os.path.join(java_xls_path, key+'.xls'))
