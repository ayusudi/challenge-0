# Exception = situasi yang tidak biasa. (Error, Warning)
# Mari kita buat calculator versi OOP cukup + - * / saja namun handling exception.

class Calculator:
  def __init__(self, number=0): 
    self.result = number

  def __str__(self):
    return f'Ouputnya {self.result}'

  def add(self, n):
    self.result += n 
    return self

  def minus(self, n):
    try: 
      if type(n) is int:
        self.result -= n
        return self
      else :
        raise Exception("Hanya menerima input integer!")
    except: 
      return "Gagal"

  def divide(self, n):
    self.result /= n 
    return self

  def multiple(self, n):
    self.result *= n
    return self

if __name__ == "__main__":
  calculator = Calculator(7)
  calculator.add(3).minus(False)
  print(calculator)