import re
import os
import time_format_exchange as tfe
from os import listdir
__DATA_FOLDER__ = '/Users/PINKFLOYD/Desktop/graduatedesign/Data_processer/out_data/'
__OUT_FOLDER__ = '/Users/PINKFLOYD/Desktop/graduatedesign/Data_processer/slot_data/'

def file_path():
    """处理每天和每个时段的上下车文件"""
    file = []
    info = listdir(__DATA_FOLDER__)
    filelistlenth = len(info)
    for i in range(filelistlenth):
        """一个文件中的处理过程"""
        day_timeslot_dict = {}
        day_dict_arr = []
        filename = info[i]
        filedomain = filename.split('_')[0]+'_'+filename.split('_')[1]+'_'+filename.split('_')[2]
        fileout = filename.split('_')[0]+'_'+filename.split('_')[1]+'_0101_volume.txt'
        date = filename.split('_')[1]
        data = read_data_in_line(__DATA_FOLDER__+filedomain)
        poi = data_zip(data)
        day_timeslot_dict = data_count(poi,day_timeslot_dict,date)
        day_arr = dict_zip(day_timeslot_dict,day_dict_arr)
        output_data(day_arr,__OUT_FOLDER__+fileout)
        # for slot in day_arr:
        #     print(slot)
        # slot_arr.sort()
        # print(slot_arr)
def read_data_in_line(DATA_PATH):
    data = []
    for line in open(DATA_PATH,'r',encoding='utf-8'): #设置文件对象并读取每一行文件
        data.append(line)               #将每一行文件加入到list中
    return data

def data_zip(data):
    poi = []
    for data_in_line in data:
        data_in_line = data_in_line[:-1]
        data_in_line = re.split('\t',data_in_line)
        i = 1
        temp_dict = {}
        for temp_data in data_in_line:
            temp_dict[i] = temp_data
            i = i +1
        poi.append(temp_dict)
    return poi

def data_count(poi,slot_dict,date):
    for data in poi:
        """每一条记录时间处理"""
        day_sta,time_sta = tfe.date_split(data[5])
        day_end,time_end = tfe.date_split(data[6])
        HH_sta,MM_sta = tfe.time_split(time_sta)
        HH_end,MM_end = tfe.time_split(time_end)
        slot_dict = time_juge(HH_sta,HH_end,MM_sta,MM_end,slot_dict,date,data)
    return slot_dict

def time_juge(HH_sta,HH_end,MM_sta,MM_end,slot_dict,date,data):
    temp_arr = []
    if int(HH_sta) > 22 or int(HH_sta) < 6:
        pass

    else:
        """判断slot为01或者02"""
        if MM_sta / 30 >= 1:
            if date + str(HH_sta) + '02' in slot_dict.keys():
                temp_arr = slot_dict[date + str(HH_sta) + '02']
                temp_arr.append(data[7])
                slot_dict[date + str(HH_sta) + '02'] = temp_arr
            else:
                slot_dict[date + str(HH_sta) + '02'] = temp_arr
                temp_arr.append(data[7])
                slot_dict[date + str(HH_sta) + '02'] = temp_arr
        else:
            if date + str(HH_sta) + '01' in slot_dict.keys():
                temp_arr = slot_dict[date + str(HH_sta) + '01']
                temp_arr.append(data[7])
                slot_dict[date + str(HH_sta) + '01'] = temp_arr
            else:
                slot_dict[date + str(HH_sta) + '01'] = temp_arr
                temp_arr.append(data[7])
                slot_dict[date + str(HH_sta) + '01'] = temp_arr

    temp_arr = []

    if int(HH_end) > 22 or int(HH_end) < 6:
        pass

    else:
        if MM_end / 30 >= 1:
            if date + str(HH_end) + '02' in slot_dict.keys():
                temp_arr = slot_dict[date + str(HH_end) + '02']
                temp_arr.append(data[7])
                slot_dict[date + str(HH_end) + '02'] = temp_arr
            else:
                slot_dict[date + str(HH_end) + '02'] = temp_arr
                temp_arr.append(data[7])
                slot_dict[date + str(HH_end) + '02'] = temp_arr
        else:
            if date + str(HH_end) + '01' in slot_dict.keys():
                temp_arr = slot_dict[date + str(HH_end) + '01']
                temp_arr.append(data[7])
                slot_dict[date + str(HH_end) + '01'] = temp_arr
            else:
                slot_dict[date + str(HH_end) + '01'] = temp_arr
                temp_arr.append(data[7])
                slot_dict[date + str(HH_end) + '01'] = temp_arr

    return slot_dict

def dict_zip(day_timeslot_dict,day_dict_arr):
    slot_arr = []
    for slot in day_timeslot_dict.keys():
        slot_arr.append(slot)
    slot_arr.sort()

    for slot in slot_arr:
        day_dict = {}
        day_dict['slot'] = slot
        day_dict['volume_count'] = len(day_timeslot_dict[slot])
        len_dict = distance_juge(day_timeslot_dict[slot])
        day_dict['len_percent'] = len_dict
        day_dict_arr.append(day_dict)
    return day_dict_arr

def distance_juge(distance_arr):
    below_5 = 0
    to_10 = 0
    to_15 = 0
    above_15 = 0
    length  = distance_arr.__len__()
    for len in distance_arr:
        if float(len) <= 5:
            below_5 = below_5 + 1
        elif float(len) > 5 and float(len) <= 10:
            to_10 = to_10 + 1
        elif float(len) > 10 and float(len) <= 15:
            to_15 = to_15 + 1
        else:
            above_15 = above_15+1
    below_5 = below_5/length
    below_5 = "%.2f%%" % (below_5 * 100)
    to_10 = to_10 / length
    to_10 = "%.2f%%" % (to_10 * 100)
    to_15 = to_15 / length
    to_15 = "%.2f%%" % (to_15 * 100)
    above_15 = above_15 / length
    above_15 = "%.2f%%" % (above_15 * 100)
    len_dict = {'5':str(below_5)+'%','10':str(to_10)+'%',
                '15':str(to_15)+'%','15+':str(above_15)+'%'}
    return len_dict

def output_data(day_arr,OUTPUT_PATH):
    f = open(OUTPUT_PATH, 'w')
    for slot in day_arr:
        len_percent = str(slot['len_percent']).replace('{','').replace('}','').replace(',',';').replace('\'','')
        f.writelines([str(slot['slot']),',',str(slot['volume_count']),',',len_percent,'\n'])
    #     for slot_data in day_arr:
    #         if slot_data
    #         f.writelines(
    #             [slot,day_arr[]])
    # f.close()

if __name__ == '__main__':
    data = file_path()