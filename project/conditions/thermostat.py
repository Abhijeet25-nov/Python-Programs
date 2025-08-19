device_status=True
temp=float(input("enter the temp"))
if device_status:
    print("device is active!")
    if temp > 35:
        print("warm temp")
    else:
        print("Temp noraml")    
        
else:
    print("Device is offline")    
    