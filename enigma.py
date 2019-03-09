import numpy as np

def getMachine():
  # read in rotors, reflector, and turnovers
  rotors = np.genfromtxt('rotors.txt', dtype='str')
  reflector = np.genfromtxt('reflectors.txt', dtype='str')
  turnovers = np.genfromtxt('turnovers.txt', dtype='str')

  # possible used rotors
  rotor1 = [x for x in rotors[0]]
  rotor2 = [x for x in rotors[1]]
  rotor3 = [x for x in rotors[2]]
  rotor4 = [x for x in rotors[3]]
  rotor5 = [x for x in rotors[4]]

  reflect1 = [x for x in reflector[0]] # UKW-A
  reflect2 = [x for x in reflector[1]] # UKW-B
  reflect3 = [x for x in reflector[2]] # UKW-C

  return [rotor1, rotor2, rotor3, rotor4, rotor5, \
    reflect1, reflect2, reflect3 , turnovers]

rotor1, rotor2, rotor3, rotor4, rotor5, \
  reflect1, reflect2, reflect3 , turnovers = getMachine()

# user input
userIn = raw_input("Input Message: ")
userIn = [y.upper() for x in userIn for y in x]

message = ""
###########################
# make a modular function #
###########################
for char in userIn:
  if(char != " "):
    # turning the first rotor
    temp = rotor1[0]; rotor1 = rotor1[1:]; rotor1.append(temp)

    # turning second rotor if needed
    if(rotor1[0] == turnovers[0]):
      temp = rotor2[0]; rotor2 = rotor2[1:]; rotor2.append(temp)
    # turning third rotor if needed
    if(rotor2[0] == turnovers[1]):
      temp = rotor3[0]; rotor3 = rotor3[1:]; rotor3.append(temp)


    # encoding
    r1Val = rotor1[ord(char) - 65] # first rotor
    r2Val = rotor2[ord(r1Val) - 65] # second rotor
    r3Val = rotor3[ord(r2Val) - 65] # third rotor

    # pass through reflector
    reflectVal = reflect2[ord(r3Val) - 65] # UKW-B as default

    # pass backwards through rotors
    ind = [i for i, x in enumerate(rotor3) if x == reflectVal][0]
    r3ValR = chr(65 + ind)
    ind = [i for i, x in enumerate(rotor2) if x == r3ValR][0]
    r2ValR = chr(65 + ind)
    ind = [i for i, x in enumerate(rotor1) if x == r2ValR][0]
    r1ValR = chr(65 + ind)

    message += r1ValR

  elif(char == " "):
    message += " "

print("Output: "+message)
