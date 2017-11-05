months = ['Jan','Feb','Mar','Apr','May','June','July','Aug','Sept','Oct','Nov','Dec']
rainfall = []
for i in range(len(months)):
    amount = input('Enter monthly rain for ' +str(months[i]+':'))
    rainfall.append(amount)
    
total = 0
highest = float(rainfall[0])
lowest = float(rainfall[0])

for rf in rainfall:
    total=total+float(rf)
    if float(rf)> highest:
        highest = float(rf)

    if float(rf)< lowest:
        lowest = float(rf)
        
average = total / 12.0

print("\n")
print("Total rainfall amount for the year:   ", total)
print("Average rainfall amount for the year: ", average)
print("Highest rainfall amount for the year: ", highest)
print("Lowest rainfall amount for the year: ", lowest)
