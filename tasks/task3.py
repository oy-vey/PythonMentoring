def collatz(input):
  output = []
  output.append(input)
  while input != 1:
      if input % 2 == 0:
        output.append(int(input / 2))
        input = input / 2
      elif input % 2 != 0:
          output.append(int(input * 3) + 1)
          input = (input * 3) + 1      
  return output