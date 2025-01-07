# 14. Queues
l_queue= [1, 2, 3, 4]
from collections import deque
queue = deque([])
queue.append(1)
queue.append(2)
queue.append(3)
queue.append(4)
queue.popleft()
if not queue:
    print("empty")

print(queue)