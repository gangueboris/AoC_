#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <unordered_map>
using namespace std;

long findStones(long n, int iter, unordered_map<string, long>& memo){
    string key = to_string(n) + '-' + to_string(iter);
    if(memo.find(key) != memo.end())
    {
        return memo[key];
    }
    
    long res = 0;
    if(iter == 0){
        res = 1;
    }else if(n == 0){
       res = findStones(1, iter - 1, memo);
    }else if(to_string(n).length() % 2 == 0){
        string n_string = to_string(n);
        string left = "0";
        string right = "0";
        for(int k = 0; k < n_string.length(); ++k){
            if(k < n_string.length() / 2) left += n_string[k];
            else right += n_string[k];
        }
        res =  findStones(stol(left), iter - 1, memo) +  findStones(stol(right), iter - 1, memo);
    }else{
        res =  findStones(n * 2024, iter - 1, memo);
    }
    memo[key] = res;
    return res;
}

int main()
{
    // Read input
    ifstream file{"input.txt"};
    string line;
    vector<long> stones;
    while(getline(file, line)){
        stringstream ss{line};
        string ch;
        while(ss >> ch){
           stones.push_back(stoi(ch));
        } 
    }
    
    const int iter = 75;
    unordered_map<string, long> memo;
    long res = 0;
    for(auto n : stones){
       res += findStones(n, iter, memo);
    }

    cout << res << '\n';

    file.close();
    return EXIT_SUCCESS;
}