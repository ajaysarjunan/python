word=input("enter a string")
reverse=list(word)
pali=True
end_index=-1
for x in range(len(word)):
    if reverse[x]==word[end_index]:
        end_index-=1
    else:
        pali=False
        break
if pali==True:
    print(f"{word} is a palindrome")
else:
    print(f"{word} is not a palindrome")