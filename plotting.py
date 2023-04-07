import pylab as plt

mySamples = []
myLinear = []
myQuadratic = []
myCubic = []
myExponential = []

for i in range(30):
    mySamples.append(i)
    myLinear.append(i)
    myQuadratic.append(i ** 2)
    myCubic.append(i ** 3)
    myExponential.append(1.5 ** i)

plt.figure('lin quad')
plt.clf()
plt.title('Linear vs. Quadratic')
plt.xlabel('sample points')
plt.ylabel('linear function')
plt.plot(mySamples, myLinear, label='linear')
plt.plot(mySamples, myQuadratic, label='quadratic')
plt.legend()
# plt.legend(loc='upper left')

plt.figure('cub exp')
plt.clf()
plt.title('Cubic vs. Exponential')
plt.xlabel('sample points')
plt.ylabel('cubic function')
plt.plot(mySamples, myCubic, label='cubic')
plt.plot(mySamples, myExponential, label='exponential')
plt.legend()

plt.show()
