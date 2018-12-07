import time
from os import listdir

__DATA_FOLDER__ = '/Volumes/Samsung_T5/test/combine/'
__OUT_FOLDER__ = '/Volumes/Samsung_T5/test/'

import io
def splite_data(DATA_PATH,OUT_FOLDER):
  time_start = time.time()
  info = listdir(DATA_PATH)
  print('splite data list:',info)
  DATA_PATH = DATA_PATH+info[0]
  LIMIT = 1000000
  file_count = 0
  url_list = []
  with io.open(DATA_PATH,'r',encoding='utf-8') as f:
    print(file_count)
    for line in f:
      url_list.append(line)
      if len(url_list) < LIMIT:
        continue
      file_name = OUT_FOLDER + str(file_count)+".txt"
      with io.open(file_name,'w',encoding='utf-8') as file:
        for url in url_list[:-1]:
          file.write(url)
        file.write(url_list[-1].strip())
        url_list=[]
        file_count+=1
  if url_list:
    file_name = OUT_FOLDER + str(file_count) + ".txt"
    with io.open(file_name,'w',encoding='utf-8') as file:
      for url in url_list:
        file.write(url)
  time_end = time.time()
  print('splite cost time:', time_end - time_start)

if __name__ == '__main__':
    time_start = time.time()
    splite_data(__DATA_FOLDER__,__OUT_FOLDER__)
    time_end = time.time()
    print(time_end - time_start)