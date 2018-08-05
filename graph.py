# coding: utf-8
from pylab import *
y=linspace(0,2*pi,50)
plot(y,sin(y))
plot(y,cos(y))
xlabel('y')
ylabel('f(y)')
legend(['sin(y)','cos(y)'])
show()
