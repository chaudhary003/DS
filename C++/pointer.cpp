#include<iostream>
#include<cstdlib>
using namespace std;
enum Day{SUN,MON,TUE,WED,THUR,FRI,SAT};
int multiply(int a, int b);
int main(){
  char a='x';
  char* p=&a;
  cout << p << endl;
  cout << *p << endl;
  *p='u';
  int x,y,z;
  cout << a << '\n';
  cin >> x;
  cin >> y;
  z=multiply(x,y);
  cout << "value after multiply is " << z << '\n';
  Day today=TUE;
  cout << today;
  return 0;
}
int multiply(int x,int y){
  return x*y;
}
