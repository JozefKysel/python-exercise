from utils import RECORD_SEPARATOR

def generateUsername(givenNames, lastName):
  givenNamesInitials = ''
  for name in givenNames:
    givenNamesInitials += name[0].lower()
  return givenNamesInitials + lastName.lower()

def createUserRecord(id, givenNames, lastName, department):
  username = generateUsername(givenNames, lastName)
  return RECORD_SEPARATOR.join([id, username, RECORD_SEPARATOR.join(givenNames), lastName, department])

def createManyUserRecords(users):
  userRecords = []
  for user in users:
    id, *fullName, department = user.split(RECORD_SEPARATOR)
    * givenNames, lastName = fullName
    userRecords.append(createUserRecord(id, givenNames, lastName, department))
  return userRecords