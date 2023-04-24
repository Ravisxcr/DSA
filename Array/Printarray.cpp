#include<iostream>
using namespace std;

void printarray(int arr[], int n){
    for(int i=0; i<n; i++){
        cout<<arr[i]<<" ";
    }
}

int main(){
    int arr[] = {10,20,30,40,50,60,70};
    int n = sizeof(arr)/sizeof(int);
    
    printarray(arr,n);
    return 0;
}