# For the following list of numbers:

numbers = [1, 6, 2, 2, 7, 1, 6, 13, 99, 7]

# 1. Print out a list of the even integers:
evens = []
for number in (numbers):
  if number % 2 == 0:
    evens.append(number)
print(evens)

# 2. Print the difference between the largest and smallest value:
print(max(numbers)- min(numbers))

# 3. Print True if the list contains a 2 next to a 2 somewhere.
current = None
for number in numbers:
    if number == current and current == 2:
        print(True)
        break
    current = number
print(current)


# 4. Print the sum of the numbers, 
#    BUT ignore any section of numbers starting with a 6 and extending to the next 7.
#    
#    So [11, 6, 4, 99, 7, 11] would have sum of 22

sum_of_num=[]
to_count = True
for number in numbers:
    if number == 6:
        to_count = False
    elif to_count == True:
        sum_of_num.append(number)
    elif number == 7:
        to_count = True

print(sum(sum_of_num))


    

    # if number != 6:
    #     sum_of_num.append(number)
    # if number == 7:

    # if number == 6:


# 5. HARD! Print the sum of the numbers. 
#    Except the number 13 is very unlucky, so it does not count.
#    And numbers that come immediately after a 13 also do not count.
#    HINT - You will need to track the index throughout the loop.
#
#    So [5, 13, 2] would have sum of 5. 
our_index = 0
all_num_sum = numbers

for number in numbers:
    our_index += 1
    if number == 13:
        break

for num in range(2):
    

    all_num_sum.pop(our_index-1)

# all_num_sum.pop(our_index-1)

print(all_num_sum)


