from user_repository import readUsersFromInputFiles, writeUserRecordsToOutputFile
from user_service import createManyUserRecords
import os
import unittest

class TestUserRepository(unittest.TestCase):
  inputFilePaths = ['tests/test_users_data.txt']
  emptyInputFilePaths = ['tests/test_users_data_empty.txt']
  outputFilePath = './tests/test_users_output_data.txt'
  users = ['3456:Milan:Rastislav:Stefanik:Defense', '4567:Jozef:Kysel:Development']
  userRecords = createManyUserRecords(users)
  
  def test_readUsersFromInputFiles(self):
        """
        Test that it will read user records from input file
        """
        result = readUsersFromInputFiles(self.inputFilePaths)
        self.assertEqual(result, self.users)
  
  def test_readUsersFromInputFiles_emtpy_input_file(self):
        """
        Test that it will not fail when input file is empty
        """
        result = readUsersFromInputFiles(self.emptyInputFilePaths)
        self.assertEqual(result, [])
  
  def test_writeUserRecordsToOutputFile(self):
        """
        Test that it will write user records to outpuFile
        """
        writeUserRecordsToOutputFile(self.outputFilePath, self.userRecords)
        outputFileContent = readUsersFromInputFiles([self.outputFilePath])
        self.assertEqual(outputFileContent, self.userRecords)
        os.remove(self.outputFilePath)
  
  def test_writeUserRecordsToOutputFile_no_userRecords(self):
        """
        Test that it will not fail when user records is empty list
        """
        writeUserRecordsToOutputFile(self.outputFilePath, [])
        outputFileContent = readUsersFromInputFiles([self.outputFilePath])
        self.assertEqual(outputFileContent, [])
        os.remove(self.outputFilePath)

if __name__ == "__main__":
    unittest.main()

