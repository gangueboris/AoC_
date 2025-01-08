#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <unordered_map>
#include <utility>

using namespace std;

void printGrid(vector<vector<char>> grid, int y, int x) {
    //grid[y][x] = '@';
    for(int r = 0; r < grid.size(); ++r) {
        for(int c = 0; c < grid[0].size(); ++c){
            cout << grid[r][c];
        }
        cout << '\n';
    }
}
pair<vector<vector<char>>, string> getInput(ifstream& file) {
    string line; 
    vector<vector<char>> grid;
    string moves;
    while(getline(file, line)) {
        char dir = line[0];
        if(line[0] == '#') {
            stringstream ss{line};
            vector<char> temp;
            char c;
            while(ss >> c) {
                temp.push_back(c);
            }
                grid.push_back(temp);
        } else if(dir == '<' || dir == '>' || dir == '^' || dir == 'v') {
            stringstream ssLine{line};
            char ssc;
            while(ssLine >> ssc) moves += ssc;
        }
    }
    return make_pair(grid, moves);
}

pair<int, int> getStart(vector<vector<char>>& grid) {
    pair<int, int> start;
    for(int r = 0; r < grid.size(); ++r) {
        for (int c = 0; c < grid[0].size(); ++c){
            if(grid[r][c] == '@'){
                grid[r][c] = '.';
                return make_pair(r, c);
            }
        }
    }
    return start;
}

//int getResult(vector<vector<int>>& grid)
bool isValid(int H, int W, int r, int c) {
    return 0 <= r && r < H && 0 <= c && c < W;
}

pair<int, int> simulation(vector<vector<char>>& grid, unordered_map<char, pair<int, int>>& directions, char move, int cy, int cx) {
    auto [dr, dc] = directions[move];
    int nr = cy + dr, nc = cx + dc;
    int H = grid.size();
    int W = grid[0].size();
    
    if(!isValid(H, W, nr, nc)) return make_pair(cy, cx);

    // if is box, try pushing box
    int cr = cy, cc = cx;
    while(isValid(H, W, cr, cc)) {
        cr += dr;
        cc += dc;

        if(!isValid(H, W, cr, cc)) break;

        if(grid[cr][cc] == '#') break;

        if(grid[cr][cc] == '.') {
            grid[cr][cc] = 'O';
            grid[cy][cx] = '.';
            cy += dr;
            cx += dc;
            grid[cy][cx] = '@';
            break;
        }
    }
    return make_pair(cy, cx);
}

int main()
{
    // Get input
    ifstream file{"input.txt"};
    pair<vector<vector<char>>, string> output = getInput(file);
    vector<vector<char>> grid = output.first;
    string moves = output.second;
    //cout << moves << '\n';
    auto [y, x] = getStart(grid);
    unordered_map<char, pair<int, int>> directions = {{'>', {0, 1}}, {'<', {0, -1}}, {'^', {-1, 0}}, {'v', {1, 0}}};

    //printGrid(grid, y, x);
    // Run simulation
    int H = grid.size(); int W = grid[0].size();
    for(auto& move : moves) {
       auto[cy, cx] = simulation(grid, directions, move, y, x);
       y = cy;
       x = cx;
    }
    //printGrid(grid, y, x);

    int ans = 0;
    for(int r = 0; r < H; ++r) {
        for(int c = 0; c < W; ++c) {
            if(grid[r][c] == 'O') {
                ans += (100 * r + c);
            }
        }
    }


    cout << ans << '\n';   
    file.close();
    return EXIT_SUCCESS;
}
