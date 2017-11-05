# Chapter-8.16
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
    # if current element is greater than max
    if(x > max):
        # set max value to x
        max = x

# calculate the average
avg = sum / 4
print('Average Weight :', avg)
print('Max weight :', max)
# get the index from user
# FIXME (4): Prompt the user for a list index and output that weight in pounds and kilograms.
index = int(input('Enter a list index location (0 - 3)\n'))
print('Weight in pounds:',weight[index - 1])
print('Weight in kilograms:',weight[index - 1] / 2.2)
# sort the list
# FIXME (5): Sort the list and output it.
weight.sort()
print('sorted list:', weight)
