#Chapter # 67 CSV

import csv

#Read CSv File
with open("mycsvfile.csv") as csvfile:
    contents = csv.reader(csvfile)
    for content in contents:
        print(content)

#Write or Overwrite CSV File
with open("mycsvfile2.csv", "w", newline="") as csvfile:
    fileWriter = csv.writer(csvfile)
    fileWriter.writerow(["2021","ICC T20", "England"])
    fileWriter.writerow(["2022","ICC T20", "China"])

#Append CSV File
with open("mycsvfile.csv", "a", newline="") as csvfile:
    fileWriter = csv.writer(csvfile)
    fileWriter.writerow(["2023","ICC T20", "Pakistan"])
    fileWriter.writerow(["2024","ICC T20", "Pakistan"])