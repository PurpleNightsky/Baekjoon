#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
#include <iostream>
using namespace std;

int main() {
    int N, K;
    scanf("%d %d", &N, &K);
    int M1 = 1;
    int M2 = 1;
    int M3 = 1;

    for (int i = 1; i <= N; i++) {
        M1 *= i;
    }

    for (int j = 1; j <= K; j++) {
        M2 *= j;
    }

    for (int n = 1; n <= N - K; n++) {
        M3 *= n;
    }
    printf("%d", M1 / (M2 * M3));
    return 0;
}