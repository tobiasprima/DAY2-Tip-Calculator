print("Welcome to the Tip Calculator")
total = float(input("How much is the total bill?\n$"))
percentage = 1+float(input("How much is the tip percentage?\n"))/100
people = input("How many people to split the bill?")
end = round((total/people)*percentage,2)

print(f"Each person should pay ${end}")
