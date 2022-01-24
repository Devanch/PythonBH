import os

def create_folder(str_path: 'имя и путь создаваемой папки'):
    if not os.path.isdir(str_path):
        os.makedirs(str_path)


def rename_file(cur_name: 'текущее имя файла', new_name: 'новое имя файла'):
    os.rename('directory/' + cur_name, 'directory/' + new_name)