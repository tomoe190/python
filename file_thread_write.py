# -*- coding:UTF-8 -*-

# author:tomoe
# contact: test@test.com
# datetime:2023/2/2 11:29
# software: PyCharm

"""
文件说明：
    
"""
import random
import threading
import time

from loggers import log


class DataSource(object):
    def __init__(self, file_name, start_line=0, max_count=None):
        self.file_name = file_name
        self.start_line = start_line
        self.line_index = start_line  # 当前读取位置
        self.max_count = max_count
        self.lock = threading.RLock()  # 同步锁
        self.__data__ = open(self.file_name, 'r', encoding='utf-8')
        for _ in range(self.start_line):
            self.__data__.readline()

    def read_file(self):
        self.lock.acquire()
        try:
            # if self.line_index <
            line = self.__data__.readline()
            if line:
                self.line_index += 1
                return True, line
            else:
                return False, None
        except Exception as e:
            return False, str(e)
        finally:
            self.lock.release()

    def write_file(self, line):
        self.lock.acquire()
        with open('write_data.txt', 'a+', encoding='utf-8') as f:
            f.write(line)
        self.lock.release()

    def process(self):
        count = 0
        start_time = time.time()
        while True:
            status, line = self.read_file()
            if status:
                log.info(f'线程处理数据:' + '\n' + f'{line}')
                self.write_file(line)
                count += 1
            else:
                break
        print(time.time() - start_time)

if __name__ == "__main__":
    datasource = DataSource('read_data.txt')
    # t_num = 5
    # workers = []
    # start_time = time.time()
    # for i in range(t_num):
    #     worker = threading.Thread(target=datasource.process, args=(i,))
    #     worker.start()
    #     workers.append(worker)
    datasource.process()
    # for worker in workers:
    #     worker.join()
    # log.info("总程序执行完毕。")
    # end_time = time.time()
    # res_time = end_time - start_time
    # log.info(res_time)




