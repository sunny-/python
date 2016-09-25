count = 1
i = 3
while count != 1000:
    if i%2 != 0:
       for k in range(2,i):
          if i%k == 0:        # 'i' is _not_ a prime!
            print(i)       # ??
            count += 1     # ??
            break
    i += 1 