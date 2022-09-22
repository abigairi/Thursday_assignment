#question number three
queue = []
def enqueue(lst: list,element)->list:
    lst.append(element)
    return element
def dequeue(lst: list):
    if len(lst)>0: return lst.pop(0)
    elif len(lst)==0:
        print('\nEmpty queue Cannot dequeue')
        return
def is_empty(lst: list)->bool:
    return len(lst)==0
def size(lst: list)->int:
    return len(lst)
print(size(queue))

print("My queue elements")
queue.append('black')
queue.append('yellow')
queue.append('blue')
queue.append('green')
queue.append('white')
  
print(queue)
  
print("removing elements dequeued from queue")
print(queue.pop(-1))
print(queue.pop(2))
print(queue)
                   
