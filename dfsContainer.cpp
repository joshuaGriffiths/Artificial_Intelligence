//
//  main.cpp
//  griffiths_ps1_ai
//
//  Created by Joshua Griffiths on 9/18/17.
//  Copyright © 2017 Joshua Griffiths. All rights reserved.
//

#include <iostream>

class can{
    
    public:
    
    int capacity;
    int currentLevel;
    

    
    can(int quartsCap, int quartsLev){
        
        capacity = quartsCap;
        currentLevel = quartsLev;
        
    }
    
    void Fill(){
        
        currentLevel = capacity;
    }
    
    void Empty(){
        currentLevel = 0;
    }
    
    bool isFull(){
        
        if(currentLevel >= capacity){
            
            return true;
        }
        
        else return false;
    }
    
    bool isEmpty(){
        
        if(currentLevel == 0){
            
            return true;
        }
        
        else return false;
    }
    
    int getState(){
        
        return currentLevel;
    }
    

    //Transfer contents from comesFrom into current can until current can is full.
    void makePour(can &comesFrom)
    {
        int oldFill = currentLevel;
        
        if(comesFrom.currentLevel > capacity){
            
            currentLevel = capacity;
            
        }
        
        else
        currentLevel = currentLevel + comesFrom.currentLevel;
        
        
        comesFrom.currentLevel = comesFrom.currentLevel - (currentLevel - oldFill);
    }
    
};

using namespace std;

int main(int argc, const char * argv[]) {
    
    can fortyQT_A = can(40, 40);
    can fortyQT_B = can(40, 40);
    can fourQT = can(4, 0);
    can fiveQT = can(5, 0);
    
    while ((fourQT.currentLevel =! 2) && (fiveQT.currentLevel =! 2)) {
        
        if (fourQT.isEmpty()){
            
            fourQT.makePour(fortyQT_A);
        }
        
        if (fiveQT.isEmpty()){
            
            fiveQT.makePour(fortyQT_A);
        }
        
        fortyQT_A.makePour(fiveQT);
        fiveQT.makePour(fourQT);
        fortyQT_A.makePour(<#can &comesFrom#>)
        
        
    }
    return 0;
}
