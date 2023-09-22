---
title: "Sorts, Loop Invariants"
date: 2020-05-03T00:00:00-00:00
draft: false
---

Ref. CLRS book, 5.3 Randomized algorithms, Chapter 7 Quicksort, 8.4 Bucket sort

## 1. Randomized Algorithms

Randomized algorithms are algorithms that incorporate randomness into their logic. The randomness allows the algorithm to make random choices during execution, rather than relying solely on the deterministic input. This provides several advantages:

- Randomized algorithms can have good expected performance across all inputs, rather than relying on assumptions about the input distribution.

- They can be useful when little is known about the properties or distribution of the input data.

- The randomness allows the algorithm to avoid worst-case situations.

Some common ways to incorporate randomness into an algorithm include:

- Randomly permuting the input array before processing it. For example, in quicksort this ensures a random pivot element.

- Random sampling of the input. Selecting a random subset of elements can be used to approximate overall properties of the data.

- Making random choices during execution, such as randomly selecting a pivot index in quicksort.

The analysis of randomized algorithms focuses on the expected running time, rather than the worst-case time. This is because the behavior of the algorithm depends on the random choices made, so we analyze the expected cost over all possible random choices.

For example, in randomized quicksort the expected running time is $O(n \log n)$. But for any single execution, the actual running time depends on the random decisions made and could be as bad as $O(n^2)$ in the worst case.

**Lemma 5.1 - Indicator Random Variables**

This lemma relates indicator random variables to event probabilities. 

Let $X_A$ be an indicator random variable for event $A$. Then:

$$E[X_A] = Pr\{A\}$$

The proof follows directly from the definition of indicator random variables and expectation.

This lemma is useful for converting event probabilities into expectations, which allows us to leverage properties like linearity of expectation.

**Lemma 5.2 - Analysis of Hire-Assistant**

This lemma analyzes the expected cost of the hire-assistant algorithm.

It shows that if candidates arrive in random order, the expected total hiring cost is $O(c_h \log n)$.

The proof uses indicator random variables $X_i$ for the event that candidate $i$ is hired. It calculates:

$$E[X_i] = \frac{1}{i}$$

Using linearity of expectation gives the overall $O(\log n)$ result.

**Lemma 5.3 - Randomized Hire-Assistant** 

This lemma shows that if we randomly permute the candidate list, the randomized hire-assistant algorithm still achieves $O(c_h \log n)$ expected cost.

The proof argues that randomly permuting the input enforces the assumption that candidates arrive in random order, matching Lemma 5.2.

**Lemma 5.4 - Permute by Sorting**

This lemma proves that the permute by sorting algorithm produces a uniform random permutation. 

The key idea is that any given element has $1/n!$ probability of winding up in any specific position. This is shown by analyzing cases where certain rank assignments occur.

**Lemma 5.5 - Randomize In-Place**

This lemma proves the randomize in-place algorithm produces a uniform random permutation.

It uses a loop invariant on k-permutations to show that after k iterations, each k-permutation is equally likely to appear in the first k elements.

These lemmas provide important theoretical foundations for analyzing randomized algorithms. The indicator random variable technique is particularly powerful for averaging over random choices.
#### The Hiring Problem

The hire-assistant problem considers the task of hiring the best assistant out of n candidates interviewed sequentially. After each interview, you must either hire that candidate or reject them. Once a candidate is rejected, they cannot be recalled. The goal is to hire the best candidate while minimizing the number of hired and fired assistants.

**Algorithm**

The hire-assistant algorithm maintains the best candidate interviewed so far. It interviews each candidate in turn. If the current candidate is better than the best so far, it hires the candidate and fires the previous best.

Pseudocode:

```
best = 0 // 0 is initial dummy candidate
for i = 1 to n:
   interview candidate i
   if candidate i is better than best:
      best = i
      hire candidate i
```

**Analysis**

To analyze hire-assistant, we let $X_i$ be an indicator random variable denoting whether candidate $i$ is hired.

We assume candidates arrive in random order, so each candidate is equally likely to be the best among the first i interviewed. Therefore:

$$Pr\{X_i = 1\} = \frac{1}{i}$$

By linearity of expectation, the expected number hired is:

$$E[X] = E[\sum_{i=1}^n X_i] = \sum_{i=1}^n E[X_i] = \sum_{i=1}^n \frac{1}{i} = H_n$$

Where $H_n$ is the nth harmonic number, which is $\Theta(\log n)$ by equation (A.7).

Therefore, the expected total cost of hiring is $O(c_h \log n)$, where $c_h$ is the hiring cost per candidate. This is a significant improvement over the worst case of $O(c_h n)$.

So by interviewing candidates in random order, we expect to hire only $O(\log n)$ candidates rather than up to n candidates. This simple randomized algorithm provides excellent performance.

## 2. Quicksort

QuickSort is a divide-and-conquer sorting algorithm that works by selecting a 'pivot' element from the array and partitioning the other elements into two sub-arrays, according to whether they are less than or greater than the pivot. The sub-arrays are then sorted recursively. This process continues until the base case is reached, where an array has one or zero elements, at which point it is already sorted. By repeatedly breaking the array down in this manner and sorting each smaller piece, the entire array becomes sorted when the recursive calls are combined.

TL;DR
- Pick an element, called a pivot, from the array.
- One subarray contains all elements less than the pivot.
- The other contains all elements greater than or equal to the pivot.
- Recursively sort both subarrays.

Some more points.
#### Asymptotic Analysis of Quicksort
1. **Worst-case ($O(n^2)$):**
   - Occurs when the chosen pivot is consistently the smallest or largest element, resulting in the most unbalanced partitions. For example, if the input list is already sorted and we always pick the last (or first) element as the pivot, then each recursive call processes one element fewer than the previous call, leading to a total of $n + (n-1) + (n-2) + ... + 1 = O(n^2)$ comparisons and operations.
   - However, the likelihood of consistently picking the worst pivot is low unless there's a systematic error in pivot selection.

2. **Best-case ($O(n \log n)$):**
   - Happens when the chosen pivot always splits the array into roughly equal halves. This ensures the depth of the recursive call tree is approximately $\log n$.
   - At each depth level, all elements are processed, contributing an $O(n)$ factor. Therefore, with $O(n)$ work across $O(\log n)$ depth levels, the best-case performance is $O(n \log n)$.

3. **Average-case ($O(n \log n)$):**
   - This considers the average behavior across all possible input sequences and pivot selections.
   - On average, the partitioning will be reasonably balanced. Not always perfect, but typically not too skewed either.
   - Like the best-case scenario, the depth of the recursive call tree averages out to $O(\log n)$, with each level doing $O(n)$ work, leading to $O(n \log n)$ performance.

4. **Space Complexity ($O(1)$ for the sorting operations):**
   - QuickSort is an in-place sorting algorithm, which means it doesn't require additional arrays.
   - However, it's worth noting the space used by the call stack. In the best case (or with a good implementation), the recursive depth is $O(\log n)$. In the worst case, it's $O(n)$. Therefore, while the sorting operations themselves only require constant space, the overall space complexity including the call stack can be as bad as $O(n)$ in the worst case.

To optimize QuickSort and make its average performance closer to the best-case scenario, strategies like randomized pivot selection or the "median-of-three" pivot selection (choosing the median of the first, middle, and last elements) can be employed. As mentioned previously, another practical optimization involves switching to a simpler sorting algorithm for small subarrays.
The key to the efficiency of quicksort is how well balanced the partitioning is each time. perfectly balanced partitioning leads to $O(n \log n)$ time. But severely unbalanced partitioning causes worst-case $O(n^2)$ time.

**Randomized Quicksort**

Randomized quicksort selects the pivot randomly, rather than always using a fixed element like the last. This ensures that the pivot does not consistently create worst-case behavior for certain input distributions.

Choosing the pivot randomly guarantees that, on average, the partitioning will be reasonably balanced. Therefore, randomized quicksort maintains its $O(n \log n)$ expected running time.

#### Analysis

1. **Average-case Time Complexity ($\mathbb{E}[T(n)] = O(n \log n)$):**
   - The key insight is that for any two distinct numbers in the array, the probability that they are compared to each other is constant, i.e., it doesn't depend on the size of the array. It's related to the chances that the first one chosen among them becomes a pivot before the other.
   - Over all potential pivot choices, the average number of times an element is involved in a comparison is $\log n$.
   - Therefore, considering all elements, the average-case time complexity is $O(n \log n)$.
   
2. **Worst-case Time Complexity ($O(n^2)$):**
   - Despite the randomization, there's still a possibility, albeit very unlikely, that we consistently choose the worst pivots (e.g., always the smallest or largest element). This would result in a worst-case scenario similar to the deterministic QuickSort.

3. **Best-case Time Complexity ($O(n \log n)$):**
   - This happens when the chosen pivot, on average, divides the array into balanced partitions.

4. **Space Complexity ($O(\log n)$ expected):**
   - As with the traditional QuickSort, randomized QuickSort is in-place and requires no additional array space.
   - The space complexity concerns the call stack. The expected height of the recursive call tree is $\log n$. Thus, even though in the worst case the stack could go up to $O(n)$, on average (and with high probability), the space complexity is $O(\log n)$.

Randomized QuickSort's main advantage is its predictable performance. By choosing the pivot randomly, we avoid worst-case scenarios that can arise from specific patterns in the input data (like already sorted or reverse sorted arrays) that would consistently degrade deterministic QuickSort's performance. While the worst-case time complexity remains the same on paper, the probability of encountering this worst case in practice becomes exceedingly low. This means that for most practical purposes, the expected average time complexity of $O(n \log n)$ holds reliably.

**Comparison of Quicksort and Randomized Quicksort**

Deterministic QuickSort and Randomized QuickSort both have best and worst-case time complexities of $O(n \log n)$ and $O(n^2)$, respectively. However, Randomized QuickSort offers a more consistent average-case performance of $O(n \log n)$ due to its pivot randomization, making it less susceptible to specific input patterns that can degrade performance in deterministic QuickSort. This consistency and predictability make Randomized QuickSort generally preferable in scenarios with unknown or potentially adversarial input patterns.

## 3. Bucket Sort

Bucket sort is an algorithm that runs in linear $O(n)$ average time, but relies on assumptions about the input data. Specifically, it assumes elements are uniformly distributed over the interval $[0, 1)$.

**Algorithm**

Bucket sort divides the interval $[0, 1)$ into $n$ buckets and distributes the $n$ input elements into the buckets. It then simply sorts each bucket using insertion sort.

The key steps are:

- Divide $[0, 1)$ into $n$ buckets
- Distribute input elements uniformly into the buckets
- Sort each bucket individually using insertion sort
- Concatenate the sorted buckets

**Analysis**

The analysis relies on the assumption of a uniform input distribution. This ensures that each bucket will receive roughly the same number of elements.

Let $n_i$ be the random variable for the number of elements in bucket $i$. The expected running time is:

$$E[T(n)] = \Theta(n) + \sum_{i=0}^{n-1} E[O(n_i^2)]$$

Using indicator random variables and linearity of expectation, we can show:

$$E[n_i^2] = 2 - \frac{1}{n}$$

This results in an overall expected running time of $O(n)$.

Bucket sort beats the $\Omega(n \log n)$ comparison sort lower bound by not using comparisons. Instead it relies on the uniform input distribution.



The implementation for the graph below comparing the three algorithms is available [here](https://raw.githubusercontent.com/AbhinavMir/toc/main/code/loops/qs.py), it is written in Python.

![Quicksort vs Randomized Quicksort](https://raw.githubusercontent.com/AbhinavMir/toc/main/code/loops/qs.png)