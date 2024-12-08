#include <iostream>
#include <sstream>
#include <fstream>
#include <vector>

using namespace std;

bool asc(vector<int> line){
    bool checked = true;
    for(int i = 0; i < line.size() - 1; ++i){
        int diff = line[i + 1] - line[i];
        if(line[i] > line[i + 1] || diff < 1 || diff > 3){
            checked = false;
            break;
        }
    }
    return checked;
}

bool desc(vector<int> line){
    bool checked = true;
    for(int i = 0; i < line.size() - 1; ++i){
        int diff = line[i] - line[i + 1];
        if(line[i] < line[i + 1] || diff < 1 || diff > 3){
            checked = false;
            break;
        }
    }
    return checked;
}

bool unsafeTrue(vector<int> line){
   
    for(int i = 0; i < line.size(); ++i){
        vector<int> copy{line};
        copy.erase(copy.begin() + i);
        if(asc(copy) || desc(copy)){
            return true;
        }
    }
    return false;
}
int main()
{
    int count = 0;
    ifstream file{"input.txt"};
    if(!file){
        cout << "Can't read file !!! \n";
        exit(0);
    }

    string line;
    int n;
    while(getline(file, line)){
        vector<int> line_arr;
        istringstream iss{line};
        while(iss >> n){
            line_arr.push_back(n);
        }
        if(asc(line_arr)){
            count++;
        }
        else if(desc(line_arr)){
            count++;
        }else{
            if (unsafeTrue(line_arr)){
                count++;
            }
        }
    }
    cout << count << "\n";

    file.close();
    return EXIT_SUCCESS;
}
