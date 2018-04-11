numbers = [12,37,5,42,8,3]
even = []
add = []
while len(numbers) > 0 :
    number = numbers.pop()
    if number % 2 == 0:
        even.append(number)
    else:
        add.append(number)

print(even)
print (add)

for letter in 'Python':
    print(letter);
    print(letter);

fruits = ['banana','apple','mango']
for fruit in fruits:
    print(fruit)

for index in range(len(fruits)):
    print (fruits[index])

print (2%2)

for num in range(2,30):
    for i in range(2,num):



        if num%i == 0:
            j = num/i
            print( num , '等于' , i , '*' , j )
            break
    else:
        print ( num , '是一个质数')

print ('--------2018 01 29------------');

print (not(0));
print (not(1));
print (not( True ));
print (not( False ));

s = 0
i = 2
while (i < 100):
    j = 2
    while (j <= i/j) :
        s += 1;
        if( i%j == 0 ):
            break
        j += 1
    else:
        print (i, '是质数')
    i += 1
print ('s = ',s)


s = 0
i = 2
while (i < 100):
    j = 2
    while (j <= (i / j)):
        s += 1
        if not (i % j): break
        j = j + 1
    if (j > i / j): print (i, " 是素数")
    i = i + 1
print ('s = ',s)
print ("Good bye!")








