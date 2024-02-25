n = int(input())
cust = list(map(int, input().split()))
ldr_max, mbr_max = map(int, input().split())
total = 0

mbr_cust = list(map(lambda x: x-ldr_max, cust))
total += len(cust)

for c in mbr_cust:
    if c > 0:
        if c % mbr_max == 0:
            total += c // mbr_max
        else:
            total += c // mbr_max + 1

print(total)