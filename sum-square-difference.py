sum_squares = 0
sum_to_square = 0

for i in range(101):
  sum_squares += i ** 2
  sum_to_square += i

print(abs(sum_squares - (sum_to_square ** 2)))
