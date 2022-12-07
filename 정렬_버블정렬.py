def bubble_sort(a):
    n= len(a)
    for i in range(n-1):
        for j in range(n-1, i,-1):
            if a[j-1] >a[j]:
                a[j-1],a[j] = a[j], a[j-1]

print('버블 정렬 실행')
num= int(input('원소 수 입력: '))
x= [None] * num

for i in range(num):
    x[i] = int(input(f'x[{i}]: '))

bubble_sort(x)

print('오름차순 정렬')
for i in range(num):
    print(f'x[{i}]= {x[i]}')