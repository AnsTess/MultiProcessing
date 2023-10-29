
import multiprocessing

def task(n=100000):
    while n:
        n -= 1

if __name__  ==  '__main__':

    p1 = multiprocessing.Process(target=task)
    p2 = multiprocessing.Process(target=task)

    p1.start()
    p2.start()

    p1.join()
    p2.join()