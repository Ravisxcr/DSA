#include<iostream>
#include<conio.h>

using namespace std;

int binarysearch(int arr[],int n,int key){
    int s = 0;
    int e = n-1;
    
    while(s<=e){
        // Error in evaluating expression
        int mid = (s+e)/2;
        if (arr[mid]==key){
            return mid;
        }
        else if (key<arr[mid]){
            e = mid-1;
        }
        else if(key>arr[mid]){
            s = mid+1;
        }
    }
    if (s>e){
        return -1;
    }
}

int main(){
    system("cls");

    int arr[] = {10,20,30,40,50,60,70};
    int key;
    cin>>key;

    int n = sizeof(arr)/sizeof(int);

    int index = binarysearch(arr,n,key);

    if (index==-1){
        cout<<"Element not found";
    }
    else{
        cout<<"Element found at"<<index;
    }

    return 0;
}