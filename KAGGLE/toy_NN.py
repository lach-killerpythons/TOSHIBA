import numpy as np
X=np.array([[0,0,1],[0,1,1], [1,1,1]])
y=np.array([[0,1,1,0]]).T
syn0=2*np.random.random((3,4))-1
syn1=2*np.random.random((4,1))-1
print(syn0)
print(syn1)
for j in xrange(10000):
    L1 = 1/(1+np.exp(-(np.dot(X,syn0))))
    L2 = 1/(1+np.exp(-(np.dot(L1,syn1))))
    print(L2, "yada")
    L2_delta = (y-L2)*(L2*(1-L2))
    L1_delta = L2_delta.dot(syn1.T)*(L1*(1-L1))
    syn1 += L1.T.dot(L2_delta)
    syn0 += X.T.dot(L1_delta)
