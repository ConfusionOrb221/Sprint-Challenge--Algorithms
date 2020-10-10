#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a)
 o(n log n)

b)
    sum = 0
    for i in range(n):
      j = 1
      while j < n:
        j *= 2
        sum += 1
    (n * n /2)

c)
    o(n)
## Exercise II
    Divide n by 2 if it doesnt break then add half of the half again until it breaks then go down until it stops breaking and the value prev is the value that the eggs stop breaking at, otherwise divide by half of half n until it stops breaking then add one till it breaks and thats the number you need

    this would be O(n log n) and would be space complexity of o(1)

