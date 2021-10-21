#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪
#HINT 1: https://www.google.com/search?q=how+to+round+number+to+2+decimal+places+python&oq=how+to+round+number+to+2+decimal
#HINT 2: https://www.kite.com/python/answers/how-to-limit-a-float-to-two-decimal-places-in-python
print("Welcome to the tip calculcator!")

total = input("What is the total bill? \n")

tip = input("\nWhat percent tip would you like to give? \n")

people = input("\nHow many people will split the bill? \n")

final = round(( float(total) + (float(total) * (int(tip)/100)) ) / int(people), 2)

print(f"\nEach person should pay {final} dollars.")