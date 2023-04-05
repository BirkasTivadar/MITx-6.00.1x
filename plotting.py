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

plt.figure('lin')
plt.plot(mySamples, myLinear)

plt.figure('quad')
plt.plot(mySamples, myQuadratic)

plt.figure('cub')
plt.plot(mySamples, myCubic)

plt.figure('exp')
plt.plot(mySamples, myExponential)

plt.show()
