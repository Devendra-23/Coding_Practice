def check_anagrams(str1,str2):
    return sorted(str1) == sorted(str2)

print(check_anagrams('act','cat'))
print(check_anagrams('tone','note'))
print(check_anagrams('save','vase'))
