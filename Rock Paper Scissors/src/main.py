#!/usr/bin/env python3

import random

print("Hi, welcome to Rock Paper Scissors!")
print("Lets play!")

while True:
   user_choice = input("Options:\n\tRock\n\tPaper\n\tScissor\nSelection: ").lower()
   
   options=["rock","paper","scissor"]
   
   if user_choice not in options:
      print("Invalid selection!")
      continue

   computer_choice = random.choice(options)

   print("You chose:", user_choice)
   print("Computer chose:", computer_choice)

   print("\n")

   if user_choice == computer_choice:
      print("It's a tie!")
   elif user_choice == "rock" and computer_choice == "scissor":
      print("\033[92mYou win!\033[0m")
   elif user_choice == "rock" and computer_choice == "paper":
      print("\033[91mYou lose!\033[0m")
   elif user_choice == "paper" and computer_choice == "rock":
      print("\033[92mYou win!\033[0m")
   elif user_choice == "paper" and computer_choice == "scissor":
      print("\033[91mYou lose!\033[0m")
   elif user_choice == "scissor" and computer_choice == "paper":
      print("\033[92mYou win!\033[0m")
   elif user_choice == "scissor" and computer_choice == "rock":
      print("\033[91mYou lose!\033[0m")
   else:
      print("Invalid selection!")

   print("\n")
   
   play_again = input("Play again? (y/n): ").lower()

   if play_again == "n":
      break

print("Thanks for playing!")
print("Have a great day!")
