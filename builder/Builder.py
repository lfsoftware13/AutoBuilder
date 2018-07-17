# -*- coding:gbk -*-
import os
import time

qname = 'Q143'
cpp_builder_file = 'cpp_builder.bat'


def build_cpp_file(src, dst, record_path):
    success_files = []
    failed_files = []

    if os.path.exists(record_path):
        os.remove(record_path)

    file_list = os.listdir(src)
    for file_name in file_list:
        file_full_path = os.path.join(src, file_name)
        if os.path.isdir(file_full_path):

            # if download zip file from server directly
            q_path = os.path.join(file_full_path, qname)
            if not os.path.exists(q_path):
                print(q_path + ' does not exist.')
                rec = '[Error][' + time.strftime('%Y-%m-%d %H:%M:%S',
                                                 time.localtime(time.time())) + ']' + q_path + ' does not exist.'
                recordLog(record_path, rec)
                continue
            source_path = os.path.join(file_full_path, qname, 'Source Files')
            if not os.path.exists(source_path):
                source_path = os.path.join(file_full_path, qname, '源文件')
            if not os.path.exists(source_path):
                source_path = os.path.join(file_full_path, qname, 'Resource Files')
            include_path = os.path.join(file_full_path, qname, 'Header Files')
            if not os.path.exists(include_path):
                include_path = os.path.join(file_full_path, qname, '头文件')

            # other special
            # source_path = file_full_path
            # include_path = file_full_path

            if (not os.path.exists(source_path)):
                print(source_path+' does not exist.')
                rec = '[Error][' + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())) + ']'+source_path+' does not exist.'
                recordLog(record_path, rec)
            if (not os.path.exists(include_path)):
                print(include_path + ' does not exist.')
                rec = '[Error][' + time.strftime('%Y-%m-%d %H:%M:%S',
                                                 time.localtime(time.time())) + ']' + include_path + ' does not exist.'
                recordLog(record_path, rec)

            dst_path = os.path.join(dst, file_name, qname)
            if not os.path.exists(dst_path):
                os.makedirs(dst_path, exist_ok=True)
            print('call '+cpp_builder_file+' "'+source_path+'" "'+include_path+'" "'+dst_path+'"')
            res = os.system('call cpp_builder.bat "'+source_path+'" "'+include_path+'" "'+dst_path+'"')
            rec = '[Info]['+time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))+']call '+cpp_builder_file+' "'+source_path+'" "'+include_path+'" "'+dst_path+'"'
            recordLog(record_path, rec)
            recordLog(record_path, res)
            if res != 0:
                rec = '[Error]['+time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))+']Status:' + str(res) + '|Path:' + file_full_path
                recordLog(record_path, rec)

            if not os.path.exists(os.path.join(dst_path, 'Main.exe')):
                failed_files.append(file_name)
            else:
                success_files.append(file_name)
    return (success_files, failed_files)


def build_java_file(src, dst, record_path):
    success_files = []
    failed_files = []

    if os.path.exists(record_path):
        os.remove(record_path)

    file_list = os.listdir(src)
    for file_name in file_list:
        file_full_path = os.path.join(src, file_name)
        if os.path.isdir(file_full_path):
            # src_path = os.path.join(file_full_path, 'src')
            src_path = file_full_path
            dst_path = os.path.join(dst, file_name)
            print('javac  -encoding utf8 -d "'+file_full_path+'"')
            rec = '[Info]['+time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))+']'+'javac -d "'+file_full_path+'"'
            recordLog(record_path, rec)
            res = java_builder(src_path, dst_path)
            if res != 0:
                rec = '[Error][' + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())) + ']Status:' + str(res) + '|Path:' + file_full_path
                recordLog(record_path, rec)

            if not os.path.exists(os.path.join(dst_path, 'Main.jar')):
                failed_files.append(file_name)
            else:
                success_files.append(file_name)
    return (success_files, failed_files)


def java_builder(src, dst):

    if not os.path.exists(src):
        print(src+' not exist.')
        return 101
    elif not os.path.exists(os.path.join(src, 'Main.java')):
        return 102

    os.chdir(src)
    if not os.path.exists(dst):
        os.makedirs(dst, exist_ok=True)

    jar_path = os.path.join(dst, "Main.jar")
    result_path = os.path.join(dst, "result.txt")
    res = os.system(r'javac  -d . Main.java > "'+result_path+'" 2>&1')
    if res != 0:
        return res

    if not os.path.exists(os.path.join(src, 'Main.class')):
        return 103

    res = os.system(r'jar -cef Main "'+jar_path+'" . > "'+result_path+'" 2>&1')
    return res


def recordLog(record_path, str1):
    record = open(record_path, 'a')
    if isinstance(str1, int):
        str1 = str(str1)
    record.write(str1)
    record.write('\n')
    record.close()

