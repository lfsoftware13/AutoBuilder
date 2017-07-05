import os
from Builder import build_cpp_file, build_java_file
from Unziper import unzip_cpp_file


root_path = r'C:\Users\Lf\Desktop\root'
code_path = os.path.join(root_path, 'code')
zip_path = os.path.join(root_path, 'zip')
product_path = os.path.join(root_path, 'product')

cpp_record_path = os.path.join(root_path, 'CppRecord.txt')

root_java_path = r'C:\Users\Lf\Desktop\java'
code_java_path = os.path.join(root_java_path, 'code')
product_java_path = os.path.join(root_java_path, 'product')

java_record_path = os.path.join(root_java_path, 'JavaRecord.txt')

qname = 'Q55'


def build_file():
    unzip_cpp_file(zip_path, code_path, cpp_record_path)
    build_cpp_file(code_path, product_path, cpp_record_path)

    build_java_file(code_java_path, product_java_path, java_record_path)

build_file()