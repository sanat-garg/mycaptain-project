print('\nEnter numbers in a list, separate them by commas.')
num = input('List: ')
num = (num).split(',')
positive = []
for x in num:
    if((int(x)) > -1):
        positive.append(x)
positive = ((',').join(positive))
print('Numbers that are positive: '+positive+'\n')
