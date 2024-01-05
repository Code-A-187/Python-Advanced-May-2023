num = int(input())

res_codes = set()

for _ in range(num):
    code = input()
    res_codes.add(code)

info = input()

while info != "END":
    res_codes.remove(info)
    info = input()

print(len(res_codes))
for num in sorted(res_codes):
    print(num)
