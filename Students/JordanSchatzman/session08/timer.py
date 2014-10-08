
import time


class Timer(object):
    """Print the time taken run the code inside the context manager."""
    def __init__(self):
        self.timer = time.time()
        
    def __enter__(self):
        self.start = self.timer
        return self
    
    def __exit__(self, *args):
        self.elapsed = time.time() - self.start
        print u'It took {} seconds to run this code'.format(self.elapsed)


if __name__ == "__main__":
    with Timer() as t:
        for i in range(9999):
            i = i * 23