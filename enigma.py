import numpy as np

# read in rotors, reflector, and turnovers, and set rotors
def getMachine():
  rotors = np.genfromtxt('rotors.txt', dtype='str')
  reflector = np.genfromtxt('reflectors.txt', dtype='str')
  turnovers = np.genfromtxt('turnovers.txt', dtype='str')

  rotors = [list(x) for x in rotors]
  reflector = [list(x) for x in reflector]

  return [rotors, reflector, turnovers]

# plugboard, creating a dictionary to map letters
def makePlug(letterMap):
  keys = [chr(i) for i in range(65,91)] # keys for dictionary, A-Z
  plugboard = {}
  for i in range(len(keys)): # looping to create dictionary
    plugboard[keys[i]] = letterMap[i]

  return plugboard

# rotor function
def rotorFunction(char, rotors, turnovers, rotorNum, forward):
  # rotating if the turnover is flipped or if it's the first rotor
  if(rotorNum == 0 and forward == 1):
    rotors[rotorNum].sort(key=rotors[rotorNum][0].__eq__)
  if(forward == 1 and rotors[rotorNum][0] == turnovers[rotorNum]):
    rotors[rotorNum+1].sort(key=rotors[rotorNum+1][0].__eq__)

  if(forward == 1):
    return [rotors,rotors[rotorNum][ord(char) - 65]]
  elif(forward == 0):
    ind = [i for i, x in enumerate(rotors[rotorNum]) if x == char][0]
    return [rotors,chr(65 + ind)]

def main(userIn,rotorNums,rotorPos,reflectNum,letterMap):
  userIn = [y.upper() for x in userIn for y in x] # clean user input

  # read in machine things
  rotors, reflector, turnovers = getMachine()
  # get plugboard dictionary
  plugboard = makePlug(letterMap)

  # machine settings
  rotors = [rotors[ind] for ind in rotorNums]
  turnovers = [turnovers[ind] for ind in rotorNums]
  reflector = reflector[reflectNum]

  # turn rotors to starting positions
  for rotorNum in range(len(rotors)):
    for i in range(rotorPos[rotorNum]-1):
      rotors[rotorNum].sort(key=rotors[rotorNum][0].__eq__)

  message = ""
  # pass through the machine
  for char in userIn:
    if(char != " "):
      encoded = plugboard[char] # pass through plugboard first
      for i in range(len(rotors)): # pass forwards
        rotors, encoded = rotorFunction(encoded,rotors,turnovers,i,1)

      # pass through reflector
      encoded = reflector[ord(encoded) - 65]

      for i in range(len(rotors)-1,-1,-1): # pass backwards
        rotors, encoded = rotorFunction(encoded,rotors,turnovers,i,0)

      message += plugboard[encoded] # pass back through plugboard

    elif(char == " "):
      message += " "

  return message

# testing settings
rotors = [0,1,2]
reflector = 1 # only length 1
rotorPos = [5,10,15] # must be same length as rotors
letterMap = ['Z', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
'N', 'O', 'P', 'Q', 'S', 'R', 'T', 'U', 'V', 'W', 'X', 'Y','A'] # symmetric

test = 'the quick brown fox jumped over the lazy dog'
message = main(test,rotors,rotorPos,reflector,letterMap) # encode
print(message)
message = main(message,rotors,rotorPos,reflector,letterMap) # decode
print(message)
