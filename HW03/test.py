a = [1,1]
b = [2,2]
c = [10,10]
d = [a,b,c]

s = []
r = []
m = []
p = []

from culc_1 import summ, raz
from culc_2 import mul, pow

for i in d:
	x = summ(i)
	y = raz(i)
	z = mul(i)
	k = pow(i)
	s.append(x)
	r.append(y)
	m.append(z)
	p.append(k)
print(s,r,m,p)