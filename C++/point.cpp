#include<iostream>
#include<cstdlib>
using namespace std;
void printadd(int x,int y);
int main(){
    int a,b;
    cin >> a;
    cin >> b;
    printadd(a,b);
    return 0;

}
void printadd(int x,int y){
    int z=0;
    z=x;
    int* p=&z;
    cout << "value of x is " << x << '\n'; 
    cout << "value at address p is " << *p <<'\n';
    cout << "value of z is " << z << '\n'; 
    //x++;   or x=x+1 
    x=x++;
    cout << "value of x is after change" << x << '\n'; 
    cout << "value at address p is after change " << *p <<'\n';
    cout << "value of z is " << z << '\n'; 
}