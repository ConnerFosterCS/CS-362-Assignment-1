# Connner Foster (932777502)
# cs362 section 001
# FizzBuzz
def fizzbuzz(num): 
  if ((num % 3) == 0 and (num % 5) == 0):
    return "FizzBuzz"
  elif ((num % 3) == 0):
    return "Fizz"
  else:
    return num