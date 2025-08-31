"""encrypt or decrypt a message"""

def encrypt(message,key):
    result=""
    for char in message:
        if char.isalpha():
            base=ord("A") if char.isupper() else ord("a")
            shifted=(ord(char) - base + key)%26 + base   #imp
            result += chr(shifted)
        else:
            result += char
    return result

def decrypt(message,key):
    return encrypt(message,-key)        
      
print("Secret message program")

choice=input("Do you wnat to E or D: ").strip().lower() 

if choice == "e":
    text=input("Enter your message:")
    try:
        key=int(input("Enter a number between 1 and 25: "))
        encrypted=encrypt(text,key)
        print()
        print("Encryoted message: ",encrypted)
        print()
    except ValueError:
        print("Invalid error")
elif choice == "d":
    text=input("Enter your encrypted message: ")
    try:
        key=int(input("Enter a number between 1 and 25: "))
        decrypted=decrypt(text,key)
        print()
        print("Encryoted message: ",decrypted)
        print()
    except ValueError:
        print("Invalid error")        
        
else:
    print("Invlid choice")
    
            