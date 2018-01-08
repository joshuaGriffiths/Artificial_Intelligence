//Joshua Griffiths in colaberation with Dylan Gema
//PS2 Q 4

#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <cstdlib>


using namespace std;

const int numColors = 4;

struct Color
{
    Color(int red, int blue, int orange, int white)
    {
        colors[0] = red;
        colors[1] = blue;
        colors[2] = orange;
        colors[3] = white;
    }
    int colors[numColors];
};

const int numResults = 25;


int createResult(int placed, int misplaced){
    
    return placed*5 + misplaced;
}

int createMatch(const Color &arr1, const Color &arr2){
    
    int placed = 0, misplaced = 0;
    
    bool used1[4] = { false, false, false, false };
    bool used2[4] = { false, false, false, false };
    
    // first get placed
    
    for(int i=0; i<3; i++){
        
        if(arr1.colors[i] == arr2.colors[i]){
            
            used1[i] = true;
            used2[i] = true;
            placed++;
        }
    }
    
    // now get misplaced
    
    for(int i=0; i<3; i++){
        
        if(used1[i]){
            continue;
        }
        
        for(int j=0; j<4; j++){
            
            if(used2[j]){
                continue;
            }
            
            if(arr1.colors[i] == arr2.colors[j]){
                
                used1[i] = true;
                used2[j] = true;
                misplaced++;
            }
        }
    }
    
    return createResult(placed, misplaced);
}

int main()
{
    vector<Color> possibilities;
    
    for(int i0=0; i0<numColors; i0++)
        for(int i1=0; i1<numColors; i1++)
            for(int i2=0; i2<numColors; i2++)
                for(int i3=0; i3<numColors; i3++)
                    possibilities.push_back(Color(i0, i1, i2, i3));
    
    vector<Color> guessPossibilities = possibilities;
    
    while(true){
        
        int biggestGrouping = INT_MAX;
        
        vector<Color>::const_iterator best = guessPossibilities.end();
        
        for(vector<Color>::const_iterator ig = guessPossibilities.begin(); ig != guessPossibilities.end(); ++ig){
            
            vector<int> resultCounts(numResults, 0);
            
            for(vector<Color>::const_iterator ip = possibilities.begin(); ip != possibilities.end();++ip){
                
                resultCounts[createMatch(*ig, *ip)]++;
            }
            
            int guessBiggestGrouping = *max_element(resultCounts.begin(), resultCounts.end());
            
            if(guessBiggestGrouping < biggestGrouping){
                
                biggestGrouping = guessBiggestGrouping;
                best = ig;
            }
        }
        
        
        
        string xs = "";
        cout << "Guess: "
        << best->colors[0] << " "
        << best->colors[1] << " "
        << best->colors[2] << " \n"
        << "Enter Xs or [nothing]:";
        cin >> xs;
        
        int placed, misplaced;
        string os = "";
        if(xs == "nothing"){
            placed = 0;
        }
        if (xs.length() == 1){
            placed = 1;
        }
        if (xs.length() == 2){
            placed = 2;
        }
        if (xs.length() == 3){
            placed = 3;
        }
        if (xs.length() == 4){
            placed = 4;
        }
        
        cout << "Enter Os or [nothing]:";
        cin >> os;
        
        if(os == "nothing"){
            misplaced = 0;
        }
        if (os.length() == 1){
            misplaced = 1;
        }
        if (os.length() == 2){
            misplaced = 2;
        }
        if (os.length() == 3){
            misplaced = 3;
        }
        if (os.length() == 4){
            misplaced = 4;
        }
        
        int result = createResult(placed, misplaced);
        
        for(vector<Color>::iterator ip = possibilities.begin();
            ip != possibilities.end();){
            
            if(result != createMatch(*best, *ip)){
                
                ip = possibilities.erase(ip);
            }
            else{
                
                ++ip;
            }
        }
        
        if(possibilities.size() == 0){
            
            cout << "You have done something wrong!\n";
            exit(1);
        }
        
        if(possibilities.size() == 1){
            
            cout << "Final guess: \n"
            << possibilities.begin()->colors[0] << ", "
            << possibilities.begin()->colors[1] << ", "
            << possibilities.begin()->colors[2] << "!\n";
            exit(0);
        }
    }
}
