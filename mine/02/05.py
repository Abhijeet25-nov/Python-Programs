import json
import csv
import os

Input_file="weather_logs.csv"
Output_file="converted_Data_json.json"

def load_data(filename):
    if not os.path.exists(filename):
        print("No csv file is there")
        return []
    
    with open(filename,'r',encoding="utf-8") as f:
        reader=csv.DictReader(f)
        data=list(reader)
        return data
    
def save_as_json(data,file):
    if not data:
        return("No data found")
    
    with open(file,'w',encoding="utf-8") as f:
        return json.dump(data,f,indent=2)
    print(f"✅ converted {len(data)} records to {file}")
    
def preview_file(data,count=4):
    for row in data:
        print(json.dumps(row,indent=2))
    print("=================================================================")    

def main():
    data=load_data(Input_file)
    save_as_json(data,Output_file)
    preview_file(data)
    
if __name__=="__main__":   
    main()     