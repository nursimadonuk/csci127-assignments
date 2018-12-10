#include<iostream>
#include<math.h>

int discriminant(int a, int b, int c){
  int d = (b*b)-(4*a*c);
  std::cout<< "a = " << a << " b = " << b << " c = " << c << "\n";
  std::cout<< "the discriminant is " <<  d << "\n";
  return 0;
}

int quadsolve(int a, int b, int c){
  int d;
  d = (b*b)-(4*a*c);
  int answer;
  if (d >= 0){
    answer = (-b + sqrt(d))/(2*a);
  }
    else{
      answer = 0;
    }
  std::cout<< "the answer is " << answer << "\n ";
  return 0;
}

int main()
{
  int disc;
  int quad;
  disc = discriminant(1,0,-25);
  quad = quadsolve(1,0,-25);
  int disc2;
  int quad2;
  disc2 = discriminant(1,18,81);
  quad2 = quadsolve(1,18,81);
  
  return 0;
}



