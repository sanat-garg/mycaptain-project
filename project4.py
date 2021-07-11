terms = int(input('\nNumber of terms in fibonacci series you want: '))

term1 = 0
term2 = 1
num = 2

print('Fibonaaci Series: ')
if(terms == 1):
    print(term1)
elif(terms == 2):
    print(term1)
    print(term2)
else:
    print(term1)
    print(term2)
    while num != terms:
        term3 = (term1+term2)
        print(term3)
        term1 = term2
        term2 = term3
        num += 1
print('\n')
