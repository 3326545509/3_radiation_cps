import numpy as np
from matplotlib import pyplot as plt
import os
from scipy import stats

radfenjie=float(os.sys.argv[1])
time=os.sys.argv[2]
houzui=os.sys.argv[3]

def read(file):
    with open(file,'r')as f:
        data=f.read()
        data=data.split()
    data=np.array(data[1:])
    data=data.astype(float)
    return data

def var_fit(x,y,slope,intercept):
    y2=x*slope+intercept
    if x==[] or y==[]:
        return 0
    mean=sum((y2-y)**2)/len(y2)
    return mean


depmax  =read('0.'+ houzui+ 'depmax')
dist    =read('0.'+ houzui+ 'dist')
rad     =read('2_'+  houzui+ 'rad')
baz     =read('0.'+ houzui+ 'baz')

#dist depmax rad: 剔除后的数据

depmax_norad=[]
for i in range(len(rad)):
    if rad[i]<radfenjie:
        depmax_norad.append('node')
    else:
        depmax_norad.append(str(round((depmax[i]/rad[i]),4)))

depmax_norad=['depmax_norad_withgeo']+depmax_norad

with open('depmax_norad_withgeo'+houzui+'.txt','w')as f:
    f.write("\n".join(depmax_norad))

os.system('mv '+houzui+'.rad '+time+'.'+houzui+'.rad')
