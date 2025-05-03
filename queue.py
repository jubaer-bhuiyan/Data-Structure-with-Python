# A simple queue using a Python list

queue = []  # empty queue

# Enqueue (add items to the back)
queue.append('apple')
queue.append('banana')
queue.append('cherry')

print("Queue now:", queue)  # ['apple', 'banana', 'cherry']

# Dequeue (remove from the front)
first_item = queue.pop(0)
print("Dequeued:", first_item)  # apple

# Peek (see the front item)
print("Front item:", queue[0])  # banana

# Check if empty
print("Is queue empty?", len(queue) == 0)

# Size of queue
print("Queue size:", len(queue))
