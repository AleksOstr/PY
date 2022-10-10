

def rle_crypt(file_name: str):
    with open(file_name, 'r') as file:
        data = file.readlines()
    count = 1
    crypted = []
    for i in data:
        for j in range(len(i)-1):
            if i[j] == i[j+1]:
                count += 1
            else:
                crypted.append([count, i[j]])
                count = 1
        crypted.append([count, i[j+1]])
    with open('crypted_data.txt', 'w') as file:
        file.write(' '.join(list(map(str, crypted))))

rle_crypt('data.txt')





