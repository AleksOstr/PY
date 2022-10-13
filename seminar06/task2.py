# Дан список, вывести отдельно буквы и цифры.

input_list = input().split()
nums = list(filter(lambda x: x.isdigit(), input_list))
alphs = list(filter(lambda x: x.isalpha(), input_list))
print(nums, alphs, sep='\n')