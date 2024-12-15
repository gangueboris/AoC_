#include <fstream>
#include <iostream>
#include <sstream>
#include <vector>
#include <unordered_map>
#include <set>
#include <utility>

using namespace std;

int main() {
    ifstream file{"input.txt"};
    string line;
    unordered_map<char, vector<pair<int, int>>> frequencies;
    set<pair<int, int>> visited;
    int i = 0;
    int height;
    int width;

    // Reading the input file
    while (getline(file, line)) {
        width = line.length();
        stringstream ss{line};
        char c;
        int j = 0;

        while (ss >> c) {
            if (c != '.') {
                frequencies[c].push_back({i, j});
            }
            ++j;
        }
        ++i;
    }
    height = i;

    int count = 0;

    for (auto const& [key, values] : frequencies) {
        for (auto const& [r1, c1] : values) {
            for (auto const& [r2, c2] : values) {
                if (r1 != r2 || c1 != c2) {
                    int dr = r2 - r1;
                    int dc = c2 - c1;

                    int rr = r1 - dr;
                    int cc = c1 - dc;
                    if (0 <= rr && rr < height && 0 <= cc && cc < width) {
                        visited.insert({rr, cc});
                    }

                    rr = r2 + dr;
                    cc = c2 + dc;
                    if (0 <= rr && rr < height && 0 <= cc && cc < width) {
                        visited.insert({rr, cc});
                    }
                }
            }
        }
    }

    cout << visited.size() << '\n';

    file.close();
    return EXIT_SUCCESS;
}
