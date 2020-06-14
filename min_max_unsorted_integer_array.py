# find the largest and smallest number in an unsorted integer array

# the python way
# a = [9, 3, 5, 8, 6, 9, 9, 4, 10, 11, 32, 22, 20]
# a.sort(); print("min : %d - max : %d" % (a[0], a[-1]))

# and manually

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
a = [9, 3, 5, 8, 6, 9, 9, 4, 10, 11, 32, 22, 20]
# start min max by comparing first two array items
if a[0] > a[1]:
    max, min = a[0], a[1]
else:
    max, min = a[1], a[0]

for n in range(len(a)):
    if a[n] < min:
        min = a[n]
        n += 1
    elif a[n] > max:
        max = a[n]
        n += 1
    else: # n is the same or neither larger or smaller
        n += 1

print(f"min: {min} - max: {max}")
# min: 3 - max: 32
