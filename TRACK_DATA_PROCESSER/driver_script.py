import os
import time

from TRACK_DATA_PROCESSER import combine_data, driver_origin_data_flix, splite_data

__ORIGIN_FOLDER__ = '/Volumes/Samsung_T5/test/origin/'
__SPLITE_FOLDER__ = '/Volumes/Samsung_T5/test/splite/'
__FLIXED_FOLDER__ = '/Volumes/Samsung_T5/test/flix/'
__COMBINE_FOLDER__ = '/Volumes/Samsung_T5/test/combine/'

LAX_ROUND = 2

if __name__ == '__main__':
    time_start = time.time()
    for i in range(LAX_ROUND):
        time_start_round = time.time()
        if i == 0:
            splite_data.splite_data(__ORIGIN_FOLDER__, __SPLITE_FOLDER__)
            os.system("cd /Volumes/Samsung_T5/test/splite/;find . -name '*.DS_Store' -type f -delete")
            driver_origin_data_flix.driver_flix(__SPLITE_FOLDER__, __FLIXED_FOLDER__)
            os.system("cd /Volumes/Samsung_T5/test/flixed/;find . -name '*.DS_Store' -type f -delete")
            combine_data.combine_data(__FLIXED_FOLDER__, __COMBINE_FOLDER__)
            os.system("cd /Volumes/Samsung_T5/test/combine/;find . -name '*.DS_Store' -type f -delete")
        else:
            splite_data.splite_data(__COMBINE_FOLDER__, __SPLITE_FOLDER__)
            os.system("cd /Volumes/Samsung_T5/test/splite/;find . -name '*.DS_Store' -type f -delete")
            driver_origin_data_flix.driver_flix(__SPLITE_FOLDER__, __FLIXED_FOLDER__)
            os.system("cd /Volumes/Samsung_T5/test/flixed/;find . -name '*.DS_Store' -type f -delete")
            combine_data.combine_data(__FLIXED_FOLDER__, __COMBINE_FOLDER__)
            os.system("cd /Volumes/Samsung_T5/test/combine/;find . -name '*.DS_Store' -type f -delete")
        time_end_round = time.time()
        print(i,'round cost time:',time_end_round-time_start_round)
    time_end = time.time()
    print('All cost time:',time_end - time_start)