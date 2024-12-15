#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <unordered_map>
#include <utility>
#include <set>

using namespace std;

unordered_map<int, vector<pair<int, int>>> findPositions(const vector<vector<int>>& grid){
    unordered_map<int, vector<pair<int, int>>> mapping;
    for(int r = 0; r < grid.size(); ++r){
        for(int c = 0; c < grid[0].size(); ++c){
            if(grid[r][c] == 0){
                mapping[0].push_back({r, c});
            }
        }
    }
    return mapping;
}
bool isValid(int const& r, int const& c, int const& ROW, int const& COL){
    return 0 <= r && r < ROW && 0 <= c && c < COL;
}


int countPath(vector<vector<int>> const& grid, set<pair<int, int>> seen, int sr, int sc, int count = 0){
    if(grid[sr][sc] == 9 && seen.find({sr, sc}) == seen.end()){
        seen.insert({sr, sc});
        return ++count;
    }

    for(auto& [cr, cc] : initializer_list<pair<int, int>>{{sr + 1, sc}, {sr - 1, sc}, {sr, sc + 1}, {sr, sc - 1}}){
        if(isValid(cr, cc, grid.size(),  grid[0].size()) && grid[cr][cc] == grid[sr][sc] + 1){
           count = countPath(grid, seen, cr, cc, count);
        }
    }
    return count;   
}

int main(){

    // Read input
    ifstream file{"input.txt"};
    string line;
    vector<vector<int>> grid;

    while(getline(file, line)){
        vector<int> temp;
        stringstream ss{line};
        char c;
        while(ss >> c){
            int n = c - '0';
            temp.push_back(n);
        }
        grid.push_back(temp); 
    }

    unordered_map<int, vector<pair<int, int>>> mapping = findPositions(grid);
    
    int res = 0;
    set<pair<int, int>> seen;
    for(auto const& [sr, sc] : mapping[0]){
        res += countPath(grid, seen, sr, sc);
    }

    cout << res << '\n';


    file.close();
    return EXIT_SUCCESS;
}