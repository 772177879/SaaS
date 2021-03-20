import zipfile
import os
import shutil
from pathlib import Path
import json
import win32api
import win32con


def get_project_path():  # 获取当前项目的路径
    path = os.getcwd()
    loc = path.index('SaaS')
    return path[:loc + 4]


def get_download_path():    # 文件下载地址的储存
    download_path = get_project_path() + '\\Download'
    return download_path


def del_download_file(path=get_download_path()):  # 直接删除该文件夹，然后再去新建该文件夹就行了
    try:
        shutil.rmtree(path)
    except:
        pass
    os.mkdir(path)


def get_video_path():
    video_path = get_project_path() + '\\ResultReport\\video'
    return video_path


def download_file_success(filename):
    boolean = Path(get_download_path() + '\\' + filename)
    return boolean


def un_zip(zip):   # 判断压缩文件里是否有文件
    zip_file = zipfile.ZipFile(get_download_path() + '\\' + zip)
    zip_list = zip_file.namelist()      # 查看zip里的所有文件
    return zip_list


def get_config(config_type):
    all_path = get_project_path() + '/Object/config.json'
    # with open(all_path, 'r') as fp:
    with open(all_path, 'r', encoding='utf-8') as fp:
        config = json.load(fp)
        return config[config_type]


def get_screen_size():
    x = win32api.GetSystemMetrics(win32con.SM_CXSCREEN)  # 获得屏幕分辨率X轴
    y = win32api.GetSystemMetrics(win32con.SM_CYSCREEN)  # 获得屏幕分辨率Y轴
    return x, y
