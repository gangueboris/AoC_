#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
#include <utility>
using namespace std;

bool backTrack(const vector<long>& values, int index, long current, long key){
    if(index == values.size()){
        return current == key;
    }
    if(backTrack(values, index + 1, current + values[index], key)){
        return true;
    }
     if(backTrack(values, index + 1, current * values[index], key)){
        return true;
    }
    return false;

}

int main(){
    ifstream file{"input.txt"};
    if (!file){
        cerr << "File can't be opened!\n";
        return 1;
    }

    string line;
    vector<pair<long, vector<long>>> content;

    while (getline(file, line)){
        stringstream ss{line};
        long total, value;
        char colon;

        ss >> total >> colon;

        vector<long> values;
        while (ss >> value){
            values.push_back(value);
        }
        content.emplace_back(total, values);
    }
    
    long ans = 0;

    for (const auto& [key, values] : content){
       if(backTrack(values, 1, values[0], key)){
          ans += key;
       }
    }

    cout << ans << '\n';

    return 0;
}
