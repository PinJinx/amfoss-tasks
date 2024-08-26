#include <stdio.h>

int main() {
    int n;
    printf("Enter a value: ");
    scanf("%d", &n);

    if (n % 2 == 0) {
        n--;
    }

    int k = (n + 1) / 2 - 1;

    for (int i=1; i <= n; i += 2) {
        for (int j = 0; j < k; ++j) {
            printf(" ");
        }
        for (int j = 0; j < i; ++j) {
            printf("*");
        }
        printf("\n");
        k--;
    }

    k = 1;
    for (int i = n-2; i >0; i -= 2) {
        for (int j= 0; j<k; ++j) {
            printf(" ");
        }
        for (int j = 0; j< i; ++j) {
            printf("*");
        }
        printf("\n");
        k++;
    }

    return 0;
}