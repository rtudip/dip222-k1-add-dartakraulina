#1.uzd
# import pandas   
# import csv
# get_info =input()
# region = []
# with open('data.txt',"r") as f:
#     next(f)
#     for line in f:
#         row=line.rstrip().split(",")
#         if row[4]==get_info:       
#              region.append(row[6])
# print(min(region))


 #2.uzd
# import pandas
# import csv
# get_info =input()
# skaits = []
# with open('data.txt',"r") as f:
#     next(f)
#     for line in f:
#         row=line.rstrip().split(",")
#         if row[4]==get_info:
#             skaits.append(int((row[8])))
            
# print(sum((skaits)))
        
#3.uzd

# import pandas   
# import csv
# get_info =input()
# skaits = []
# with open('data.txt',"r") as f:
#     next(f)
#     for line in f:
#         row=line.rstrip().split(",")
#         if row[4]==get_info:
#              if row[7] == "Telecommunications":  
#                 skaits.append(int((row[8])))
# print(sum(skaits))


#4.uzd

# import pandas   
# import csv
# get_info =input()
# x= 0
# with open('data.txt',"r") as f:
#     next(f)
#     for line in f:
#         row=line.rstrip().split(",")
#         if row[4]==get_info:
#             if row[3].startswith("https://") :
#                 x+=1
# print(x)  


#5.uzd

import pandas   
import csv
get_info =input()
x= 0
with open('data.txt',"r") as f:
     next(f)
     for line in f:
        row=line.rstrip().split(",")
        if row[4]==get_info:
            if row[3].endswith(".org/"):
                x+=1
print(x)  