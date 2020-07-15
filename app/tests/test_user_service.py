from user_service import generateUsername, createUserRecord, createManyUserRecords
import unittest

class TestUserService(unittest.TestCase):
  
  id = '1234'
  givenNames = ['John', 'Stuart']
  lastName = 'Doe'
  department = 'Research'
  username = 'jsdoe'
  users = ['3456:Milan:Rastislav:Stefanik:Defense', '4567:Jozef:Kysel:Development']
  userRecords = ['3456:mrstefanik:Milan:Rastislav:Stefanik:Defense', '4567:jkysel:Jozef:Kysel:Development']
  colon = ':'

  def test_createManyUserRecords(self):
      """
      Test that it will create many user records 
      """
      result = createManyUserRecords(self.users)
      self.assertEqual(result, self.userRecords)
  
  def test_generateUsername(self):
        """
        Test that it can generate username
        """
        result = generateUsername(self.givenNames, self.lastName)
        self.assertEqual(result, self.username)
  
  def test_generateUsername_no_middle_names(self):
        """
        Test that it not fail when user has not middle name
        """
        givenNames = ['John']
        result = generateUsername(givenNames, self.lastName)
        self.assertEqual(result, 'jdoe')
  
  def test_generateUsername_no_given_names(self):
        """
        Test that it not fail when user has not givenNames
        """
        givenNames = []
        result = generateUsername(givenNames, self.lastName)
        self.assertEqual(result, 'doe')
  
  def test_createUserRecord(self):
        """
        Test that it will create user record
        """
        result = createUserRecord(self.id, self.givenNames, self.lastName, self.department)
        expectedResult = self.colon.join([self.id, self.username, self.colon.join(self.givenNames), self.lastName, self.department])
        self.assertEqual(result, expectedResult)
  
  def test_createUserRecord_no_given_names(self):
        """
        Test that it will not fail when user has not givenNames
        """
        givenNames = []
        username = 'doe'
        result = createUserRecord(self.id, givenNames, self.lastName, self.department)
        expectedResult = self.colon.join([self.id, username, self.colon.join(givenNames), self.lastName, self.department])
        self.assertEqual(result, expectedResult)
  
  def test_createUserRecord_no_middle_name(self):
        """
        Test that it will not fail when user has not middle name
        """
        givenNames = ['John']
        username = 'jdoe'
        result = createUserRecord(self.id, givenNames, self.lastName, self.department)
        expectedResult = self.colon.join([self.id, username, self.colon.join(givenNames), self.lastName, self.department])
        self.assertEqual(result, expectedResult)

if __name__ == "__main__":
    unittest.main()

