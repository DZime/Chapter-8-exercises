weight = []

for i in range(1, 5):
    strng = 'Enter weight ' + str(i) + '\n'
    x = float(input(strng))
    weight.append(x)
    print()
print('Weights:', weight)

sum = 0
max = -1

for x in weight:
    sum += x
    if(x > max):
        max = x

avg = sum / 4
print('Average Weight :', avg)
print('Max weight :', max)

index = int(input('Enter a list index location (0 - 3)\n'))
print('Weight in pounds:',weight[index - 1])
print('Weight in kilograms:',weight[index - 1] / 2.2)

weight.sort()
print('sorted list:', weight)
