#include<iostream>

int sumofsquares(int a, int b){
  int sum;
  std::cout<<"a = " << a << " b = " << b << "\n";
  while (b >= a){
    sum = sum + (a*a);
    a++;
  }
  std::cout<< sum << "\n";
  return 0;

}
int main()
{
  int sum;
  sum = sumofsquares(5,10);
  return 0;
}
