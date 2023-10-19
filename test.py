# 1. Import unittest
import unittest
from calculator import Calculator

# 2. Class Test 
# - Implementasi inheritance
class Test(unittest.TestCase):
  
  # 3. Buat testing (method)
  def test_add(self):
    # 3.1 Input 
    testcase1 = Calculator(5)
    self.assertEquals(testcase1.result, 5)
    # 3.2 Proses
    testcase1.add(50)
    # 3.3 Output 
    self.assertEquals(testcase1.result, 55)


# 4. Cek file jalan atau tidak!
unittest.main()