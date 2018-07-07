# usr/bin/python3
# -*- coding: utf-8 -*-
# /**
#  *                    _ooOoo_
#  *                   o8888888o
#  *                   88" . "88
#  *                   (| -_- |)
#  *                    O\ = /O
#  *                ____/`---'\____
#  *              .   ' \\| |// `.
#  *               / \\||| : |||// \
#  *             / _||||| -:- |||||- \
#  *               | | \\\ - /// | |
#  *             | \_| ''\---/'' | |
#  *              \ .-\__ `-` ___/-. /
#  *           ___`. .' /--.--\ `. . __
#  *        ."" '< `.___\_<|>_/___.' >'"".
#  *       | | : `- \`.;`\ _ /`;.`/ - ` : | |
#  *         \ \ `-. \_ __\ /__ _/ .-` / /
#  * ======`-.____`-.___\_____/___.-`____.-'======
#  *                    `=---='
#  *
#  * .............................................
#  *          佛祖保佑             永无BUG
#  */

"""
Project:LS  
Date:2018/6/23
QQ:1217750958
"""
__author__ = 'LS'

"""
对于操作系统来说，一个任务就是一个进程（Process），比如打开一个浏览器就是启动一个浏览器进程，打开一个记事本就启动了一个记事本进程，打开两个记事本就启动了两个记事本进程，打开一个Word就启动了一个Word进程。

有些进程还不止同时干一件事，比如Word，它可以同时进行打字、拼写检查、打印等事情。在一个进程内部，要同时干多件事，就需要同时运行多个“子任务”，我们把进程内的这些“子任务”称为线程（Thread）。

总结一下就是，多任务的实现有3种方式：

多进程模式；
多线程模式；
多进程+多线程模式。
同时执行多个任务通常各个任务之间并不是没有关联的，而是需要相互通信和协调，
有时，任务1必须暂停等待任务2完成后才能继续执行，有时，任务3和任务4又不能同时执行，
所以，多进程和多线程的程序的复杂度要远远高于我们前面写的单进程单线程的程序。


"""
# print '----------------------------------------------python并发编程之多进程--------------------------------------------------111'
"""
1、multiprocessing模块介绍
multiprocessing模块用来开启子进程，并在子进程中执行我们定制的任务（比如函数），该模块与多线程模块threading的编程接口类似。
multiprocessing模块的功能众多：支持子进程、通信和共享数据、执行不同形式的同步，提供了Process、Queue、Pipe、Lock等组件。
需要再次强调的一点是：与线程不同，进程没有任何共享状态，进程修改的数据，改动仅限于该进程内。

2、Process类的介绍
创建进程的类
Process([group [, target [, name [, args [, kwargs]]]]])，由该类实例化得到的对象，表示一个子进程中的任务（尚未启动）

强调：
1. 需要使用关键字的方式来指定参数
2. args指定的为传给target函数的位置参数，是一个元组形式，必须有逗号

参数介绍

group参数未使用，值始终为None
target表示调用对象，即子进程要执行的任务
args表示调用对象的位置参数元组，args=(1,2,'hexin',)
kwargs表示调用对象的字典,kwargs={'name':'hexin','age':18}
name为子进程的名称

方法介绍

p.start()：启动进程，并调用该子进程中的p.run() 
p.run():进程启动时运行的方法，正是它去调用target指定的函数，我们自定义类的类中一定要实现该方法  
p.terminate():强制终止进程p，不会进行任何清理操作，如果p创建了子进程，该子进程就成了僵尸进程，使用该方法需要特别小心这种情况。如果p还保存了一个锁那么也将不会被释放，进而导致死锁
p.is_alive():如果p仍然运行，返回True
p.join([timeout]):主线程等待p终止（强调：是主线程处于等的状态，而p是处于运行的状态）。timeout是可选的超时时间，需要强调的是，p.join只能join住start开启的进程，而不能join住run开启的进程

属性介绍

p.daemon：默认值为False，如果设为True，代表p为后台运行的守护进程，当p的父进程终止时，p也随之终止，并且设定为True后，p不能创建自己的新进程，必须在p.start()之前设置
p.name:进程的名称
p.pid：进程的pid
p.exitcode:进程在运行时为None、如果为–N，表示被信号N结束(了解即可)
p.authkey:进程的身份验证键,默认是由os.urandom()随机生成的32字符的字符串。这个键的用途是为涉及网络连接的底层进程间通信提供安全性，这类连接只有在具有相同的身份验证键时才能成功（了解即可）

"""
# from multiprocessing import Process,Pool
# import os
# import time
#
# def run_proc(wTIme):
#     n = 0
#     while n < 3:
#         print "子进程 %s run," % os.getpid(),"{0}".format(time.ctime())   ##获取当前进程号和正在运行是的时间
#         time.sleep(wTIme)        #  #等待（休眠）
#         n += 1
#
# if __name__ == "__main__":          # 注意：在windows中Process()必须放到# if __name__ == '__main__':下
#     p = Process(target=run_proc, args=(2,))         #申请子进程, #必须加,号
#
#     p.daemon = True  # 加入daemon,其父进程结束，该进程也直接终止运行（即使还没运行完）
#
#     p.start()     #运行进程
#
#     p.join()  # 加入join方法,它使子进程执行结束后，父进程才执行之后的代码,这样所有的进程就能顺利的执行了
#
#     print "父进程开始运行. 子进程是 ", p.pid
#     print "父进程结束,{0}".format(time.ctime())

# --------------------------------------------------------

# import multiprocessing
# import time
#
#
# def process(num):
#     time.sleep(num)
#     print 'Process:', num
#
#
# if __name__ == '__main__':
#     for i in range(5):
#         p = multiprocessing.Process(target=process, args=(i,))
#         p.start()
#
#     print('CPU number:' + str(multiprocessing.cpu_count()))
#     for p in multiprocessing.active_children():
#         print('Child process name: ' + p.name + ' id: ' + str(p.pid))
#
#     print('Process Ended')

"""
根据运行结果可知，父进程运行结束后子进程仍然还在运行，这可能造成僵尸（ zombie）进程。

通常情况下，当子进程终结时，它会通知父进程，清空自己所占据的内存，并在内核里留下自己的退出信息。父进程在得知子进程终结时，会从内核中取出子进程的退出信息。但是，如果父进程早于子进程终结，这可能造成子进程的退出信息滞留在内核中，子进程成为僵尸（zombie）进程。当大量僵尸进程积累时，内存空间会被挤占。

有什么办法可以避免僵尸进程呢？ 
这里介绍进程的一个属性 deamon，当其值为TRUE时，其父进程结束，该进程也直接终止运行（即使还没运行完）。 
所以给上面的程序加上p.deamon = true，看看效果。
"""

"""
子进程并没有执行完，这不是所期望的结果。有没办法将子进程执行完后才让父进程结束呢？ 
这里引入p.join()方法，它使子进程执行结束后，父进程才执行之后的代码
"""

"""
#进程对象的其他方法一:terminate,is_alive
p1.terminate()#关闭进程,不会立即关闭,所以is_alive立刻查看的结果可能还是存活
print(p1.is_alive()) #结果为True

#进程对象的其他方法二:p.daemon=True,p.join
p.daemon=True #一定要在p.start()前设置,设置p为守护进程,禁止p创建子进程,并且父进程死,p跟着一起死
p.start()
p.join(0.0001) #等待p停止,等0.0001秒就不再等了
注意：p.join(),是父进程在等p的结束，是父进程阻塞在原地，而p仍然在后台运行


"""

#print '---------------------------------------------将进程定义成类----------------------------------------------------------'
# from multiprocessing import Process, Pool
# import os
# import time
#
#
# class Myprocess(Process):
#
#     def __init__(self, wTime):
#         Process.__init__(self)
#         self.wTime = wTime
#
#     def run(self):
#         n = 0
#         while n < 3:
#             print "subProcess %s run," % os.getpid(), "{0}".format(time.ctime())
#             time.sleep(self.wTime)
#             n += 1
#
#
# if __name__ == "__main__":
#     p = Myprocess(2)
#     p.daemon = True
#     p.start()    #自动调用run方法
#     p.join()
#     print "Parent process run. subProcess is ", p.pid
#     print "Parent process end,{0}".format(time.ctime())

#------------------------------------------------------------------

# from multiprocessing import Process
# import time
#
#
# class MyProcess(Process):
#     def __init__(self, loop):
#         Process.__init__(self)
#         self.loop = loop
#
#     def run(self):
#         for count in range(self.loop):
#             time.sleep(1)
#             print('Pid: ' + str(self.pid) + ' LoopCount: ' + str(count))
#
#
# if __name__ == '__main__':
#     for i in range(2, 5):
#         p = MyProcess(i)
#         p.start()
#
# print '----------------------------------------进程池------------------------------------------------------'

"""
创建多个进程
很多时候系统都需要创建多个进程以提高CPU的利用率，当数量较少时，可以手动生成一个个Process实例。
当进程数量很多时，或许可以利用循环，但是这需要程序员手动管理系统中并发进程的数量，有时会很麻烦。这时进程池Pool就可以发挥其功效了。
可以通过传递参数限制并发进程的数量，默认值为CPU的核数。 
"""

# from multiprocessing import Process,Pool
# import os,time
#
# def run_proc(name):        ##定义一个函数用于进程调用
#     for i in range(5):
#         time.sleep(0.2)    #休眠0.2秒
#         print 'Run child process %s (%s)' % (name, os.getpid())
# #执行一次该函数共需1秒的时间
#
# if __name__ =='__main__': #执行主进程
#     print 'Run the main process (%s).' % (os.getpid())
#     mainStart = time.time() #记录主进程开始的时间
#     p = Pool(8)           #开辟进程池
#     for i in range(16):                                 #开辟14个进程
#         p.apply_async(run_proc,args=('Process'+str(i),))#每个进程都调用run_proc函数，
#                                                         #args表示给该函数传递的参数。
#
#     print 'Waiting for all subprocesses done ...'
#     p.close() #关闭进程池
#     p.join()  #等待开辟的所有进程执行完后，主进程才继续往下执行
#     print 'All subprocesses done'
#     mainEnd = time.time()  #记录主进程结束时间
#     print 'All process ran %0.2f seconds.' % (mainEnd-mainStart)  #主进程执行时间

"""
这里进程池对并发进程的限制数量为8个，而程序运行时会产生16个进程，进程池将自动管理系统内进程的并发数量，其余进程将会在队列中等待。
限制并发数量是因为，系统中并发的进程不是越多越好，并发进程太多，可能使CPU大部分的时间用于进程调度，而不是执行有效的计算。

采用多进程并发技术时，就单个处理机而言，其对进程的执行是串行的。
但具体某个时刻哪个进程获得CPU资源而执行是不可预知的（如执行结果的开头部分，各进程的执行顺序不定），这就体现了进程的异步性。

如果单个程序执行14次run_proc函数，那么它会需要至少16秒,通过进程的并发，这里只需要2.49秒，可见并发的优势。
"""

#print '----------------------------------------多线程之threading模块--------------------------------------------------------------'

"""
Python3 通过两个标准库 _thread 和 threading 提供对线程的支持。

_thread 提供了低级别的、原始的线程以及一个简单的锁，它相比于 threading 模块的功能还是比较有限的。

threading 模块除了包含 _thread 模块中的所有方法外，还提供的其他方法：

threading.currentThread(): 返回当前的线程变量。
threading.enumerate(): 返回一个包含正在运行的线程的list。正在运行指线程启动后、结束前，不包括启动前和终止后的线程。
threading.activeCount(): 返回正在运行的线程数量，与len(threading.enumerate())有相同的结果。
除了使用方法外，线程模块同样提供了Thread类来处理线程，Thread类提供了以下方法:

run(): 用以表示线程活动的方法。
start():启动线程活动。
join([time]): 等待至线程中止。这阻塞调用线程直至线程的join() 方法被调用中止-正常退出或者抛出未处理的异常-或者是可选的超时发生。
isAlive(): 返回线程是否活动的。
getName(): 返回线程名。
setName(): 设置线程名。
"""

#print '---------------------使用 threading 模块创建线程-------------------------'
#我们可以通过直接从 threading.Thread 继承创建一个新的子类，并实例化后调用 start() 方法启动新线程，即它调用了线程的 run() 方法：

#!/usr/bin/python3

# import threading
# import time
#
# exitFlag = 0
#
# class myThread (threading.Thread):
#     def __init__(self, threadID, name, counter):
#         threading.Thread.__init__(self)
#         self.threadID = threadID
#         self.name = name
#         self.counter = counter
#     def run(self):
#         print ("开始线程：" + self.name)
#         print_time(self.name, self.counter, 5)
#         print ("退出线程：" + self.name)
#
# def print_time(threadName, delay, counter):
#     while counter:
#         if exitFlag:
#             threadName.exit()
#         time.sleep(delay)
#         print ("%s: %s" % (threadName, time.ctime(time.time())))
#         counter -= 1
#
# # 创建新线程
# thread1 = myThread(1, "Thread-1", 1)
# thread2 = myThread(2, "Thread-2", 2)
#
# # 开启新线程
# thread1.start()
# thread2.start()
# thread1.join()
# thread2.join()
# print ("退出主线程")

#print '-----------------------线程同步----------------------------------'

"""
如果多个线程共同对某个数据修改，则可能出现不可预料的结果，为了保证数据的正确性，需要对多个线程进行同步。
使用 Thread 对象的 Lock 和 Rlock 可以实现简单的线程同步，这两个对象都有 acquire 方法和 release 方法，对于那些需要每次只允许一个线程操作的数据，可以将其操作放到 acquire 和 release 方法之间。如下：
多线程的优势在于可以同时运行多个任务（至少感觉起来是这样）。但是当线程需要共享数据时，可能存在数据不同步的问题。
考虑这样一种情况：一个列表里所有元素都是0，线程"set"从后向前把所有元素改成1，而线程"print"负责从前往后读取列表并打印。
那么，可能线程"set"开始改的时候，线程"print"便来打印列表了，输出就成了一半0一半1，这就是数据的不同步。为了避免这种情况，引入了锁的概念。
锁有两种状态——锁定和未锁定。每当一个线程比如"set"要访问共享数据时，必须先获得锁定；如果已经有别的线程比如"print"获得锁定了，那么就让线程"set"暂停，也就是同步阻塞；等到线程"print"访问完毕，释放锁以后，再让线程"set"继续。
经过这样的处理，打印列表时要么全部输出0，要么全部输出1，不会再出现一半0一半1的尴尬场面。
"""

#!/usr/bin/python3

# import threading
# import time
#
# class myThread (threading.Thread):
#     def __init__(self, threadID, name, counter):
#         threading.Thread.__init__(self)
#         self.threadID = threadID
#         self.name = name
#         self.counter = counter
#     def run(self):
#         print ("开启线程： " + self.name)
#         # 获取锁，用于线程同步
#         threadLock.acquire()
#         print_time(self.name, self.counter, 3)
#         # 释放锁，开启下一个线程
#         threadLock.release()
#
# def print_time(threadName, delay, counter):
#     while counter:
#         time.sleep(delay)
#         print ("%s: %s" % (threadName, time.ctime(time.time())))
#         counter -= 1
#
# threadLock = threading.Lock()
# threads = []
#
# # 创建新线程
# thread1 = myThread(1, "Thread-1", 1)
# thread2 = myThread(2, "Thread-2", 2)
#
# # 开启新线程
# thread1.start()
# thread2.start()
#
# # 添加线程到线程列表
# threads.append(thread1)
# threads.append(thread2)
#
# # 等待所有线程完成
# for t in threads:
#     t.join()
# print ("退出主线程")

#print '------------------------------线程优先级队列（ Queue）--------------------'

"""
Python 的 Queue 模块中提供了同步的、线程安全的队列类，包括FIFO（先入先出)队列Queue，LIFO（后入先出）队列LifoQueue，和优先级队列 PriorityQueue。
这些队列都实现了锁原语，能够在多线程中直接使用，可以使用队列来实现线程间的同步。
Queue 模块中的常用方法:

Queue.qsize() 返回队列的大小
Queue.empty() 如果队列为空，返回True,反之False
Queue.full() 如果队列满了，返回True,反之False
Queue.full 与 maxsize 大小对应
Queue.get([block[, timeout]])获取队列，timeout等待时间
Queue.get_nowait() 相当Queue.get(False)
Queue.put(item) 写入队列，timeout等待时间
Queue.put_nowait(item) 相当Queue.put(item, False)
Queue.task_done() 在完成一项工作之后，Queue.task_done()函数向任务已经完成的队列发送一个信号
Queue.join() 实际上意味着等到队列为空，再执行别的操作
"""

#!/usr/bin/python3

# import threading
# import queue
# import time
#
# exitFlag = 0
#
# class myThread (threading.Thread):
#     def __init__(self, threadID, name, q):
#         threading.Thread.__init__(self)
#         self.threadID = threadID
#         self.name = name
#         self.q = q
#     def run(self):
#         print ("开启线程：" + self.name)
#         process_data(self.name, self.q)
#         print ("退出线程：" + self.name)
#
# def process_data(threadName, q):
#     while not exitFlag:
#         queueLock.acquire()
#         if not workQueue.empty():
#             data = q.get()
#             queueLock.release()
#             print ("%s processing %s" % (threadName, data))
#         else:
#             queueLock.release()
#         time.sleep(1)
#
# threadList = ["Thread-1", "Thread-2", "Thread-3"]
# nameList = ["One", "Two", "Three", "Four", "Five"]
# queueLock = threading.Lock()
# workQueue = queue.Queue(10)
# threads = []
# threadID = 1
#
# # 创建新线程
# for tName in threadList:
#     thread = myThread(threadID, tName, workQueue)
#     thread.start()
#     threads.append(thread)
#     threadID += 1
#
# # 填充队列
# queueLock.acquire()
# for word in nameList:
#     workQueue.put(word)
# queueLock.release()
#
# # 等待队列清空
# while not workQueue.empty():
#     pass
#
#
# # 通知线程是时候退出
# exitFlag = 1
#
# # 等待所有线程完成
# for t in threads:
#     t.join()
# print ("退出主线程")

