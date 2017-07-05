import zipfile
import os


def unzip_cpp_file(src, dst, record_path):
    file_list = os.listdir(src)
    for file_name in file_list:
        (shotname, extension) = os.path.splitext(file_name)
        if extension == '.zip':
            print("unzip file "+file_name)
            file_full_path = os.path.join(src, file_name)
            file_dst_path = os.path.join(dst, shotname)

            f = zipfile.ZipFile(file_full_path, 'r')
            for fi in f.namelist():
                f.extract(fi, file_dst_path)

