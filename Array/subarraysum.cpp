#include<iostream>
#include<conio.h>

using namespace std;

void subarraysum(int arr[], int n){
    for(int i=0; i<n; i++){
        for(int j=i; j<n; j++){
            int sum=0;
            for(int k=i; k<=j; k++){
                sum += arr[k];
            }
            cout<<sum<<endl;
        }
    }
}

int main(){
    //system("cls");
    int arr[] = {10,20,30,40,50,60,70};
    int n = sizeof(arr)/sizeof(int);

    subarraysum(arr,n);

    return -1;
}