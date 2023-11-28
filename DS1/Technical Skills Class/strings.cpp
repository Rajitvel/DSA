#include <iostream>
#include <string>

using namespace std;

int main(){
    string input;
    cin >> input;
    string

    int upper=0,lower=0;
    for(int i=0; i<input.length(); i++){
        if(input[i]=='A' && input[i]<='Z'){
            upper++;
        }
        else if (input[i]>='a' && input[i]<='z'){
            lower++;
        }
        if(upper>lower){
            cout << toupper(input[i]) <<endl;
        }

        else if (lower>upper || lower==upper)
        {
            cout << tolower(input[i]) << endl;
        }
    }
    
    return 0;
}