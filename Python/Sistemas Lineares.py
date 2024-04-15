#solving linear systems

import random 
def rand():
	k=random.randrange(1,10)
	return k

#this creates a random nxn triangular superior matrix and its "result" (b)
def rand_upp_m():
	m=[]
	n=rand()
	for i in range(n):
		mi=[]
		for j in range(n):
			if i-j>0:
				mi.append(0)
			else:
				r=rand()
				mi.append(r)
		m.append(mi)
	
	b=[]
	for i in range(n):
		b.append(rand())
	return [m,b]

#this create a random nxn matrix and its "result" (b)
def rand_m():
	m=[]
	n=rand()
	for i in range(n):
		mi=[]
		for j in range(n):
			r=rand()
			mi.append(r)
		m.append(mi)
	
	b=[]
	for i in range(n):
		b.append(rand())
	return [m,b]


#this solves triangular upper matrixes linear systems
def u_lin_sys(m,b):
	n=len(m)
	sol_r=[]
	x_j=0
	m_aux=0
	for j in range(n-1,-1,-1):
		k=n-1
		while k != j:
			m_aux=m_aux+(m[j][k]*sol_r[n-1-k])
			k=k-1
		x_j=(b[j]-m_aux)/m[j][j]
		sol_r.append(x_j)
		m_aux=0
	sol=list(reversed(sol_r))
	return sol

#now we want to transform a non-triangular to a triangular matrix that represents the same linear system
def gauss(m,b):
    n=len(m)
    for i in range(n):
        k=n-1
        o=0
        while i!=k and o<1000*n:
            if m[i][i]==0:
                for j in range(i,n):
                    if m[j][i]!=0:
                        m[i][i],m[j][i]=m[j][i],m[i][i]
                        break
            if m[k][i]!=0:
                mult=m[i][i]/m[k][i]
                m[k]=[x * mult for x in m[k]]
                b[k]=mult*b[k]
                m[k]=[i - j for i, j in zip(m[k], m[i])]
                b[k]=b[k]-b[i]
            k=k-1
            o=o+1
    return [m,b]


def roundm(m):
    n=len(m)
    for i in range(n):
        for j in range(n):
            m[i][j]="%.2f" % m[i][j]
            m[i][j]=float(m[i][j])
    return m
def roundb(b):
    n=len(b)
    for i in range(n):
        b[i]="%.2f" % b[i]
        b[i]=float(b[i])
    return b



l=rand_m()  
g=gauss(l[0],l[1])
g[0]=roundm(g[0])
g[1]=roundb(g[1])
sol=u_lin_sys(g[0],g[1])
sol=roundb(sol)
print(l)
print(g)
print(sol)