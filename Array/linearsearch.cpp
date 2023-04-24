#include<iostream>
#include<conio.h>
using namespace std;

int linearsearch(int arr[], int n , int key){
    for(int i=0; i<n; i++){
        if(arr[i]==key){
            return i;
        }
    }
    return -1;
}

int main(){
    system("cls");
    cout<<"Linear Search \n";
    int arr[] = {10,20,30,40,50,60,70};
    int n = sizeof(arr)/sizeof(int);

    int key ;
    cin>>key ;

    int index = linearsearch(arr,n,key);

    if(index==-1){
        cout<<"Element not found";
    }
    else{
        cout<<"Element found at "<<index;
    }


    return 0;
}