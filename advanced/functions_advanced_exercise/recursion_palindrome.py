reversed_word = ""


def palindrome(string, index):
    global reversed_word
    if reversed_word[:index] != string[:index]:
        return f"{string} is not a palindrome"
    if index == len(string):
        return f"{string} is a palindrome"
    reversed_word += string[-(index + 1)]
    return palindrome(string, index + 1)


# Test input
print(palindrome("peter", 0))
