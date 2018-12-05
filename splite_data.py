__DATA_FOLDER__ = '/Volumes/SeagateBac/test/taxi_data_origin.txt'
__OUT_FOLDER__ = '/Volumes/SeagateBac/test/'

import io
LIMIT = 10000000
file_count = 0
url_list = []
with io.open(__DATA_FOLDER__,'r',encoding='utf-8') as f:
  for line in f:
    url_list.append(line)
    if len(url_list) < LIMIT:
      continue
    file_name = __OUT_FOLDER__ + str(file_count)+".txt"
    with io.open(file_name,'w',encoding='utf-8') as file:
      for url in url_list[:-1]:
        file.write(url)
      file.write(url_list[-1].strip())
      url_list=[]
      file_count+=1
if url_list:
  file_name = __OUT_FOLDER__ + str(file_count) + ".txt"
  with io.open(file_name,'w',encoding='utf-8') as file:
    for url in url_list:
      file.write(url)
print('done')