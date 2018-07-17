import os

from builder.Builder import build_cpp_file, build_java_file
from builder.Unziper import unzip_cpp_file
from util.constant import root_path, code_path, zip_path, cpp_record_path, product_path, root_java_path, code_java_path, product_java_path, java_record_path, cpp_test_record_path, java_test_result_path, cpp_user_result_path, java_user_result_path



def build_file():
    # unzip_cpp_file(zip_path, code_path, cpp_record_path)
    build_cpp_file(code_path, product_path, cpp_record_path)

    # build_java_file(code_java_path, product_java_path, java_record_path)

build_file()