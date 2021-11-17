# For the following list of numbers:

numbers = [1, 6, 2, 2, 7, 1, 6, 13, 99, 7]

# 1. Print out a list of the even integers:


# 2. Print the difference between the largest and smallest value:


# 3. Print True if the list contains a 2 next to a 2 somewhere.


# 4. Print the sum of the numbers, 
#    BUT ignore any section of numbers starting with a 6 and extending to the next 7.
#    
#    So [11, 6, 4, 99, 7, 11] would have sum of 22


# 5. HARD! Print the sum of the numbers. 
#    Except the number 13 is very unlucky, so it does not count.
#    And numbers that come immediately after a 13 also do not count.
#    HINT - You will need to track the index throughout the loop.
#
#    So [5, 13, 2] would have sum of 5. 

#1
print(list(filter(lambda number: number % 2 == 0, numbers)))

# 2
print(max(numbers) - min(numbers))

#3
# for num in numbers:
#     if num == 2 and numbers[numbers.index(num) + 1] == 2:
#         print(True)
for i in range(len(numbers) - 1):
    if numbers[i] == 2 and ((i + 1) <= len(numbers) - 1):
        if numbers[i] == numbers[i + 1]:
            print(True)

#4
do_count = True
sum_tot = 0
for num in numbers:
    if num == 6: do_count = False 
    if do_count == True: sum_tot += num 
    if num == 7: do_count = True 
print(sum_tot)

#5
do_count = True
sum_tot = 0
for num in numbers:
    if num == 13: do_count = False 
    if do_count == True: sum_tot += num 
    if num != 13: do_count = True 
print(sum_tot)








