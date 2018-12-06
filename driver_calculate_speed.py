import re
import time
from os import listdir
import time_format_exchange as tfe

__DATA_FOLDER__ = '/Users/PINKFLOYD/Desktop/graduatedesign/TrafiicDataProcesser/taxi_data_flixed/'
__OUT_FOLDER__ = '/Users/PINKFLOYD/Desktop/graduatedesign/TrafiicDataProcesser/taxi_data_final/'


def file_path():
    info = listdir(__DATA_FOLDER__)
    filelistlenth = len(info)
    for i in range(filelistlenth):
        """一个文件中的处理过程"""
        day_timeslot_dict = {}
        day_dict_arr = []
        filename = info[i]
        filedomain = filename.split('_')[0] + '_' + filename.split('_')[1] + '_' + filename.split('_')[2].split('.')[0]
        date = filename.split('_')[1]
        data = read_data_in_line(__DATA_FOLDER__+filedomain+'.txt')
        slot_dict = data_count(data,date)
        day_timeslot_dict,time_slot_arr = calculate_speed(slot_dict)
        time_slot_arr.sort()
        output_data(day_timeslot_dict,time_slot_arr,__OUT_FOLDER__+filedomain+'_volumn.txt')



def read_data_in_line(DATA_PATH):
    data = []
    for line in open(DATA_PATH,'r',encoding='utf-8'): #设置文件对象并读取每一行文件
        line = line[:-1]
        timeArray = time.localtime(int(re.split(',', line)[3]))
        otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
        one_record = [re.split(',', line)[0],otherStyleTime,re.split(',', line)[4]]
        data.append(one_record)               #将每一行文件加入到list中
    return data

def data_count(data,date):
    slot_dict = {}
    for one_record in data:
        """每一条记录时间处理"""
        day,time= tfe.date_split(one_record[1])
        HH,MM = tfe.time_split(time)
        slot_dict = time_juge(HH,MM,slot_dict,date,one_record)
    return slot_dict


def time_juge(HH,MM,slot_dict,date,one_record):
    temp_arr = []
    temp_dict = {}
    if int(HH) > 22 or int(HH) < 6:
        pass

    else:
        """判断slot为01或者02"""
        if MM / 30 >= 1:
            if date + str(HH) + '02' in slot_dict.keys():
                temp_dict = slot_dict[date + str(HH) + '02']
                if one_record[0] in temp_dict.keys():
                    temp_arr = temp_dict[one_record[0]]
                    temp_arr.append(one_record[2])
                    temp_dict[one_record[0]] = temp_arr
                    slot_dict[date + str(HH) + '02'] = temp_dict
                else:
                    temp_arr.append(one_record[2])
                    temp_dict[one_record[0]] = temp_arr
                    slot_dict[date + str(HH) + '02']  = temp_dict
            else:
                temp_arr.append(one_record[2])
                temp_dict[one_record[0]] = temp_arr
                slot_dict[date + str(HH) + '02'] = temp_dict
        else:
            if date + str(HH) + '01' in slot_dict.keys():
                temp_dict = slot_dict[date + str(HH) + '01']
                if one_record[0] in temp_dict.keys():
                    temp_arr = temp_dict[one_record[0]]
                    temp_arr.append(one_record[2])
                    temp_dict[one_record[0]] = temp_arr
                    slot_dict[date + str(HH) + '01'] = temp_dict
                else:
                    temp_arr.append(one_record[2])
                    temp_dict[one_record[0]] = temp_arr
                    slot_dict[date + str(HH) + '01']  = temp_dict
            else:
                temp_arr.append(one_record[2])
                temp_dict[one_record[0]] = temp_arr
                slot_dict[date + str(HH) + '01'] = temp_dict
    return slot_dict


def calculate_speed(data_dict):
    final_dict = {}
    time_slot_arr = []
    for key in data_dict.keys():
        time_slot_arr.append(key)
        temp_arr = []
        average_speed_for_one_slot = 0
        temp_dict = data_dict[key]
        final_dict[key] = temp_arr
        temp_arr.append(len(temp_dict.keys()))
        for driver in temp_dict.keys():
            temp_speed = speed_account(temp_dict[driver])
            average_speed_for_one_slot = average_speed_for_one_slot+temp_speed
        average_speed_for_one_slot = average_speed_for_one_slot/temp_arr[0]
        temp_arr.append(average_speed_for_one_slot)
        final_dict[key] = temp_arr
    return final_dict,time_slot_arr

def speed_account(speed_arr):
    len = speed_arr.__len__()
    temp_speed = 0
    for speed in speed_arr:
        temp_speed = temp_speed+float(speed)
    one_driver_speed = temp_speed/len
    return one_driver_speed


def output_data(driver_dict,time_slot_arr,OUTPUT_PATH):
    f = open(OUTPUT_PATH, 'w')
    for slot in time_slot_arr:
        f.writelines([slot,',',str(driver_dict[slot][0]),',',str(driver_dict[slot][1]),'\n'])
    f.close()

if __name__ == '__main__':
    file_path()