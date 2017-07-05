# -*- coding:gbk -*-
import os
import time

qname = 'Q55'
cpp_builder_file = 'cpp_builder.bat'


def build_cpp_file(src, dst, record_path):
    success_files = []
    failed_files = []

    file_list = os.listdir(src)
    for file_name in file_list:
        file_full_path = os.path.join(src, file_name)
        if os.path.isdir(file_full_path):
            source_path = os.path.join(file_full_path, qname, 'Source Files')
            include_path = os.path.join(file_full_path, qname, 'Header Files')
            dst_path = os.path.join(dst, file_name)
            if not os.path.exists(dst_path):
                os.mkdir(dst_path)
            print('call '+cpp_builder_file+' "'+source_path+'" "'+include_path+'" "'+dst_path+'"')
            res = os.system('call cpp_builder.bat "'+source_path+'" "'+include_path+'" "'+dst_path+'"')
            if res != 0:
                record = open(record_path, 'w+')
                record.write('Error|'+time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))+'|Status:' + str(res) + '|Path:' + file_full_path)
                record.close()

            if not os.path.exists(os.path.join(dst_path, 'Main.exe')):
                failed_files.append(file_name)
            else:
                success_files.append(file_name)
    return (success_files, failed_files)


def build_java_file(src, dst, record_path):
    success_files = []
    failed_files = []

    file_list = os.listdir(src)
    for file_name in file_list:
        file_full_path = os.path.join(src, file_name)
        if os.path.isdir(file_full_path):
            src_path = os.path.join(file_full_path, 'src')
            dst_path = os.path.join(dst, file_name)
            print('javac -d "'+file_full_path+'"')
            res = java_builder(src_path, dst_path)
            if res != 0:
                record = open(record_path, 'w+')
                record.write('Error|' + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())) + '|Status:' + str(res) + '|Path:' + file_full_path)
                record.close()

            if not os.path.exists(os.path.join(dst_path, 'Main.jar')):
                failed_files.append(file_name)
            else:
                success_files.append(file_name)
    return (success_files, failed_files)


def java_builder(src, dst):
    os.chdir(src)

    if not os.path.exists(src):
        return 101
    elif not os.path.exists(os.path.join(src, 'Main.java')):
        return 102

    if not os.path.exists(dst):
        os.mkdir(dst)

    jar_path = os.path.join(dst, "Main.jar")
    result_path = os.path.join(dst, "result.txt")
    res = os.system(r'javac -d . Main.java > "'+result_path+'" 2>&1')
    if res != 0:
        return res

    if not os.path.exists(os.path.join(src, 'Main.class')):
        return 103

    res = os.system(r'jar -cef Main "'+jar_path+'" . > "'+result_path+'" 2>&1')
    return res

