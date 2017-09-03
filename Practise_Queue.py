from collections import deque
queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")           # Terry arrives
queue.append("Graham")   
print(queue)                    # Graham arrives
queue.popleft()                 # The first to arrive now leaves
print(queue)  
queue.popleft()                 # The second to arrive now leaves
print(queue)                    # Remaining queue in order of arrival
