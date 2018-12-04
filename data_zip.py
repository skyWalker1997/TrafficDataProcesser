import re
import os
from os import listdir
from geopy.distance import geodesic
__DATA_FOLDER__ = '/Users/PINKFLOYD/Desktop/graduatedesign/data/data/'
__OUT_FOLDER__ = '/Users/PINKFLOYD/Desktop/graduatedesign/data/out_data/'

def file_path():
    """处理每天和每个时段的上下车文件"""
    file = []
    info = listdir(__DATA_FOLDER__)
    filelistlenth = len(info)
    for i in range(filelistlenth):
        filename = info[i]
        filedomain = filename.split('_')[0]+'_'+filename.split('_')[1]+'_'+filename.split('_')[2]+'.txt'
        file_up = filename.split('_')[0]+'_'+filename.split('_')[1]+'_'+filename.split('_')[2]+'_up.txt'
        file_down = filename.split('_')[0]+'_'+filename.split('_')[1]+'_'+filename.split('_')[2]+'_down.txt'
        file_zip(file_up,file_down,filedomain)

def file_zip(PATH_UP,PATH_DOWN,filedomain):
    data_up = read_data_in_line(__DATA_FOLDER__+PATH_UP)
    data_down = read_data_in_line(__DATA_FOLDER__+PATH_DOWN)
    if os.path.exists(__OUT_FOLDER__+filedomain):
        pass
    else:
        poi_up = data_zip(data_up,0)
        poi_down = data_zip(data_down,1)
        poi = poi_up+poi_down
        fileabsurl = __OUT_FOLDER__+filedomain
        output_file(poi,fileabsurl)

def read_data_in_line(DATA_PATH):
    data = []
    for line in open(DATA_PATH,'r',encoding='utf-8'): #设置文件对象并读取每一行文件
        data.append(line)               #将每一行文件加入到list中
    return data

def data_zip(data,upordown):
    poi = []
    for data_in_line in data:
        data_in_line = data_in_line[:-1]
        data_in_line = re.split('\t',data_in_line)
        i = 1
        temp_dict = {}
        for temp_data in data_in_line:
            if i != 5 and i!= 6:
                temp_dict[i] = temp_data
                i = i+1
            else:
                i = i+1

        len = ("%.5f" % len_calculate(temp_dict))
        temp_dict['len'] = str(len)
        if upordown == 0:
            temp_dict['upordown'] = 'up'
        else:
            temp_dict['upordown'] = 'down'
        poi.append(temp_dict)
    # print(poi)
    return poi

def print_data(data):
    for data_in_line in data:
        data_in_line = data_in_line[:-1]
        data_in_line = re.split('	',data_in_line)
        i = 0
        for data_column in data_in_line:
            print(i,data_column)
            i = i+1
        print("################")

def len_calculate(temp_dict):
    # print(temp_dict)
    gps_start = re.split(',',temp_dict[3])
    gps_end = re.split(',',temp_dict[4])
    lon1 = gps_start[0]
    lat1 = gps_start[1]
    lon2 = gps_end[0]
    lat2 = gps_end[1]
    len = geodesic((lat1,lon1), (lat2,lon2)).km
    return len

def output_file(poi,OUTPUT_PATH):
    f = open(OUTPUT_PATH, 'w')
    print(poi)
    for data in poi:
        f.writelines([data[1],'\t',data[2],'\t',data[3],'\t',data[4],'\t',data[7],'\t',data[8],'\t',data['len'],'\t',data['upordown']+'\n'])
    f.close()
if __name__ == '__main__':
    file_path()