import queue

q = queue.Queue()
q.put("Python")
q.put("Django")
q.put("DRF")
q.put("Dock for Django")

print(q.queue)
print("Size:", q.qsize())
while not q.empty():
    print(q.get())
    
print("Size:", q.qsize())
          
