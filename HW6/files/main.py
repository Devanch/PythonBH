from pathlib import Path
import os
import logging
import packagePav

logging.basicConfig(filename='logs.log', format='%(asctime)s - %(levelname)s - %(message)s', level=logging.DEBUG)
logging.info('Старт программы')

logging.info('вывести текущую директорию')
logging.info(f'{os.getcwd()} - Текущая деректория')
logging.info(f'{os.listdir("directory/")} - Все папки и файлы')


for filenames in os.listdir('directory/'):
    logging.debug('файл:' + filenames)
    path_elem = filenames.split('-')
    logging.debug(f'{path_elem} элементы пути файла с его именем')

    path_all = "directory/" + path_elem[0] + "/" + path_elem[1]
    logging.debug(f'{path_all} полный путь к файлу')
    logging.info('создание новой папки с проверкой')
    packagePav.create_folder(path_all)

    logging.info(f'{filenames} переименовать в файл с коротким именем')
    packagePav.rename_file(filenames, path_elem[2])
    # os.rename('directory/' + filenames, 'directory/' + path_elem[2])

    logging.info(f'{path_elem[2]} переместить этот файл в новый каталог')
    os.replace("directory/" + path_elem[2], path_all + '/' + path_elem[2])
