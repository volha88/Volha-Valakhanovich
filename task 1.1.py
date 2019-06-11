s = input('Введите выражение - ')
i = len(s)
for i in range(i // 2):
    if s[i] != s[-1-i]:
        print('ne palindrom')
        quit()
print('palindrom')