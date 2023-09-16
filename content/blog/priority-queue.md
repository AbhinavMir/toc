---
title: "Priority Queues"
draft: false
---

A priority queue is a data structure that maintains a collection of elements, each associated with a priority or key, and provides efficient access to the element with the highest (or lowest) priority. It allows for the insertion and removal of elements based on their priorities, making it a fundamental tool for tasks where items need to be processed in order of importance, such as scheduling tasks, graph algorithms, and simulation. Priority queues can be implemented using various data structures, each with its own trade-offs in terms of time complexity and efficiency.

Priority queues are used in applications requiring efficient management of elements with associated priorities, including scheduling, graph algorithms, data compression, and task prioritization.

### Implementation

1-3 are naive ways to implement a priority queue. 4 is the most efficient way to implement a priority queue, it uses a heap. In priority queues, the most commonly used heap is the binary heap. Binary heaps can be either min-heaps or max-heaps, depending on whether you want the minimum or maximum element to have the highest priority. While insertion is fastest in unsorted arrays, peek and delete are fastest in sorted arrays. Binary heaps are the most efficient way to implement a priority queue, with logarithmic time complexities for insertion and deletion.

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

These time complexities describe the efficiency of each method for the different priority queue implementations. Binary heaps are particularly efficient for priority queues due to their logarithmic time complexities for insertion and deletion, making them suitable for many applications where efficient priority queue operations are required.