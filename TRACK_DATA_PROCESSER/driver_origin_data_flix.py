import re
import time
from os import listdir

__DATA_FOLDER__ = '/Users/PINKFLOYD/Desktop/graduatedesign/TrafficDataProcesser/taxi_data_origin/'
__OUT_FOLDER__ = '/Users/PINKFLOYD/Desktop/graduatedesign/TrafficDataProcesser/taxi_data_flixed/'

def file_path(BEFORE_FLIX_PATH,AFTER_FLIX_FOLDER):
    info = listdir(BEFORE_FLIX_PATH)
    print('flix data list:', info)
    filelistlenth = len(info)
    for i in range(filelistlenth):
        filename = info[i]
        origin_data = read_data_in_line(BEFORE_FLIX_PATH+filename)
        driver_dict = data_flix(origin_data)
        output_data(driver_dict, AFTER_FLIX_FOLDER+filename)


def read_data_in_line(DATA_PATH):
        new_data_arr = []
        # i = 0
        for line in open(DATA_PATH,'r',encoding='utf-8'): #设置文件对象并读取每一行文件
            line = line[:-1]
            # print(i,':',line)
            one_record = [re.split(',', line)[0], re.split(',', line)[1], re.split(',', line)[2],
                          re.split(',', line)[3], re.split(',', line)[4]]
            new_data_arr.append(one_record)
            # i = i+1
        return new_data_arr

def data_resolve(data):
    new_data_arr = []
    for data_in_line in data:
        data_in_line = data_in_line[:-1]
        one_record = re.split(',',data_in_line)
        new_data_arr.append(one_record)
    return new_data_arr

def data_flix(data_arr):
    driver_dict = {}
    for one_line in data_arr:
        temp_arr = []
        if one_line[0] in driver_dict.keys():
            temp_arr = driver_dict[one_line[0]]
            if (abs((int(one_line[3]) - int(temp_arr[len(temp_arr)-1][3])))) > 20:
                temp_arr.append(one_line)
                driver_dict[one_line[0]] = temp_arr
        else:
            temp_arr.append(one_line)
            driver_dict[one_line[0]] = temp_arr
    return  driver_dict

def output_data(driver_dict,OUTPUT_PATH):
    f = open(OUTPUT_PATH, 'w')
    for key in driver_dict.keys():
        for record in driver_dict[key]:
            f.writelines([record[0],',',record[1],',',record[2],',',record[3],',',record[4],'\n'])
    f.close()

def driver_flix(BEFORE_FILX_FOLDER,AFTER_FLIX_FOLDER):
    start_time = time.time()
    file_path(BEFORE_FILX_FOLDER,AFTER_FLIX_FOLDER)
    end_time = time.time()
    print('flix cost time:',end_time - start_time)


if __name__ == '__main__':
    driver_flix('/Volumes/Samsung_T5/test2/splite/','/Volumes/Samsung_T5/test2/flixed/')
