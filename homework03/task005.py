

def fib(num):
    if num in (1, 2):
        return 1
    return fib(num-1) + fib(num-2)


n = int(input('Введите число '))
result = [0]

for i in range(1, n+1):
    result.append(-fib(i))
    result.append(fib(i))
result.sort()
print(result)