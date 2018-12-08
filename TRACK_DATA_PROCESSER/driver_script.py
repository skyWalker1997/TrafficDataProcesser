import os
import time

import combine_data, driver_origin_data_flix, splite_data

__ORIGIN_FOLDER__ = '/home/youyizhe/TrafficDataProcesser/test_script/origin/'
__SPLITE_FOLDER__ = '/home/youyizhe/TrafficDataProcesser/test_script/splite/'
__FLIXED_FOLDER__ = '/home/youyizhe/TrafficDataProcesser/test_script/flixed/'
__COMBINE_FOLDER__ = '/home/youyizhe/TrafficDataProcesser/test_script/combine/'

LAX_ROUND = 2

if __name__ == '__main__':
    time_start = time.time()
    for i in range(LAX_ROUND):
        time_start_round = time.time()
        if i == 0:
            print('round:', i, 'is processing......')
            print('Compelte splite data in round:', i)
            driver_origin_data_flix.driver_flix(__SPLITE_FOLDER__, __FLIXED_FOLDER__)
            print('Compelte flix data in round:', i)
            print('Deleting splite data in round:', i)
            os.system("cd /home/youyizhe/TrafficDataProcesser/test_script/splite/;rm *.txt")
            combine_data.combine_data(__FLIXED_FOLDER__, __COMBINE_FOLDER__)
            print('Compelte combine data in round:', i)
            print('Deleting flixed data in round:', i)
            os.system("cd /home/youyizhe/TrafficDataProcesser/test_script/flixed/;rm *.txt")
        else:
            print('round:', i, 'is processing......')
            splite_data.splite_data(__COMBINE_FOLDER__, __SPLITE_FOLDER__)
            print('Compelte splite data in round:', i)
            driver_origin_data_flix.driver_flix(__SPLITE_FOLDER__, __FLIXED_FOLDER__)
            print('Compelte flix data in round:', i)
            print('Deleting splite data in round:', i)
            os.system("cd /home/youyizhe/TrafficDataProcesser/test_script/splite/;rm *.txt")
            combine_data.combine_data(__FLIXED_FOLDER__, __COMBINE_FOLDER__)
            print('Compelte combine data in round:', i)
            print('Deleting flix data in round:', i)
            os.system("cd /home/youyizhe/TrafficDataProcesser/test_script/flixed/;rm *.txt")
        time_end_round = time.time()
        print(i,'round cost time:',time_end_round-time_start_round)
    time_end = time.time()
    print('All cost time:',time_end - time_start)