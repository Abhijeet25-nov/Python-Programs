import json 
import csv
import os

Input_file="api_data.json"
Output_data="converted_data.csv"

def load_data(filename):
    if not os.path.exists(filename):
        print("No file exists")
        return []
    
    with open(filename,"r",encoding="utf-8") as f:
        try:
            return json.load(f)
        except:
            print("Invalid Json format")
     
            
def convert_into_csv(data, output_file):
    if not data:
        print("No data found")
        return
        
    fieldname=list(data[0].keys())    
    
    with open(output_file,"w",encoding="utf-8") as f: 
        writer=csv.DictWriter(f, fieldnames=fieldname)
        writer.writeheader()
        for record in data:
            writer.writerow(record)
            
    print(f"Converted {len(data)} records to {output_file}") 
    
def main():
    print("Converting Json to csv..") 
    data = load_data(Input_file)  #data is fetched from json file
    convert_into_csv(data, Output_data)          
                           
if __name__=="__main__":
    main()