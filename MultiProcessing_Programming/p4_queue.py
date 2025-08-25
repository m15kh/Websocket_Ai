from multiprocessing import Process, Queue

def p1_func(queue):
    nums = queue.get()
    nums.extend([1, 2, 3])
    queue.put(nums)
    print(nums)


def p2_func(queue):
    nums = queue.get()
    nums.extend([4, 5, 6])  # Modify the list retrieved from the queue
    queue.put(nums)         # Put the modified list back into the queue
    print(nums)

qs = Queue()
qs.put([])  # Initialize with an empty list

p1 = Process(target=p1_func, args=(qs,))
p2 = Process(target=p2_func, args=(qs,))

p1.start()
p2.start()
p1.join()
p2.join()

print(qs.get())  # Retrieve and print the final list from the queue