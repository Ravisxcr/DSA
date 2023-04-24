#include<iostream>
#include<conio.h>

using namespace std;

void subarrary(int arr[],int n){
    for(int i=0; i<n; i++){
        for(int j=i; j<n; j++){
            for(int k=i; k<=j; k++){
                cout<<arr[k]<<" ";
            }
            cout<<endl;
        }
    }
}

int main(){

    system("cls");
    int arr[] = {10,20,30,40,50,60,70};
    int n = sizeof(arr)/sizeof(int);

    subarrary(arr,n);

    return -1;
}