marks=[]
maths=int(input("Enter marks in Maths: "))
marks.append(maths)
science=int(input("Enter marks in Science: "))
marks.append(science)
english=int(input("Enter marks in English: "))
marks.append(english)
total=sum(marks)
average=total/len(marks)
print("Total Marks=", total)
print("Average Marks=", average)
if average>=50:
    print("Pass")