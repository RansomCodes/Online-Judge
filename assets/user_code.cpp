#include <iostream>
using namespace std;

int main() {
    int n, k;
    cin >> n >> k;

    int arr[n];
    int sum = 0;
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
        sum += arr[i];
    }

    if (sum == k) {
        cout << "yess" << endl;
    } else {
        cout << "no" << endl;
    }

    return 0;
}
