#include <iostream>
#include <sstream>
#include <fstream>
#include <vector>
#include <set>
#include<utility>
#include <queue>
#include <algorithm>
using namespace std;

/*
 Today problem is a graph problem, connected components
 I will use flood fill algorithm
*/

bool isValid(int r, int c, int ROW, int COL, const vector<vector<char>>& grid, const set<pair<int, int>>& visited, char elem){
    return 0 <= r && r < ROW && 0 <= c && c < COL && grid[r][c] == elem && !visited.count({r, c}); 
}

int findPerimeter(vector<pair<int, int>>& region){
    int perimeter = 0;
        for(auto& [r, c] : region){
            perimeter += 4;
            for(auto [nr, nc] : initializer_list<pair<int, int>>{{r + 1, c}, {r - 1, c}, {r, c + 1},{r, c - 1}}){
                if(find(region.begin(), region.end(), make_pair(nr, nc)) != region.end()){
                    perimeter -= 1;
                }
            }
        }
    return perimeter;
}
int main(void){
    fstream file{"input.txt"};
    vector<vector<char>> grid;
    string line;
    while(getline(file, line)){
        char c;
        vector<char> temp;
        stringstream ss{line};
        while (ss >> c) temp.push_back(c);
        grid.push_back(temp);   
    }
    vector<vector<pair<int, int>>> regions;
    set<pair<int, int>> visited;
    queue<pair<int, int>> q;
    int ROW = grid.size();
    int COL = grid[0].size();

    // Apply flood fill
    for(int r = 0; r < ROW; ++r){
        for(int c = 0; c < COL; ++c){
            if(visited.count({r, c})) continue;
            visited.emplace(r, c);
            q.emplace(r, c);
            vector<pair<int, int>> region;
            region.emplace_back(r, c);
            char elem = grid[r][c];

            while(!q.empty())
            {
                auto [r, c] = q.front();
                q.pop();
                for(auto [nr, nc] : initializer_list<pair<int, int>>{{r + 1, c}, {r - 1, c}, {r, c + 1}, {r, c},{r, c - 1}}){
                    if(!isValid(nr, nc, ROW, COL, grid, visited, elem)) continue;
                    q.emplace(nr, nc);
                    visited.emplace(nr, nc);
                    region.emplace_back(nr, nc); 
                }
            }
            regions.push_back(region);
        }
    }
    int res = 0;

    for(auto& region: regions){
       res += region.size() * findPerimeter(region);
    }
    cout << res << '\n';




    file.close();
    return EXIT_SUCCESS;
}