# find the largest and smallest number in an unsorted integer array
# first find out if array[0] is greater than array[1]
#   if it is then place array[1] in min and array[0] in max
# loop comparing n to min and max
# if array[n]
#   < min
#       min = n
#   > max
#       max = n
#   == min or max
#       n += 1

min, max = 0, 0
a = [] # list to sort
# a = [9, 0, 8, 1, 7, 3, 6, 4, 5]

# start min max by comparing first two array items
if a[0] > a[1]:
    min, max = a[1], a[0]
else:
    min, max = a[0], a[1]

for n in range(len(a)):
    if a[n] < min:
        min = a[n]
        n += 1
    elif a[n] > max:
        max = a[n]
        n += 1
    else:  # n is the same or neither larger or smaller
        n += 1

print(f"min: {min} - max: {max}")
# min: 0 - max: 9
