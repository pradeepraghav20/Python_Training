import csv

with open ("friends.csv",'r') as file:
    reader=csv.reader(file)
    print(reader)
    for row in reader:
        pass
        # print(row)


import csv
with open('protagonist.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["SN", "Movie", "Protagonist"])
    writer.writerow([1, "Lord of the Rings", "Frodo Baggins"])
    writer.writerow([2, "Harry Potter", "Harry Potter"])




#
# with open ('protagonist.csv', 'r') as file:
#     read=csv.reader(file)
#     for i in read:
#         print(i)

import pandas as pd
content=pd.read_csv("friends.csv",usecols =["name"])
print(content)




