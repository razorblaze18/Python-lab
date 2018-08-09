p=input('enter the principle amount=')
r=input('rate of interest is=')
t=input('time period=')
n=input('enter the value of n=')
SI=p*r*t/100
print SI
CI=p*(1+(r/n))**(n*t)
print CI
