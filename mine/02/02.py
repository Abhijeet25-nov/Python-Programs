import csv
from datetime import datetime
import os
import requests

Filename="weather_logs.csv"
API_key="e8725ff73a079e5454ee2643505444f2"

if not os.path.exists(Filename):
    with open (Filename ,"w",newline="",encoding="utf-8" ) as f:
        writer=csv.writer(f)
        writer.writerow(["Date","City","Temperature","Condition"])
        
def log_weather():
   city_name = input("Enter your city name: ").strip()
   date = datetime.now().strftime("%Y-%m-%d")

   with open(Filename, "r", newline='', encoding="utf-8") as f:
      reader = csv.DictReader(f)
      for row in reader:
          if row["Date"] == date and row['City'].lower() == city_name.lower():
              print("Entry for this city and date exists")
              return
   try:
       url=f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_key}"
       response = requests.get(url)
       data = response.json()

       if response.status_code != 200:
           print(f"API Error ")
           return
       temp = data["main"]["temp"]
       condition = data["weather"][0]["main"]

       with open(Filename, "a", newline='', encoding="utf-8") as f:
           writer = csv.writer(f)
           writer.writerow([date, city_name.title(), temp, condition])
           print()
           print(f"Logged: {temp} {condition} in {city_name .title()} on {date}")
           print()
   except Exception as e:
       print("Failed to make API call")


def view_logs():
    with open(Filename, "r", encoding="utf-8") as f:
        reader = list(csv.reader(f))
        if len(reader) <=1:
            print("No Entries")
            return
        for row in reader[1:]:
            print("-------------------------")
            print(f"{row[0]} : {row[1]} : {row[2]} : {row[3]}")
            print("-------------------------")

def remove_data():
    with open(Filename, "w") as f:
        f.truncate(0)
    with open(Filename, "w", newline='', encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Date", "City", "Temperature", "Condition"])    
    print()        
    print("===========================================")        
    print("Truncated successfully")
    print("===========================================")
    print()  

def main():
    print()
    print("Welcome to Weather Repo Info")
    print()
    while True:
        print("Real time weather logger")
        print("1. Add weather log")
        print("2. View weather log")
        print("3. Truncate the file")
        print("4. Exit")

        choice = input("Choose an option: ").strip()

        match choice:
            case "1": log_weather()
            case "2": view_logs()
            case "3" : remove_data()
            case "4": break 
            case _ :  print("Invalid choice")
    print()        
    print("===========================================")        
    print("Thanking You for using this...!")
    print("===========================================") 



if __name__ == "__main__":
    main()


# city_name=""
# url=f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_key}"



