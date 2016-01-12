# encoding=utf8

# standard libs
import os
import time
import random
from multiprocessing import Process, Pool, Queue


def test1():
    print "Process %s start ..." % os.getpid()
    pid = os.fork()
    if pid == 0:
        print "child process , pid %s , ppid %s" % (os.getpid(), os.getppid())
    else:
        print "parent process, %s , child process %s" % (os.getpid(), pid)

def run_proc(name):
    print 'Run child process %s (%s)...' % (name, os.getpid())

def test2():
    print "Parent process %s" % os.getpid()
    p = Process(target=run_proc, args=("mytest",))
    print "Process will start"
    p.start()
    p.join()
    print "Proecss end"

def long_time_task(name):
    print 'Run task %s (%s)...' % (name, os.getpid())
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print 'Task %s runs %0.2f seconds.' % (name, (end - start))

def test3():
    print "Parent process %s" % os.getpid()
    p = Pool(5)
    print p._processes
    for i in range(5):
        p.apply_async(long_time_task, args=(i, ))
    print "Waiting for all subprocesss done..."
    p.close()
    p.join()
    print "All Process done."


# 写数据进程执行的代码:
def write(q):
    for value in ['A', 'B', 'C']:
        print 'Put %s to queue...' % value
        q.put(value)
        time.sleep(random.random())


# 读数据进程执行的代码:
def read(q):
    while True:
        value = q.get(True)
        print 'Get %s from queue.' % value


def test():
    # 父进程创建Queue，并传给各个子进程：
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    # 启动子进程pw，写入:
    pw.start()
    # 启动子进程pr，读取:
    pr.start()
    # 等待pw结束:
    pw.join()
    # pr进程里是死循环，无法等待其结束，只能强行终止:
    pr.terminate()

if __name__ == "__main__":
    test()