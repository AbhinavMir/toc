#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

void galeShapley(int menPreferences[4][4], int womenPreferences[4][4], int n) {
    int wPartner[n];
    bool mEngaged[n];
    int men_proposals[n][n];

    for (int i = 0; i < n; i++) {
        wPartner[i] = -1;
        mEngaged[i] = false;
        for (int j = 0; j < n; j++) {
            men_proposals[i][j] = 0;
        }
    }

    int freeCount = n;

    while (freeCount > 0) {
        int m;
        for (m = 0; m < n; m++)
            if (mEngaged[m] == false)
                break;

        for (int i = 0; i < n && mEngaged[m] == false; i++) {
            int w = menPreferences[m][i];

            if (men_proposals[m][w] == 0) {
                men_proposals[m][w] = 1;

                if (wPartner[w] == -1) {
                    wPartner[w] = m;
                    mEngaged[m] = true;
                    freeCount--;
                } else {
                    int m1 = wPartner[w];

                    bool preferM1 = false;
                    for (int j = 0; j < n; j++) {
                        if (womenPreferences[w][j] == m1) {
                            preferM1 = true;
                            break;
                        }
                        if (womenPreferences[w][j] == m)
                            break;
                    }

                    if (!preferM1) {
                        wPartner[w] = m;
                        mEngaged[m] = true;
                        mEngaged[m1] = false;
                    }
                }
            }
        }
    }

    printf("Man   Woman\n");
    for (int i = 0; i < n; i++)
        printf(" %d      %d\n", i + 1, wPartner[i] + 1);
}

int main() {
    int menPreferences[4][4] = {{3, 1, 2, 0}, {1, 2, 3, 0}, {2, 1, 0, 3}, {1, 2, 3, 0}};
    int womenPreferences[4][4] = {{2, 0, 3, 1}, {0, 2, 1, 3}, {3, 2, 1, 0}, {2, 1, 0, 3}};

    galeShapley(menPreferences, womenPreferences, 4);

    return 0;
}
