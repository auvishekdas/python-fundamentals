from collections import deque
University = deque(["Emon","Rafsan","Zamil","Sharif","Mahim"])
print(University)
University.popleft()
print(University)
University.popleft()
University.popleft()
University.popleft()
University.popleft()

if not University:
    print("No student left")