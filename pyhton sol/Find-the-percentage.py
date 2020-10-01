n = int(input())
student_marks = {}
for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))


    student_marks[name] = scores



query_name = input()
list_1 =  list(student_marks[query_name])
sum1 = sum(list_1)

avg = '%.2f'%(sum1/len(list_1))
print(avg)
