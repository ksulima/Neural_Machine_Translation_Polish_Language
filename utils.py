
from contextlib import contextmanager
import time


@contextmanager
def elapsed_time():
    start_time = time.time()
    yield
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f'Time took: {elapsed_time}')
