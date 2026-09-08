start = int(input("Enter start: "))
end = int(input("Enter end: "))

print("Prime numbers:")

for n in range(start, end + 1):
    count = 0
    i = 1

    while i <= n:
        if n % i == 0:
            count += 1
        i += 1

    if count == 2:
        print(n, end=" ")