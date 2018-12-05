import re
import time
from os import listdir

__DATA_FOLDER__ = '/Users/PINKFLOYD/Desktop/graduatedesign/Data_processer/taxi_data_flixed/T_0425_0101.txt'
__OUT_FOLDER__ = '/Users/PINKFLOYD/Desktop/graduatedesign/Data_processer/taxi_data_final/T_0425_0101_volumn.txt'


def file_path():
    info = listdir(__DATA_FOLDER__)
    filelistlenth = len(info)
    for i in range(filelistlenth):
        """一个文件中的处理过程"""
        day_timeslot_dict = {}
        day_dict_arr = []
        filename = info[i]
        filedomain = filename.split('_')[0] + '_' + filename.split('_')[1] + '_' + filename.split('_')[2]
        print(filedomain)



def read_data_in_line(DATA_PATH):
    data = []
    for line in open(DATA_PATH,'r',encoding='utf-8'): #设置文件对象并读取每一行文件
        data.append(line)               #将每一行文件加入到list中
    return data

def data_resolve(data):
    new_data_arr = []
    for data_in_line in data:
        data_in_line = data_in_line[:-1]
        one_record = re.split(',',data_in_line)
        timeArray = time.localtime(int(one_record[3]))
        otherStyleTime = time.strftime("%Y--%m--%d %H:%M:%S", timeArray)
        one_record[4] = otherStyleTime
        new_data_arr.append(one_record)
    return new_data_arr

def data_count(data_arr):
    driver_arr_final = []
    for one_line in data_arr:
        i  = 1
        temp_dict = {}
        # for

def output_data(driver_dict,OUTPUT_PATH):
    f = open(OUTPUT_PATH, 'w')
    for key in driver_dict.keys():
        for record in driver_dict[key]:
            f.writelines([record[0],',',record[1],',',record[2],',',record[3],',',record[1],',',record[4],',',record[5],',',record[6],',',record[7],',',record[8],',',record[9],',',record[10],'\n'])
    f.close()

if __name__ == '__main__':
    file_path()
    # origin_data = read_data_in_line(__DATA_FOLDER__)
    # new_data_arr = data_resolve(origin_data)
    # driver_dict = data_count(new_data_arr)
    # output_data(driver_dict,__OUT_FOLDER__)
    # for key in driver_dict.keys():
    #     print(driver_dict[key])
