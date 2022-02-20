import queue
import threading
import time

from timer import timer

# Setting up variables
input_values = [100, 10, 7, 2, 15, 150]
my_queue = queue.Queue()
active_thread = []

# Multiply the values
def print_multiply(x):
    output_value = []
    for i in range(1, x+1):
        output_value.append(i * x)
    time.sleep(2)
    print(f"Output \n *** The multiplication result for the {x} is - {output_value}")

# Process the queue
def process_queue(thread_name):
    while True:
        try:
            value = my_queue.get(block=False)
        except queue.Empty:
            return
        else:
            print(thread_name, '-->' , value)
            print_multiply(value)
            

# Multithreading Class
class Multithreading(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name    
    def run(self):
        print(f" ** Starting the thread - {self.name}")
        process_queue(self.name)
        print(f" ** Completed the thread - {self.name}")
"""
Thread.run() method is an inbuilt method of the Thread class of the threading module in Python. This method is used to represent thread's activity. It calls the method expressed as the target argument in the Thread object along with the positional and keyword arguments taken from the args and kwargs arguments, respectively. This method can also be overridden in the subclass.
"""

@timer(1, 5)
def main(): 
    # Fill the queue
    for x in input_values:
        my_queue.put(x)

    
    # Serial process
    process_queue('Serial')
    
    """
    # Parallel process
    #Initializing and starting 3 threads
    thread1 = Multithreading('first')
    thread2 = Multithreading('second')
    thread3 = Multithreading('third')
    thread4 = Multithreading('fourth')

    thread1.start()
    thread2.start()
    thread3.start()
    thread4.start()

    # Join the threads
    thread1.join()
    thread2.join()
    thread3.join()
    thread4.join()
    """

    """
    # Parallel process with for looping
    queue_size = my_queue.qsize() 
    for y in range(1, queue_size + 1):
        z = Multithreading(('thread' + str(y)))
        z.start()
        active_thread.append(z)
    for a in active_thread:
        a.join()
    """
    
