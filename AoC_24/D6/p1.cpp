#include <iostream>
#include <sstream>
#include <fstream>
#include <vector>
#include <set>

using namespace std;

#include <set>

struct Coord {
    int x, y;

    // Define the comparison operator for set
    bool operator<(const Coord& other) const {
        return (x < other.x) || (x == other.x && y < other.y);
    }
};


int main(){
    ifstream file{"input.txt"};
    if(!file){
        cout << "Can't open the file !! \n";
    }

    string line = "\n";
    vector<string> grid;
    while(file >> line){
       grid.push_back(line);
    }

    int r = 0;
    int c = 0;
    set<Coord> visited;

    for(int i = 0; i < grid.size(); ++i) {
        for(int j = 0; j < grid[i].length(); ++j) {
            if(grid[i][j] != '#' && grid[i][j] != '.') {
                r = i;
                c = j;
            }
        }
    }
    int rdir = -1;
    int cdir = 0;
    string move = "top";
   
    while((r >= 0 && r < grid.size()) && (c >= 0 &&  c < grid[0].length())){
        visited.insert({r, c});
        
        if(r - 1 >= 0 && grid[r-1][c] == '#' && move == "top"){
            rdir = 0;
            cdir = 1;
            move = "right";
        }
        else if(c + 1 < grid[0].length() && grid[r][c + 1] == '#' && move == "right"){
            rdir  = 1;
            cdir = 0;
            move = "bottom";
        }
        else if(r + 1 < grid.size() && grid[r + 1][c] == '#' && move == "bottom"){
            rdir = 0;
            cdir = -1;
            move = "left";
        }
        else if(c - 1 >= 0 && grid[r][c - 1] == '#' && move == "left"){
            rdir = -1;
            cdir = 0;
            move =  "top";
        }else{
            r += rdir;
            c += cdir;
        }
        
    }
    cout << visited.size() << '\n';
    file.close();
   return EXIT_SUCCESS;
}