import math  # math library
import tabulate # tabulate library
import matplotlib.pyplot as plt # plot fuction from matplotlib library

class Collatz:
  def __init__(self):
    pass
  def table(self, x, y, xlabel, ylabel):
    print(tabulate.tabulate({xlabel: x, ylabel: y}, headers="keys", tablefmt="pretty"))
  def graph(self, x, y, xlabel, ylabel, title):
    # plotting the points 
    plt.plot(x, y)

    # naming the x axis
    plt.xlabel(xlabel)
    
    # naming the y axis
    plt.ylabel(ylabel)

    # giving a title to my graph
    plt.title(title)

    # function to show the plot
    plt.show()
  def loop(self):
    num = int(input("Enter an odd number: "))
    if num >= 1 and num % 2 == 1 and isinstance(num, int):
      specialStep = 1
      steps, output = 0, num
      stepsList = [num]
      while output != specialStep:
        if output % 2 == 0:
          output = int(output / 2)
        else:
          output = 3 * output + 1
        steps += 1
        stepsList.append(output)
        
      print(f"It took {steps} steps to get to the Collatz Conjecture Loop")
      print(f"Input number: {num}")
      print("Steps Taken: ")
      x = [x for x in range(len(stepsList))] # x axis values
      y = stepsList # corresponding y axis values
      self.table(x, y, "x", "f(x)")
      self.graph(x, y, 'Steps Taken', 'Current Value', 'Steps Taken to Reach Collatz Conjecture Loop!')
    else:
      print(f"{num} is an invalid input")
  def output(self):
    num = int(input("Input: "))
    if num >= 1 and num % 2 == 1 and isinstance(num, int):
      specialStep = 1
      output = num
      stepsList = [num]
      while output != specialStep:
        if output % 2 == 0:
          output = int(output / 2)
        else:
          output = 3 * output + 1
        stepsList.append(str(output))
      y = [str(step) for step in stepsList]   # corresponding y axis values
      print(f"Output: {' '.join(y)}")
    else:
      print(f"{num} is an invalid input")
C = Collatz()
C.loop()
C.output()