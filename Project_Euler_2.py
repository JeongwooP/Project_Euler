#4 million = 4,000,000

from timeit import default_timer as timer

start_sec = timer()
sum_fin = 0

def fib(num): #피보나치의 0번째부터 몇 번째의 수 인지 출력하는 함수
                #실행시간이 길어서 더 효율적인 피보나치 함수를 만들어야함
    # if num == 0:
    #     return 0
    # if num == 1:
    #     return 1
    #
    # return fib(num - 2) + fib(num - 1)

    if num < 2:
        return num
    else:
        f0 = 0
        f1 = 1

        for i in range(2, num + 1):
            tmp = f1
            f1 = f1 + f0
            f0 = tmp

        return f1

for i in range(2, 1000):
    fib_num = fib(i)
    if fib_num % 2 == 0:
        sum_fin = sum_fin + fib_num

    if fib_num > 4000000:
        break

print(sum_fin)
end_sec = timer()

print(end_sec - start_sec)