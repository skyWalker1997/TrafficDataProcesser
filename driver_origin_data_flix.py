import re
__DATA_FOLDER__ = '/Users/PINKFLOYD/Desktop/graduatedesign/Data_processer/taxi_data_origin/taxi_data_origin.txt'
__OUT_FOLDER__ = '/Users/PINKFLOYD/Desktop/graduatedesign/Data_processer/taxi_data_flixed/taxi_data_flixed.txt'

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
        new_data_arr.append(one_record)
    return new_data_arr

def data_flix(data_arr):
    driver_dict = {}
    for one_line in data_arr:
        temp_arr = []
        if one_line[0] in driver_dict.keys():
            temp_arr = driver_dict[one_line[0]]
            # for i in range(len(temp_arr)):
            #     if i == 0:
            #         if one_line[3] - temp_arr[i][3] >
            #     if one_line[3] - temp_arr[][3] > 20
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
            f.writelines([record[0],',',record[1],',',record[2],',',record[3],',',record[1],',',record[4],',',record[5],',',record[6],',',record[7],',',record[8],',',record[9],',',record[10],'\n'])
    f.close()

if __name__ == '__main__':
    origin_data = read_data_in_line(__DATA_FOLDER__)
    new_data_arr = data_resolve(origin_data)
    driver_dict = data_flix(new_data_arr)
    output_data(driver_dict,__OUT_FOLDER__)
    # for key in driver_dict.keys():
    #     print(driver_dict[key])
