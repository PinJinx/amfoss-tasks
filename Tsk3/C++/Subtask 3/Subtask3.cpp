#include <iostream>

using namespace std;

int main() {
    int n;
    cout << "Enter a value: ";
    cin >> n;

    if (n % 2 == 0) {
        n--;
    }

    int k = (n + 1) / 2 - 1;

    for (int i = 1; i <= n; i += 2) {
        for (int j = 0; j < k; ++j) {
            cout << " ";
        }
        for (int j = 0; j < i; ++j) {
            cout << "*";
        }
        cout << endl;
        k--;
    }

    k = 1;
    for (int i = n - 2; i > 0; i -= 2) {
        for (int j = 0; j < k; ++j) {
            cout << " ";
        }
        for (int j = 0; j < i; ++j) {
            cout << "*";
        }
        cout << endl;
        k++;
    }

    return 0;
}