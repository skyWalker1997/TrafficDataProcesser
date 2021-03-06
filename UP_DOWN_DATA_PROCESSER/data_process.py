import gc
import re
from TRACK_DATA_PROCESSER import time_format_exchange as tfe
from os import listdir
import numpy as np
__DATA_FOLDER__ = '/Users/PINKFLOYD/Desktop/graduatedesign/TrafficDataProcesser/out_data/'
__OUT_FOLDER__ = '/Users/PINKFLOYD/Desktop/graduatedesign/TrafficDataProcesser/slot_data/'

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
        fileout = filename.split('_')[0]+'_'+filename.split('_')[1]+'_'+filename.split('_')[2].replace('.txt','')+'volume.txt'
        date = filename.split('_')[1]
        data = read_data_in_line(__DATA_FOLDER__+filedomain)
        poi = data_zip(data)
        day_timeslot_dict = data_count(poi,day_timeslot_dict,date)
        day_arr = dict_zip(day_timeslot_dict,day_dict_arr)
        output_data(day_arr,__OUT_FOLDER__+fileout)
        del data,poi,day_arr
        gc.collect()

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
                temp_arr.append({'len':data[7],'u_d':data[8]})
                slot_dict[date + str(HH_sta) + '02'] = temp_arr
            else:
                slot_dict[date + str(HH_sta) + '02'] = temp_arr
                temp_arr.append({'len':data[7],'u_d':data[8]})
                slot_dict[date + str(HH_sta) + '02'] = temp_arr
        else:
            if date + str(HH_sta) + '01' in slot_dict.keys():
                temp_arr = slot_dict[date + str(HH_sta) + '01']
                temp_arr.append({'len':data[7],'u_d':data[8]})
                slot_dict[date + str(HH_sta) + '01'] = temp_arr
            else:
                slot_dict[date + str(HH_sta) + '01'] = temp_arr
                temp_arr.append({'len':data[7],'u_d':data[8]})
                slot_dict[date + str(HH_sta) + '01'] = temp_arr

    temp_arr = []

    if int(HH_end) > 22 or int(HH_end) < 6:
        pass

    else:
        if MM_end / 30 >= 1:
            if date + str(HH_end) + '02' in slot_dict.keys():
                temp_arr = slot_dict[date + str(HH_end) + '02']
                temp_arr.append({'len':data[7],'u_d':data[8]})
                slot_dict[date + str(HH_end) + '02'] = temp_arr
            else:
                slot_dict[date + str(HH_end) + '02'] = temp_arr
                temp_arr.append({'len':data[7],'u_d':data[8]})
                slot_dict[date + str(HH_end) + '02'] = temp_arr
        else:
            if date + str(HH_end) + '01' in slot_dict.keys():
                temp_arr = slot_dict[date + str(HH_end) + '01']
                temp_arr.append({'len':data[7],'u_d':data[8]})
                slot_dict[date + str(HH_end) + '01'] = temp_arr
            else:
                slot_dict[date + str(HH_end) + '01'] = temp_arr
                temp_arr.append({'len':data[7],'u_d':data[8]})
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
        day_dict['volume_count_up'],day_dict['volume_count_down'] = up_down_count(day_timeslot_dict[slot])
        distance_arr = len_arr(day_timeslot_dict[slot])
        len_dict = distance_juge(distance_arr)
        day_dict['len_percent'] = len_dict
        day_dict_arr.append(day_dict)
    return day_dict_arr

def len_arr(day_timeslot_dict):
    distance_arr = []
    for k in day_timeslot_dict:
        distance_arr.append(k['len'])
    return distance_arr

def distance_juge(distance_arr):
    below_5 = 0
    to_10 = 0
    to_15 = 0
    above_15 = 0
    below_5_list = []
    to_10_list = []
    to_15_list = []
    above_15_list = []
    length  = distance_arr.__len__()
    for len in distance_arr:
        if float(len) <= 5:
            below_5 = below_5 + 1
            below_5_list.append(float(len))
        elif float(len) > 5 and float(len) <= 10:
            to_10 = to_10 + 1
            to_10_list.append(float(len))
        elif float(len) > 10 and float(len) <= 15:
            to_15 = to_15 + 1
            to_15_list.append(float(len))
        else:
            above_15 = above_15+1
            above_15_list.append(float(len))
    below_5 = below_5/length
    below_5 = "%.2f%%" % (below_5 * 100)
    if below_5_list.__len__() == 0:
        below_5_mean = 0.00
    else:
        below_5_mean = "%.2f" % np.mean(below_5_list)
    to_10 = to_10 / length
    to_10 = "%.2f%%" % (to_10 * 100)
    if to_10_list.__len__() == 0:
        to_10_mean = 0.00
    else:
        to_10_mean = "%.2f" % np.mean(to_10_list)
    to_15 = to_15 / length
    to_15 = "%.2f%%" % (to_15 * 100)
    if to_15_list.__len__() == 0:
        to_15_mean = 0.00
    else:
        to_15_mean = "%.2f" % np.mean(to_15_list)
    above_15 = above_15 / length
    above_15 = "%.2f%%" % (above_15 * 100)
    if above_15_list.__len__() == 0:
        above_15_mean = 0.00
    else:
        above_15_mean = "%.2f" % np.mean(above_15_list)
    len_dict = {'5':[str(below_5),str(below_5_mean)],'10':[str(to_10),str(to_10_mean)],
                '15':[str(to_15),str(to_15_mean)],'15+':[str(above_15),str(above_15_mean)]}
    return len_dict

def up_down_count(day_timeslot_dict):
    up_count = 0
    down_count = 0
    for k in day_timeslot_dict:
        if k['u_d'] == 'down':
            down_count+=1
        else:
            up_count+=1
    return up_count,down_count

def output_data(day_arr,OUTPUT_PATH):
    f = open(OUTPUT_PATH, 'w')
    for slot in day_arr:
        # len_percent = str(slot['len_percent']).replace('{','').replace('}','').replace(',',';').replace('\'','').replace(' ','')
        f.writelines([str(slot['slot']),',',str(slot['volume_count_up']),',',str(slot['volume_count_down']),',','5:',str(slot['len_percent']['5']).replace('\'','').replace(' ,',','),';','10:',str(slot['len_percent']['10']).replace('\'','').replace(' ,',','),';','15:',str(slot['len_percent']['15']).replace('\'','').replace(' ,',','),';','15+:',str(slot['len_percent']['15+']).replace('\'','').replace(' ,',','),'\n'])
    f.close()

if __name__ == '__main__':
    data = file_path()
