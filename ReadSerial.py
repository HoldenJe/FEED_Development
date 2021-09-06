import serial

print("Define COM port. Example 'COM7':")
mycom = input()
print("Connecting to: " + mycom)

marel = serial.Serial(mycom, 9600)
print("Weigh object on scale and press record:")
rl2 = marel.readline()
rl2 = rl2.decode()
rl2 = rl2.split("\t")
weight = float(rl2[2])
print("Your object weighs:")
print(weight)
print("")



