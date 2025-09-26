n = 43261596
bit=format(n, '032b')
revbit= bit[::-1]
print(int(revbit,2))
