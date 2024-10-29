def palindrome(word:str) -> bool: 
    drome: str = ""
    for i in word:
        drome = i+drome
        print(drome)
    if drome == word:
       return True
    
    return False

print(palindrome("kayak"))
print(palindrome("ana"))

def palindrome2(word: str) -> bool:
    drome = word[::-1]
    return drome == word

print(palindrome2("kayak"))
print(palindrome2("ana"))