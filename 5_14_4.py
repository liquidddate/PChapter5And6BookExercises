def recurse(n, s):
    if n == 0:
        print(s)
    else:
        recurse(n-1, n+s) #first loop is 3 + 0, second is 2 + 3, third is 1 + 5, then n = 0 so it prints s

recurse(3, 0)