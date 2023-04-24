#include<iostream>
#include<conio.h>

using namespace std;

void reverse(int arr[], int n){
    int s=0;
    int e=n-1;

    while(s<e){
        swap(arr[s],arr[e]);
        s += 1;
        e -= 1;
    }

}

void printarray(int arr[], int n){
    for(int i=0; i<n; i++){
        cout<<arr[i]<<" ";
    }
}

int main(){
    int arr[] = {10,20,30,40,50,60,70};
    int n;

    n = sizeof(arr)/sizeof(int);

    reverse(arr,n);
    printarray(arr,n);

    return 0;
}