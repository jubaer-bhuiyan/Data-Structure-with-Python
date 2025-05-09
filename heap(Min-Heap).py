import heapq

# Create an empty list to use as a heap
min_heap = []

# Insert elements using heappush
heapq.heappush(min_heap, 10)
heapq.heappush(min_heap, 5)
heapq.heappush(min_heap, 8)
heapq.heappush(min_heap, 3)

# Display the heap (not sorted, but heap order)
print("Heap array (min-heap):", min_heap)

# Access the smallest element
print("Smallest element:", min_heap[0])

# Remove the smallest element
smallest = heapq.heappop(min_heap)
print("Removed smallest:", smallest)

# Heap after removal
print("Heap now:", min_heap)
