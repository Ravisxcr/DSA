#include<iostream>
using namespace std;

int main(){
    int marks[100];
    int n;
    cin>>n;

    cout<<"Input Block";
    for(int i =0; i<n; i++){
        cin>>marks[i];
    }

    cout<<"Output Array";
    for(int i = 0; i<n; i++){
        cout<<marks[i]<<",";
    }

    return 0;
}