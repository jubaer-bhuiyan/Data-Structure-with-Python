# A simple stack using Python list

stack = []  # empty stack

# Push items (add to top)
stack.append('apple')
stack.append('banana')
stack.append('cherry')

print("Stack now:", stack)  # ['apple', 'banana', 'cherry']

# Peek (see the top item)
print("Top item:", stack[-1])  # cherry

# Pop item (remove top item)
top_item = stack.pop()
print("Popped:", top_item)  # cherry

# Check if empty
print("Is stack empty?", len(stack) == 0)

# Size of stack
print("Stack size:", len(stack))
