#MadLib.py
#Name: Jacob Cargile
#Date: 8/30/2024
#Assignment: MadLib

def main():
  print("Madlib")
  #Ask user for words
  noun1 = input("Enter your name:")
  noun2 = input("Enter what sauce or condiment you would use:")
  noun3 = input("What type of meat would you like:")
  noun4 = input("1st topping for you sandwich:")
  noun5 = input("2nd topping for your sandwich:")
  noun6 = input("WHat type of bread would you like for your sandwich:")
  #Print the story with the user supplied words.
  print("If I," , noun1 , ",were going to make a sandwich I would add" , noun2 , "to my bread, and use" , noun3 , "as my meat." )
  print("I would also add" , noun4 , "and" , noun5 , "as extra toppings to finish it off. Of course the most important part is the bread and I would choose" , noun6 , ".")

#Call the main function if this is the file being run.
if __name__ == '__main__':
    main()
