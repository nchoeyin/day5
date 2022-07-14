students = input("Enter the scores: ").split()
max = int(students[0])
for i in range(1,len(students)):
    if int(students[i])> max:
        max = int(students[i]);
print(f'Max is {max}')
