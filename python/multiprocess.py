from multiprocessing import Pool, cpu_count
import time

def t():
    # Make a dummy dictionary
    d = {k: k**2 for k in range(10)}

    print(cpu_count())

    pool = Pool(processes=(cpu_count() - 1))

    for key, value in d.items():
        pool.apply_async(thread_process, args=(key, value))

    pool.close()
    pool.join()


def thread_process(key, value):
    time.sleep(5)  # Simulate a process taking some time to complete
    print("For", key, value)

if __name__ == '__main__':
    t()