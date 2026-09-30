import csv
import json
infile = "student.csv"
outfile = "students.json"
stud = []
with open(infile, "r", newline="", encoding="utf-8") as file:
    rdr = csv.DictReader(file)
    for rec in rdr:
        stud.append(rec)
with open(outfile, "w", encoding="utf-8") as file:
    json.dump(stud, file, indent=4)
print("CSV file converted to JSON successfully!")
print("JSON file saved as:", outfile)
