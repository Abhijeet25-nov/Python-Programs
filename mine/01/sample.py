import csv
import os
FILENAME = "contacts.csv"

if not os.path.exists(FILENAME):
    with open(FILENAME, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Name", "Phone", "Email"])
        
with open(FILENAME, 'r', encoding="utf-8") as f:
        reader = csv.DictReader(f)
        rows = list(reader)
        print((rows))
        # if len(rows) < 1:
        #     print("No contacts found")
        
        # print("\n Your contacts: \n")

        # for row in rows[1:]:
        #     print(f"{row[0]} | {row[1]} | {row[2]}")
        # print()