

def rle_crypt(arr):
    count = 1
    crypted = []
    for i in arr:
        for j in range(len(i)-1):
            if i[j] == i[j+1]:
                count += 1
            else:
                crypted.append([count, i[j]])
                count = 1
        crypted.append([count, i[j+1]])
    return crypted

with open('data.txt', 'r') as file:
    data = file.readlines()

with open('crypted_data.txt', 'w') as file:
    file.write(' '.join(list(map(str, rle_crypt(data)))))



