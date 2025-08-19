chai_size=input("Enter your chai size you want! s/m/l").lower()

print(f"User chooses :{chai_size} ")
if chai_size=="s":
    print("Price is Rs10")
elif chai_size=="m":
    print("Price is Rs15")
elif chai_size=="l":
    print("Price is Rs20")
    
else:
    print(f"{chai_size} is invalid input")           

    