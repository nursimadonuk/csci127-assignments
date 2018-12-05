#include<iostream>
#include<random>
#include<cstdlib>
#include<ctime>


int main(){
 //establish the computers number
 srand(time(NULL));
 int answer = rand() %100;
 std::cout << answer << "\n";

 // repeat until the answer is guessed
 int guess;
 std::cout<<"Please enter a guess"<<"\n";
 std::cin >> guess;
 int guesses = 1;
 while (guess != answer){
  if (guess > answer){
   std::cout<< "You guessed too high\n";
  }else if (guess < answer){
    std::cout<< "You guessed too low \n";
  }
 std::cout<<"Pleas enter a guess"<<"\n";
 std::cin>> guess;
 guesses++;
 }

 std::cout<<"Congragulations you have guessed the number!!";
 std::cout<<"It took you "<< guesses << " guesses.\n";
 //get a guess from the user
 //see if the guess is too low/high just right

  
 return 0;
}


 
