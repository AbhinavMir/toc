---
title: "Priority Queues"
draft: false
---

A priority queue is a data structure that maintains a collection of elements, each associated with a priority or key, and provides efficient access to the element with the highest (or lowest) priority. It allows for the insertion and removal of elements based on their priorities, making it a fundamental tool for tasks where items need to be processed in order of importance, such as scheduling tasks, graph algorithms, and simulation. Priority queues can be implemented using various data structures, each with its own trade-offs in terms of time complexity and efficiency.

Priority queues are used in applications requiring efficient management of elements with associated priorities, including scheduling, graph algorithms, data compression, and task prioritization.

1. Insert (Enqueue): This operation allows you to add a new element to the priority queue while ensuring that it is placed in the correct position according to its priority. It should be efficient to insert elements in the order of their priority.

2. Delete (Dequeue): Deleting or dequeuing an element from the priority queue typically removes the element with the highest (or lowest) priority and adjusts the queue to maintain the priority order. This operation should be efficient, and the removed element should be returned.

3. Peek (Front): The peek operation lets you view the element with the highest (or lowest) priority without removing it from the queue. It is essential for checking the next element to be dequeued without altering the queue's state.

4. IsEmpty: This operation checks whether the priority queue is empty. It returns a boolean value (true if the queue is empty, false if it contains elements). It's a basic check that helps in controlling the flow of your program.

5. Change Priority: This operation allows you to change the priority of an element in the queue. It is useful when the priority of an element changes during the execution of your program.

### Implementation

1-3 are naive ways to implement a priority queue. 4 is the most efficient way to implement a priority queue, it uses a heap. In priority queues, the most commonly used heap is the binary heap. Binary heaps can be either min-heaps or max-heaps, depending on whether you want the minimum or maximum element to have the highest priority. While insertion is fastest in unsorted arrays, peek and delete are fastest in sorted arrays. Binary heaps are the most efficient way to implement a priority queue, with logarithmic time complexities for insertion and deletion. Binary heaps just outsource the sorting to the insertion algorithm, which is why they are so efficient.

1. **Unsorted Array**:
   - Insert (Enqueue): [$ O(1) $] (average case), [$ O(n) $] (worst case)
   - Delete (Dequeue): [$ O(n) $]
   - Peek (Front): [$ O(n) $]
   - IsEmpty: [$ O(1) $]

2. **Sorted Array**:
   - Insert (Enqueue): [$ O(n) $]
   - Delete (Dequeue): [$ O(1) $]
   - Peek (Front): [$ O(1) $]
   - IsEmpty: [$ O(1) $]

3. **Sorted Linked List**:
   - Insert (Enqueue): [$ O(n) $]
   - Delete (Dequeue): [$ O(1) $]
   - Peek (Front): [$ O(1) $]
   - IsEmpty: [$ O(1) $]

4. **Binary Heap (Min-Heap or Max-Heap)**:
   - Insert (Enqueue): [$ O(\log n) $]
   - Delete (Dequeue): [$ O(\log n) $]
   - Peek (Front): [$ O(1) $]
   - IsEmpty: [$ O(1) $]

5. **D-ary heaps** are slower than binary heaps because binary heaps have better cache locality compared to d-ary heaps. In modern computer architectures, accessing data in contiguous memory locations is faster than accessing data spread out across multiple memory locations. Binary heaps store elements in a more compact manner, making better use of cache lines and reducing cache misses, which can lead to faster access times.

### Empirical Analysis
