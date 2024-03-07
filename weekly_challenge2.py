def LargePower(base, exponent):
    result = base**exponent
    if result > 5000:
        return True
    else:
        return False
            
    
print(LargePower(10, 3))
print(LargePower(10, 5))

def divisible_by_ten(num):
    answer = num%10
    if answer == 0:
        return True
    else:
        return False
    
print(divisible_by_ten(100))
print(divisible_by_ten(2))

