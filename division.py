def  division (num1:int, num2:int) -> int:
    
    accumulator: int = num1
    index: int = 0

    while accumulator > 0 :
        accumulator = accumulator - num2
        index = index + 1 
    return index

print(division(10,2))