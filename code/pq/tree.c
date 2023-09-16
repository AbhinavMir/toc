#include <stdio.h>

#define MAX_SIZE 100

// return the index of the parent node
int parent(int i) {
    return (i - 1) / 2;
}

// return the index of the left child node
int left(int i) {
    return 2 * i + 1;
}

// return the index of the right child node
int right(int i) {
    return 2 * i + 2;
}

void swap(int *a, int *b) {
    int tmp = *a;
    *a = *b;
    *b = tmp;
}

void insert (int a[], int data, int *n) 
{
    if (*n == MAX_SIZE) {
        printf("Heap is full\n");
        return;
    }

    a[*n] = data;
    (*n)++;

    int i = *n - 1;
    while (i != 0 && a[parent(i)] > a[i]) {
        swap(&a[parent(i)], &a[i]);
        i = parent(i);
    }
}

// void max_heapify(int