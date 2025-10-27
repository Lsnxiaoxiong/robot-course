import time
from contextlib import contextmanager



def get_num(a):
    for i in range(a):
        time.sleep(1)
        yield i


if __name__ == "__main__":
    for num in get_num(10):
        print("Number:", num)