import csv
data = [
    ["sid", "sname", "salary"],
    [1, "jay", 3800],
    [2, "om", 4000],  
    [3, "sahu", 4500],
    [4, "hiren", 4100],
    [5, "sai", 4200]   
]
with open('salary.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(data)
s_names = 0
total_records = 0
with open('salary.csv', 'r') as f:
    reader = csv.reader(f)
    header = next(reader)  
    for row in reader:
        total_records += 1
        sid, sname, salary = row
        if sname.startswith("s") or sname.startswith("S"):
            print(f"{sid},{sname},{salary}")
            s_names += 1
print(f"Number of 'S' names are {s_names}/{total_records}")
