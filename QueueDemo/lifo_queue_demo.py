import queue

lq = queue.LifoQueue()
lq.put("Python")
lq.put("Django")
lq.put("DRF")
lq.put("Dock for Django")

print(lq.queue)
print("Size:", lq.qsize())
while not lq.empty():
    print(lq.get())
print("Size:", lq.qsize())
