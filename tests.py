import unittest
from functions.get_files_info import get_files_info, get_file_content, write_file
from functions.run_python import run_python_file

class TestFileInfo(unittest.TestCase):
   def test_error2_dir(self):
        result = get_files_info("calculator", "../")
        expected = 'Error: Cannot list "../" as it is outside the permitted working directory'
        self.assertEqual(result, expected)

class TestFileContent(unittest.TestCase):
   def test_main(self):
      result = get_file_content("calculator", "main.py")
      with open("calculator/main.py", "r") as f:
         expected = f.read(10000)
        
      self.assertEqual(result, expected)  

   def test_calc(self):
      result = get_file_content("calculator", "pkg/calculator.py")
      with open("calculator/pkg/calculator.py", "r") as f:
         expected = f.read(10000)
        
      self.assertEqual(result, expected) 
       
   def test_error(self):
      result = get_file_content("calculator", "/bin/cat")
      expected = 'Error: Cannot read "/bin/cat" as it is outside the permitted working directory'
        
      self.assertEqual(result, expected)  

   def test_error2(self):
      result = get_file_content("calculator", "pkg/does_not_exist.py")
      expected = 'Error: File not found or is not a regular file: "pkg/does_not_exist.py"'
        
      self.assertEqual(result, expected)  

class TestWriteFile(unittest.TestCase):
   def test_lorem(self):
      result = write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
      expected = f'Successfully wrote to "lorem.txt" (28 characters written)'

      self.assertEqual(result, expected)

   def test_more_lorem(self):
      result = write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
      expected = f'Successfully wrote to "pkg/morelorem.txt" (26 characters written)'

      self.assertEqual(result, expected)

   def test_error(self):
      result = write_file("calculator", "/tmp/temp.txt", "this should not be allowed")
      expected = 'Error: Cannot write to "/tmp/temp.txt" as it is outside the permitted working directory'

      self.assertEqual(result, expected)

class TestRunPython(unittest.TestCase):
   def test_run_main(self):
      result = run_python_file("calculator", "main.py")
      print(result)
   
   def test_args(self):
      result = run_python_file("calculator", "main.py", ["3 + 5"])
      print(result)

   def test_tests(self):
      result = run_python_file("calculator", "tests.py")
      print(result)

   def test_error(self):
      result = run_python_file("calculator", "../main.py")
      print(result)
      expected = 'Error: Cannot execute "../main.py" as it is outside the permitted working directory'

      self.assertEqual(result, expected)

   def test_error_non_existent_dir(self):
      result = run_python_file("calculator", "nonexistent.py")
      print(result)
      expected = 'Error: File "nonexistent.py" not found.'

      self.assertEqual(result, expected)

   def test_error_not_python_file(self):
      result = run_python_file("calculator", "lorem.txt")
      print(result)
      expected = 'Error: "lorem.txt" is not a Python file.'

      self.assertEqual(result, expected)



if __name__ == "__main__":
    unittest.main()