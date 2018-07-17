from map_user_result.combine_user_result import read_project_user_dict
from statistics.Main import create_q_submit_list
from util.constant import combine_score_file, exam_score_file

import csv

q_name_list = ['Q143', 'Q144']
not_max_q_name = ['Q143']


def find_users_by_user_name(users, user_name):
    for usr in users:
        if usr['username'] == user_name:
            return usr
    return None

if __name__ == '__main__':
    q_submit_list = create_q_submit_list(q_name_list)
    map_dict = read_project_user_dict()
    user_result = []

    for q_name in q_name_list:
        projects = q_submit_list[q_name]
        for pro in projects:
            user_name = map_dict.get(pro['name'], pro['name'])
            usr = find_users_by_user_name(user_result, user_name)
            if usr is None:
                usr = {'username':user_name, q_name:0}
                user_result += [usr]
            if pro['score'] > usr.get(q_name, 0):
                usr[q_name] = pro['score']

    if exam_score_file is not None:
        csv_reader = csv.reader(open(exam_score_file, encoding='utf-8'))
        is_f = True
        for row in csv_reader:
            if is_f:
                is_f = False
                continue
            user_name = row[2]
            score = row[1]
            q_name = 'Q'+row[3]
            # tmp filter Q143 problem
            if q_name in not_max_q_name:
                continue
            usr = find_users_by_user_name(user_result, user_name)
            if usr is None:
                usr = {'username': user_name, q_name: 0}
                user_result += [usr]
            usr[q_name] = max(usr.get(q_name, 0), float(score))

    for usr in user_result:
        total_list = [usr.get(q_name, 0) for q_name in q_name_list]
        usr['total'] = sum(total_list)/len(q_name_list)


    with open(combine_score_file, mode='w', encoding='utf-8') as f:
        # def consist_line_fn(x):
        #     line = str(x['username'])+','+','.join([str(usr[q_name]) for q_name in q_name_list]) + ',' + str(usr['total']) + '\n'
        #     return line

        consist_line_fn = lambda x: str(x['username'])+','+','.join([str(x.get(q_name, 0)) for q_name in q_name_list]) + ',' + str(x['total']) + '\n'
        lines = [consist_line_fn(usr) for usr in user_result]
        f.writelines(lines)







