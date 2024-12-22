#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <utility>
#include <set>
#include <queue>
#include <tuple>
using namespace std;

pair<int, int> findCoord(const vector<vector<char>>& grid){
    for(int r = 0; r < grid.size(); ++r){
        for(int c = 0; c < grid[0].size(); ++c){
            if(grid[r][c] == 'S'){
                return pair<int, int>{r, c};
            }
        }
    }
    return make_pair(0, 0);
}

bool isValid(int r, int c, int ROW, int COL, const vector<vector<char>>& grid) {
    return 0 <= r && r < ROW && 0 <= c && c < COL && grid[r][c] != '#';
}

// BFS to find the shortest path
int solve(const vector<vector<char>>& grid, int sr, int sc) {
    priority_queue<tuple<int, int, int, int, int>, vector<tuple<int, int, int, int, int>>, greater<>> pq;
    set<tuple<int, int, int, int>> seen;

    pq.push({0, sr, sc, 0, 1});  // (cost, row, col, dr, dc)
    seen.insert({sr, sc, 0, 1}); 

    while(!pq.empty()){
        int ROW = grid.size();
        int COL = grid[0].size();
        auto [cost, r, c, dr, dc] = pq.top();

        pq.pop();
        seen.insert({r, c, dr, dc});

        if (grid[r][c] == 'E'){
            return cost;
        }

        vector<tuple<int, int, int, int, int>> moves = {{cost + 1, r + dr, c + dc, dr, dc}, {cost + 1000, r, c, dc, -dr}, {cost + 1000, r, c, -dc, dr}};
        for (auto [new_cost, nr, nc, ndr, ndc] : moves) {
            if(!isValid(nr, nc, ROW, COL, grid) || seen.count({nr, nc, ndr, ndc})) continue;
            pq.push({new_cost, nr, nc, ndr, ndc});
           
        }
    }

    return -1;
}


int main()
{
    // Read input
    ifstream file{"input.txt"};
    string line;
    
    vector<vector<char>> grid;
    while(getline(file, line)){
        vector<char> temp;
        char c;
        stringstream ss{line};
        while(ss >> c){
            temp.push_back(c);
        }

        grid.push_back(temp); 
    }

    auto [sr, sc] = findCoord(grid);
    cout << solve(grid, sr, sc) << '\n';
   
   

    file.close();
    return EXIT_SUCCESS;
}