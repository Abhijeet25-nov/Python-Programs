def get_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("X Please enter a valid number.")


num_people=int(input("How many people are there in the group :"))
names=[]

for i in range(num_people):
    name=input(f"Enter the name of person #{i+1}: ").strip()
    names.append(name)


total_bill =get_float("ENter the bill amount in number only: ")

share= round(total_bill / num_people)

print("\n"+"*"*40)
print(f"Total bill: {total_bill}")
print(f"Each person bill: {share}")


for name in names:
    print(f"{name} owes {share} rupees")

print("\n"+"*"*40)
