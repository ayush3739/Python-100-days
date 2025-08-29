#include <iostream>
#include <iomanip>
using namespace std;

int main() {
    int N;
    cin >> N;

    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            int layer = min(min(i, j), min(N - 1 - i, N - 1 - j));
            int start = 4 * layer * (N - layer) + 1;

            int val;
            if (i == layer) { // top row
                val = start + (j - layer);
            } else if (j == N - layer - 1) { // right column
                val = start + (N - 2 * layer - 1) + (i - layer);
            } else if (i == N - layer - 1) { // bottom row
                val = start + 2 * (N - 2 * layer - 1) + (N - layer - 1 - j);
            } else { // left column
                val = start + 3 * (N - 2 * layer - 1) + (N - layer - 1 - i);
            }

            cout << setw(2) << setfill('0') << val << " ";
        }
        cout << "\n";
    }
    return 0;
}
