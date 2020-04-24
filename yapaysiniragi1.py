from numpy import exp,array,random,dot,mean,abs
import numpy
girdi=array([[0,0],[0,1],[1,0]])
sonuc=array([[0,1,1]]).T
agirlik=array([[1.0,1.0,1.0]]).T

for tekrarsayisi in range(100000):
    hücredegeri=dot(girdi,agirlik)
    tahmin=1/(1+(exp(-hücredegeri))
    a= a+ dot(girdi.T,((sonuc-tahmin)) * tahmin * (1-tahmin))))
    print(str(numpy.mean(numpy.abs(sonuc - tahmin))))