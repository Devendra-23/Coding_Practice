def filter_even_numbers(numbers):
     evens = []
     for num in numbers:
          if num % 2 == 0:
               evens.append(num)
     return evens

print(filter_even_numbers([1,22,434,35,12,68,99,3,494,567,344,333,312,4343,55]))
        