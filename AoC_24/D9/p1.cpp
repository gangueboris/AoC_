#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
using namespace std;

int main()
{
    ifstream file{"input.txt"};
    string line;
    vector<int> process;
    int index = 0;
    while(getline(file, line)){
        stringstream ss{line};
        char c;
        int i = 0;
        int index = 0;
        while(ss >> c){
            int x = static_cast<int>(c - '0');
            if(!(i % 2)){
                for(int k = 0; k < x ; ++k){
                    process.push_back(index);
                }
                index++;  
            }else{
                for(int k = 0; k < x ; ++k){
                    process.push_back(-1);
                }  
            }
            i++;
        }
    }

    int r = process.size() - 1;
    for(int l = 0; l < process.size(); ++l){
       if( l <= r && process[l] == -1){
          while(process[r] == -1){r--;}

          process[l] = process[r];
          process[r] = -1;
       }
    }
    process[r] = process[r + 1];
    process[r + 1] = -1;

    long int res = 0;
    for(int k = 0; k < process.size(); ++k){
        if(process[k] == -1) break;
       res += k * process[k];
    } 
    cout << res << '\n';

    file.close();
    return EXIT_SUCCESS;
}