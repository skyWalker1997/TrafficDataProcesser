import sys, os
import time

__DATA_FOLDER__ = '/Volumes/Samsung_T5/test/splite/'
__OUT_FOLDER__ = '/Volumes/Samsung_T5/test/combine/'
def combine_data(DATA_FOLDER,OUT_PATH):
    time_start = time.time()
    info = os.listdir(DATA_FOLDER)
    print('combine data list:',info)
    fo = open(OUT_PATH, 'w')
    for name in info:
        fi = open(DATA_FOLDER+name)
        # print(DATA_FOLDER+name)
        while True:
            s = fi.read(1 * 1024)
            if not s:
                break
            fo.write(s)
        fi.close()
    fo.close()
    time_end = time.time()
    print('combine cost time:',time_end - time_start)


if __name__ == '__main__':
    time_start = time.time()
    combine_data(__DATA_FOLDER__,__OUT_FOLDER__+'big.txt')
    time_end = time.time()
    print(time_end-time_start)