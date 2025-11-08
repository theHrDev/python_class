num_lists = [45,50,90,30,56,67,49,100]

maximum = 0
for num in num_lists:
   if num > maximum:
       print(f"{num} is greater than {maximum}")
       maximum = num
print(f"maximum is {maximum}")