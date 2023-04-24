#include<iostream>
#include<conio.h>

using namespace std;

void bubblesort(int arr[], int n){
    int temp=0;
    for(int i=0; i<n; i++){
        for(int j=0; j<n-i; j++){
            if(arr[j]>arr[j+1]){
                temp = arr[j];
                arr[j] = arr[j+1];
                arr[j+1] = temp;
            }
        }
    }
}

int main(){
    int arr[] = {80,70,60,50,40,30,20,10};
    int n = sizeof(arr)/sizeof(int);

    bubblesort(arr,n);

    cout<<n<<endl;

    for(int i=0; i<n; i++){
        cout<<arr[i]<<",";
    }
    
    return 0;
}