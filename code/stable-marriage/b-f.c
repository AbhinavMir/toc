#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

void permute(int *array, int start, int end, int n, int menPreferences[4][4], int womenPreferences[4][4]);
bool isStable(int *permutation, int n, int menPreferences[4][4], int womenPreferences[4][4]);
void swap(int *a, int *b);

int main() {
    int menPreferences[4][4] = {{7, 5, 6, 8}, {5, 6, 7, 8}, {6, 5, 8, 7}, {5, 6, 7, 8}};
    int womenPreferences[4][4] = {{3, 1, 4, 2}, {1, 3, 2, 4}, {4, 3, 2, 1}, {3, 2, 1, 4}};
    int n = 4;

    int *permutation = malloc(n * sizeof(int));
    for (int i = 0; i < n; i++) {
        permutation[i] = i + n + 1;
    }

    permute(permutation, 0, n - 1, n, menPreferences, womenPreferences);

    free(permutation);

    return 0;
}

void permute(int *array, int start, int end, int n, int menPreferences[4][4], int womenPreferences[4][4]) {
    if (start == end) {
        if (isStable(array, n, menPreferences, womenPreferences)) {
            printf("Stable permutation found:\n");
            for (int i = 0; i < n; i++) {
                printf("%d ", array[i]);
            }
            printf("\n");
            exit(0);
        }
        return;
    }

    for (int i = start; i <= end; i++) {
        swap((array + i), (array + start));
        permute(array, start + 1, end, n, menPreferences, womenPreferences);
        swap((array + i), (array + start));
    }
}

bool isStable(int *permutation, int n, int menPreferences[4][4], int womenPreferences[4][4]) {
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if (menPreferences[i][j] == permutation[i]) {
                break;
            }

            for (int k = 0; k < n; k++) {
                if (womenPreferences[menPreferences[i][j] - n - 1][k] == i + 1) {
                    break;
                }
                if (womenPreferences[menPreferences[i][j] - n - 1][k] == permutation[i]) {
                    return false;
                }
            }
        }
    }

    return true;
}

void swap(int *a, int *b) {
    int temp = *a;
    *a = *b;
    *b = temp;
}
