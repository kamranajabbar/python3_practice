#Chapter # 67-73 CSV files

#67: CSV files
#68: CSV files: Reading them
#69: CSV files: Picking information out of them
#70: CSV files: Loading information into them. Part 1
#71: CSV files: Loading information into them. Part 2
#72: CSV files: Loading information into them. Part 3
#73: CSV files: Appending rows to them.

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