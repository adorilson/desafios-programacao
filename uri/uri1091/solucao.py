def compute(divisa, casa):
  if casa[0]==divisa[0] or casa[1]==divisa[1]:
    return 'divisa'
  
  if casa[0]>divisa[0] and casa[1]>divisa[1]:
    return 'NE'
  
  if casa[0]>divisa[0] and casa[1]<divisa[1]:
    return 'SE'
  
  if casa[0]<divisa[0] and casa[1]<divisa[1]:
    return 'SO'
  
  if casa[0]<divisa[0] and casa[1]>divisa[1]:
    return 'NO'

while True:
  K = int(input())
  if K==0:
    break
  
  divisa = tuple([int(e) for e in input().split()])

  for _ in range(K):
    casa = tuple([int(e) for e in input().split()])
    pais = compute(divisa, casa)
    print(pais)
