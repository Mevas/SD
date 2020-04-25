from fibonacci_heap import FibonacciHeap

# Create the heap
heap = FibonacciHeap()

print('Insertion')
heap.insert(1)
print(heap)
heap.insert(2)
print(heap)
heap.insert(3)
print(heap)
heap.insert(4)
print(heap)
heap.insert(5)
print(heap)
# Duplicate
heap.insert(3)
print(heap)

print('\nFinding the minimum without removing it')
print(heap)
print(heap.find_min().value)
print(heap)

print('\nExtracting the minumum')
print(heap)
print(heap.extract_min())
print(heap)
print(heap.extract_min())
print(heap)
print(heap.extract_min())
print(heap)
print(heap.extract_min())
print(heap)
print(heap.extract_min())
print(heap)
print(heap.extract_min())
print(heap)

print('\nMerging 2 heaps')
heap.insert(2)
heap.insert(9)

heapToMerge = FibonacciHeap()
heapToMerge.insert(1)
heapToMerge.insert(2)
heapToMerge.insert(3)
heapToMerge.insert(7)

print(heap)
print(heapToMerge)

merged = heap.merge(heapToMerge)

print('\nMerged list')
print(merged)
