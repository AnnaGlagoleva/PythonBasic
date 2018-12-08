from culc_1 import summ, raz
from culc_2 import mul, pow


# Test-cases
a = [1,1]
b = [2,2]
c = [10,10]

# Links to cases
d = [a,b,c]

# Results
s = []
r = []
m = []
p = []

for i in d:
	x = summ(i)
	y = raz(i)
	z = mul(i)
	k = pow(i)

	s.append(x)
	r.append(y)
	m.append(z)
	p.append(k)



print('Test cases', [a,b,c], '\n')
print('Sum results', s)
print('Minuese results', r)
print('Multipuls results', m)
print('Powers results', p)



