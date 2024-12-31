#include <iostream>
#include <sstream>
#include <fstream>
#include <vector>
#include <utility>

using namespace std;

int main (){
    ifstream file("input.txt");
    string line;
    vector<pair<int, int>> finalPositions;
    const int H = 103;
    const int W = 101;
    const int iter = 100;

    while(getline(file, line)){
        int x, y, vx, vy;
        sscanf(line.c_str(), "p=%d,%d v=%d,%d", &x, &y, &vx, &vy);
        int endx = (x + iter * vx) % W;
        int endy = (y + iter * vy) % H;
        finalPositions.emplace_back(endx, endy);
    }
  
    int midW = W / 2;
    int midH = H / 2;
    int tl = 0, tr = 0, bl = 0, br = 0;
    for(auto&[x, y] : finalPositions){
        if(x == midW || y == midH) continue;
        if(x < midW){
            if(y < midH) tl++;
            else bl++;
        }else{
            if(y < midH) tr++;
            else br++;
        }
    }

    int res = tl * tr * bl * br;
    cout << res << endl;   




    file.close();
    return EXIT_SUCCESS;
}