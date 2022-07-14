count = 0
sum = 0
student_heights = input("Enter the heights: ").split()
for i in student_heights:
    count += 1
    i = int(i)
    sum += i 
avg = round(sum / count) 
print(f"There are {count} number of elements \nSum is {sum} \nAverage is {avg}")
'''
----------------------------------------------------------------------------------------------------------------------------------------------------------------
Output:
Enter the heights: 170 165 160 180
There are 4 number of elements 
Sum is 675 
Average is 169

Enter the heights: 100 100 100
There are 3 number of elements 
Sum is 300 
Average is 100.0

-----------------------------------------------------------------------------------------------------------------------------------------------------------------
'''
