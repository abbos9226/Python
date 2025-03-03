# import threading
# from time import sleep
# # GIL = Global Interpreter Lock

# # How to create threads
# # join threads (wait for thread complition)
# # Deamon thread


# def worker(name):
#     print(f'Thread {name} started\n', end='')
#     sleep(3)
#     print(f'Thread {name} ended\n', end='')

# # How to create threads
# print('Main thread started')

# # worker(1)
# # worker(2)
# # worker(3)


# threads = []
# for i in range(5):
#     thread = threading.Thread(target= worker, args=(i+1,))
#     thread.start()
#     threads.append(thread)


# # for i in threads:
# #     i.join()

# print('All tasks has been successfully completed')



# # print('test', end=' ')
# # print('test')


# n = 10_000

# s = 0
# for i in range(n):
#     for j in range(i):
#         s += j
# print(s)


# 1_000_000


# 1 = 1
# 2 = 3
# ...
# 10 = 45

# ...


# import threading

# sum_overall = 0
# def sum_nums(range_max):
#     global sum_overall
#     sum_overall += sum(range(range_max+1))

# n = 5

# threads = []
# for i in range(n):
#     thread = threading.Thread(target=sum_nums, args=(i, ))
#     threads.append(thread)
#     thread.start()


# for i in threads:
#     i.join()

# print(sum_overall)
# print("Task completed")

# 0 = 0
# 1 = 1
# 2 = 3
# 3 = 6
# 4 = 10





import concurrent.futures
from time import sleep 
import requests as r


def worker(name, num):
    print(f'Thread {name} started\n', end='')
    
    print(f'Thread {name} ended\n', end='')

ls = 

with concurrent.futures.ThreadPoolExecutor(max_workers=5)



