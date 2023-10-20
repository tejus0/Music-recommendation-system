#include<iostream>
using namespace std;
class A1
{
    public:
        A1()
        {
            int a=20;
            int b=35;
            int c;
            c=a+b;
            cout<<"Sum is:"<<c<< endl;
        }
};
 
class A2
{
    public:
        A2()
        {
            int x=50;
            int y=42;
            int z;
            z=x-y;
            cout<<"Difference is:"<<z<<endl;
        }
};
class A3
{
    public:
        A3()
        {
            int x=50;
            int y=42;
            int z;
            z=x-y;
            cout<<"ce is:"<<z<<endl;
        }
};
 
class S: public A1,public A3,public A2
{
    public:
        S()
        {
            int r=40;
            int s=8;
            int t;
            t=r*s;
            cout<<"Product is:"<<t<<endl;
        }
};
 
int main()
{
    S obj;
    return 0;
}