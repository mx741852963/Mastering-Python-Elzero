# --------------------------------------------------------------------
# -- Data Structures: Stacks & Queues (Simplified for ML Engineers) --
# --------------------------------------------------------------------

# 1. Stack (LIFO - Last In, First Out)
# -----------------------------------
# - Definition: A collection where the last element added is the first one to be removed.
# - Analogy: A stack of plates. You can only take the one on top.
# - Operations:
#   * Push: Adding an element (using .append())
#   * Pop: Removing the last element (using .pop())
# - Best for: Undo/Redo operations, Depth-First Search (DFS) algorithms.

# Example:
# my_stack = []
# my_stack.append("Task 1")
# my_stack.append("Task 2")
# my_stack.pop()  # Removes "Task 2"

#

# 2. Queue (FIFO - First In, First Out)
# ------------------------------------
# - Definition: A collection where the first element added is the first one to be removed.
# - Analogy: A line of people waiting for a bus. The first in line is the first out.
# - Operations:
#   * Enqueue: Adding an element to the back (using .append())
#   * Dequeue: Removing the element from the front (using .popleft())
# - Best for: Task scheduling, Breadth-First Search (BFS) algorithms.
# - Note: We use 'collections.deque' for performance (O(1) time).

# Example:
# from collections import deque
# my_queue = deque(["Car 1", "Car 2"])
# my_queue.popleft()  # Removes "Car 1"

#

# 3. Performance Summary
# ----------------------
# - Stack: Use standard list. Fast for append/pop from the end.
# - Queue: Use deque. Much faster than list.pop(0) which is very slow (O(n)).
# --------------------------------------------------------------------
from collections import deque

queue = deque()
queue.append("car1")
queue.append("car2")
queue.append("car3")
queue.append("car4")
queue.append("car5")
print(queue)
# print(type(queue))
print(queue.popleft())
# print(queue.popleft())
# print(queue.popleft())
# print(queue.popleft())
# print(queue.popleft())
# # print(queue.popleft()) IndexError: pop from an empty deque
# print(repr(queue))
print(queue)
