

# tmp map file
import os


def read_project_user_dict():
    map_file = r'C:\Users\Lf\Desktop\file_tmp\project_user.csv'
    map_dict = {}
    with open(map_file, encoding='utf-8') as f:
        lines = f.readlines()
    for l in lines:
        vs = l.split(',')
        (filepath, tempfilename) = os.path.split(vs[0])
        (shotname, extension) = os.path.splitext(tempfilename)
        map_dict[shotname.strip()] = vs[2].strip().replace('"', '')
    return map_dict