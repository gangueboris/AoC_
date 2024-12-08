#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <cmath>
#include <algorithm>

using namespace std;

int main()
{

    ifstream file{"input.txt"};
    vector<int> Lrecord;
    vector<int> Rrecord;

    if(!file){
        cout << "Can't open file !" << "\n";
        exit(1);
    }
    string line;
    while(getline(file, line)){
        int f_space = line.find_first_of("   ");
        int l_space = line.find_last_of("   ");
        int a = atoi(line.substr(0, f_space).c_str());
        int b = atoi(line.substr(l_space, line.length()).c_str());
        Lrecord.push_back(a);
        Rrecord.push_back(b);    
    }
    sort(Lrecord.begin(), Lrecord.end());
    sort(Rrecord.begin(), Rrecord.end());
    
    int total = 0;
    for(int k = 0; k < Lrecord.size(); ++k){
        total += abs(Lrecord[k] - Rrecord[k]);
    }
    
    cout << total << '\n';


    file.close();
    return EXIT_SUCCESS;
}