#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>

using namespace std;

int main()
{
    // Read file 
    ifstream file{"input.txt"};
    string line;
    vector<int> disks;
    while (getline(file, line))
    {
       stringstream ss{line};
       char c;
       int i = 0;
       int index = 0;
       
       // Process the input
       while(ss >> c){
           int x = c - '0';
          if(!(i % 2)){
                for(int j = 0; j < x; ++j){
                    disks.push_back(index);
                }
                index++;
            }else{
                 for(int j = 0; j < x; ++j){
                    disks.push_back(-1);
                }
            }
          i++;
       }
    }
    int right = disks.size() - 1;
     // While we can move any block
    while (right > 0){
        // Find start of disk from the end
        while (right > 0 && disks[right] == -1){
            right--;
        }

        // Find block length
        int file_size = 0;
        int file_type = disks[right];
        while (right - file_size >= 0 && disks[right - file_size] == file_type){
            file_size++;
        }

        // Lookup the suitable free blocks
        int left = 0;
        while(left < right){

            // Find the start point of a free space
            while(disks[left] != -1 && left < right){
                left++;
            }
            if(left < right){
                // Find free block size
                int free_size = 0;
                while(left + free_size < right && disks[left + free_size] == -1){
                    free_size++;
                }

                // If there is enough space
                if(free_size >= file_size){
                    for(int i = 0; i < file_size; ++i){
                        disks[left + i] = file_type;
                    }
                    for(int i = 0; i < file_size; ++i){
                        disks[right - i] = -1;
                    }
                    // Go to the end
                    left = right + 1; 
                }else{
                    left += free_size;
                }
            }

        }
        right -= file_size;
    }

    long res = 0;
    for(int i = 0; i < disks.size(); ++i){
        if(disks[i] != -1){
            res += disks[i] * i;
        }
    }
    cout << res <<'\n';

    file.close();
    return EXIT_SUCCESS;
}