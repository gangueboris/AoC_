#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>

using namespace std;


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
    const int iter = 25;
    for(int i = 0; i < iter; ++i){
        vector<long> temp;
        for(auto& n : stones){
            if(n == 0){
                temp.push_back(1);
            }else if(to_string(n).length() % 2 == 0){
                string n_string = to_string(n);
                string left = "0";
                string right = "0";
                for(int k = 0; k < n_string.length(); ++k){
                    if(k < n_string.length() / 2) left += n_string[k];
                    else right += n_string[k];
                }
                temp.push_back(stoi(left));
                temp.push_back(stoi(right));
            }else{
                temp.push_back(n * 2024);
            }

        }
        stones = temp;
    }
    /*for(auto &n : stones){
        cout << n <<  " ";
    }
    cout << '\n';*/
    cout << stones.size() << '\n';

    file.close();
    return EXIT_SUCCESS;
}