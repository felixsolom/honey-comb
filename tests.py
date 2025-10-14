import unittest
import textwrap
from functions.get_files_info import get_files_info, get_file_content

class TestFileInfo(unittest.TestCase):

   def test_root_dir(self):
    result = get_files_info("calculator", ".")
    print(result)
    expected = textwrap.dedent('''
        Results for . directory:
        - main.py: file_size=718 bytes, is_dir=False
        - pkg: file_size=160 bytes, is_dir=True
        - tests.py: file_size=1330 bytes, is_dir=False
    ''').strip()
    self.assertEqual(result, expected)

   def test_pkg_dir(self):
    result = get_files_info("calculator", "pkg")
    print(result)
    expected = textwrap.dedent('''
        Results for pkg directory:
        - calculator.py: file_size=1720 bytes, is_dir=False
        - render.py: file_size=375 bytes, is_dir=False
    ''').strip()
    self.assertEqual(result, expected)

   def test_error1_dir(self):
        result = get_files_info("calculator", "/bin")
        print(result)
        expected = 'Error: Cannot list "/bin" as it is outside the permitted working directory'
        self.assertEqual(result, expected)

   def test_error2_dir(self):
        result = get_files_info("calculator", "../")
        print(result)
        expected = 'Error: Cannot list "../" as it is outside the permitted working directory'
        self.assertEqual(result, expected)

class TestFileContent(unittest.TestCase):
   def test_main(self):
      result = get_file_content("calculator", "main.py")
      print(result)
      with open("calculator/main.py", "r") as f:
         expected = f.read(10000)
        
      self.assertEqual(result, expected)  

    


if __name__ == "__main__":
    unittest.main()