#include<cstdlib>
#include<iostream>
using namespace std;
int main(){
    cout << "hello world \n";
    int a=10;
    cout << a << endl;
    int* p=&a;
    cout << p << endl;
    int** z=&p;
    cout << z << endl;
    cout << *(*z);


}