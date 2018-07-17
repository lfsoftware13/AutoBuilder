import xlwt
import os


def export_user_data(users, file_path):
    users = sorted(users, key=lambda x: x['name'])
    wbk = xlwt.Workbook()
    sheet = wbk.add_sheet('sheet 1', cell_overwrite_ok=True)
    sheet.write(0, 0, 'name')
    sheet.write(0, 1, 'build')
    sheet.write(0, 2, 'testcases')
    sheet.write(0, 3, 'acs')
    sheet.write(0, 4, 'was')
    sheet.write(0, 5, 'ties')
    sheet.write(0, 6, 'mes')
    sheet.write(0, 7, 'rtes')
    sheet.write(0, 8, 'score')

    for i in range(0, len(users)):
        us = users[i]
        sheet.write(i+1, 0, us['name'])
        sheet.write(i+1, 1, us['build'])
        sheet.write(i+1, 2, convert_to_str(us['testcases']))
        sheet.write(i+1, 3, convert_to_str(us['acs']))
        sheet.write(i+1, 4, convert_to_str(us['was']))
        sheet.write(i+1, 5, convert_to_str(us['ties']))
        sheet.write(i+1, 6, convert_to_str(us['mes']))
        sheet.write(i+1, 7, convert_to_str(us['rtes']))
        sheet.write(i+1, 8, us['score'])

    wbk.save(file_path)


def export_testcase_data(testcases, file_path):

    if not os.path.exists(file_path):
        f = open(file_path,'w')
        f.close()

    wbk = xlwt.Workbook()
    sheet = wbk.add_sheet('sheet 1', cell_overwrite_ok=True)
    sheet.write(0, 0, 'name')
    sheet.write(0, 1, 'time')
    sheet.write(0, 2, 'memory')
    sheet.write(0, 3, 'status')
    sheet.write(0, 4, 'exitcode')
    sheet.write(0, 5, 'result')

    print(len(testcases))

    for i in range(0, len(testcases)):
        ts = testcases[i]
        sheet.write(i+1, 0, ts['name'])
        sheet.write(i+1, 1, ts['time'])
        sheet.write(i+1, 2, ts['memory'])
        sheet.write(i+1, 3, ts['status'])
        sheet.write(i+1, 4, ts['exitcode'])
        sheet.write(i+1, 5, ts['result'])

    wbk.save(file_path)



def convert_to_str(testcases):
    res = ''
    first = 1
    for ts in testcases:
        if first == 0:
            res += ','
        first = 0
        res += ts
    return res
