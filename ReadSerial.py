import serial

marel = serial.Serial('COM7', 9600)
print(marel.name)
rl2 = marel.readline()
print(rl2)





