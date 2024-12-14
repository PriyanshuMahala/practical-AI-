#Check if a num if palindrome

word = "racecar"
is_palindrome = True

for i in range(len(word) // 2):
    if word[i] != word[len(word) - 1 - i]:
        is_palindrome = False
        break


print("Yes" if is_palindrome else "No")

