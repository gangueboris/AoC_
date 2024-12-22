#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <set>
#include <queue>
#include <map>
#include <tuple>
#include <deque>
#include <climits> // For INT_MAX

using namespace std;

pair<int, int> findCoord(const vector<vector<char>>& grid){
    for (int r = 0; r < grid.size(); ++r) {
        for (int c = 0; c < grid[0].size(); ++c) {
            if (grid[r][c] == 'S'){
                return {r, c};
            }
        }
    }
    return {0, 0};
}

bool isValid(int r, int c, int ROW, int COL, const vector<vector<char>>& grid){
    return 0 <= r && r < ROW && 0 <= c && c < COL && grid[r][c] != '#';
}

int solve(const vector<vector<char>>& grid, int sr, int sc){
    using State = tuple<int, int, int, int, int>;

    priority_queue<State, vector<State>, greater<>> pq; 
    map<tuple<int, int, int, int>, int> lowest_cost;  
    map<tuple<int, int, int, int>, set<tuple<int, int, int, int>>> backtrack;
    set<tuple<int, int, int, int>> end_states;

    int best_cost = INT_MAX;
    int ROW = grid.size(), COL = grid[0].size();

    pq.push({0, sr, sc, 0, 1}); 
    lowest_cost[{sr, sc, 0, 1}] = 0;

    while (!pq.empty()){
        auto [cost, r, c, dr, dc] = pq.top();
        pq.pop();

        if (cost > lowest_cost[{r, c, dr, dc}]) continue;

        if (grid[r][c] == 'E') {
            if (cost > best_cost) break;
            best_cost = cost;
            end_states.insert({r, c, dr, dc});
        }

        vector<State> moves = {{cost + 1, r + dr, c + dc, dr, dc},{cost + 1000, r, c, dc, -dr},{cost + 1000, r, c, -dc, dr}};

        for (auto [new_cost, nr, nc, ndr, ndc] : moves){
            if (!isValid(nr, nc, ROW, COL, grid)) continue;
            auto key = make_tuple(nr, nc, ndr, ndc);
            int lowest = lowest_cost.count(key) ? lowest_cost[key] : INT_MAX;

            if (new_cost > lowest) continue;

            if (new_cost < lowest) {
                backtrack[key] = {};
                lowest_cost[key] = new_cost;
            }

            backtrack[key].insert({r, c, dr, dc});
            pq.push({new_cost, nr, nc, ndr, ndc});
        }
    }

    // Perform backtracking BFS
    deque<tuple<int, int, int, int>> states(end_states.begin(), end_states.end());
    set<tuple<int, int, int, int>> seen(end_states.begin(), end_states.end());

    while (!states.empty()){
        auto key = states.front();
        states.pop_front();

        for (auto last : backtrack[key]) {
            if (seen.count(last)) continue;

            seen.insert(last);
            states.push_back(last);
        }
    }

    // Count unique (r, c) pairs in seen states
    set<pair<int, int>> unique_positions;
    for (const auto& [r, c, _, __] : seen){
        unique_positions.insert({r, c});
    }

    return unique_positions.size();
}

int main() {
    // Read input
    ifstream file{"input.txt"};
    string line;
    vector<vector<char>> grid;

    while (getline(file, line)){
        vector<char> row(line.begin(), line.end());
        grid.push_back(row);
    }

    file.close();

    
    auto [sr, sc] = findCoord(grid);
    cout << solve(grid, sr, sc) << '\n';

    return 0;
}
