#test การกราฟ
import matplotlib.pyplot as plt

SUBJECT_1 = input()
score_1 = float(input())
if score_1 > 100:
    print("Error")

SUBJECT_2 = input()
score_2 = float(input())
if score_2 > 100:
    print("Error")

SUBJECT_3 = input()
score_3 = float(input())
if score_3 > 100:
    print("Error")

SUBJECT_4 = input()
score_4 = float(input())
if score_4 > 100:
    print("Error")

dictcollect = {}

dictcollect[SUBJECT_1]= score_1
dictcollect[SUBJECT_2]= score_2
dictcollect[SUBJECT_3]= score_3
dictcollect[SUBJECT_4]= score_4

sorted_data = dict(sorted(dictcollect.items(), key=lambda item: item[1], reverse=True))

listallsubject = list(sorted_data.keys()) 
values = list(sorted_data.values())

# สร้างกราฟแท่ง
plt.bar(listallsubject, values)
plt.ylim(0, 100)#ตัวนี้กำหนดกราฟมึงต้องเอาตัวนี้ไปใส่
plt.title('THIS IS GRAPH SCORE FOR SHIT PROHECT')

plt.show()