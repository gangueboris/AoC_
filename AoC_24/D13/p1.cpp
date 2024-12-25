#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <utility>
#include <algorithm>

using namespace std;


int solve(pair<int, int>& a, pair<int, int>& b, pair<int, int>& prize){
    int px = prize.first;
    int py = prize.second;
    int ax = a.first;
    int ay = a.second;
    int bx = b.first;
    int by = b.second;
    const int inf = 999999999;
    int minCost = inf;
   for(int i = 0; i <= 100; ++i){
    for(int j = 0; j <= 100; ++j){
        if(ax * i + bx * j == px && ay * i + by * j == py){
           minCost = min(minCost, 3* i + j);
        }
    }
   }
  return minCost != inf ? minCost : 0;
}
int main(){
    fstream file{"input.txt"};
    vector<pair<int, int>> A;
    vector<pair<int, int>> B;
    vector<pair<int, int>> prizes;
    
    string line;
    while (getline(file, line)){
        int x, y;
        if (line.find("Button A:") != string::npos){
            sscanf(line.c_str(), "Button A: X+%d, Y+%d", &x, &y);
            A.emplace_back(x, y);
        }
      
        else if (line.find("Button B:") != string::npos){
            sscanf(line.c_str(), "Button B: X+%d, Y+%d", &x, &y);
            B.emplace_back(x, y);
        }
      
        else if (line.find("Prize:") != string::npos){
            sscanf(line.c_str(), "Prize: X=%d, Y=%d", &x, &y);
            prizes.emplace_back(x, y);
        }
    }
    
    int res = 0;
   for(int i = 0; i < A.size(); ++i){
       res += solve(A[i], B[i], prizes[i]);
   }
 
 
    cout << res << '\n';


    file.close();
    return EXIT_SUCCESS;
}