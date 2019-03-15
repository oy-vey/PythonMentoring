def cumsum(list):
  x = 0
  result = [0]
  for i in list:
    result.append(i + x)
    x = result[-1]
  return result