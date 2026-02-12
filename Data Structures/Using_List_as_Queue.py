from collections import deque


List = deque(["a", "b", "c", "d", "e"])

# adds z to the end of the list
List.append("z")
print(List)

# removes the first element from the list
List.popleft()
print(List)

