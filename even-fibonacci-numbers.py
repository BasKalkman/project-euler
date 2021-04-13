fibonacci = [1,2]

while sum(fibonacci[-2:]) < 4000000:
  fibonacci.append(sum(fibonacci[-2:]))

result = 0
for term in fibonacci:
  if term % 2 == 0:
    result += term

print(result)

