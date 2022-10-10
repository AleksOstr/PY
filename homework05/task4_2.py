# def rle_decrypt(file_name: str):
#     with open(file_name, 'r') as file:
#         cypted_data = file.readlines()

# encrypted = ''
# for i in crypted:
#     for j in range(len(i)-1):
#         encrypted += i[j] * i[j+1]
# print(encrypted)


with open('crypted_data.txt', 'r') as f:
    cr_data = (''.join(f.readlines()))
print(cr_data)