import tellurium as te
import os, glob
import matplotlib.pyplot as plt
import matplotlib
import numpy as np

matplotlib.use('Qt5Agg')
import seaborn as sns


ant = """

model toy
   R1: A -> B ; k1*A 
   R2: B -> A ; k2*B
   
   k1 = 0.1;
   k2 = 0.1;
   A=10;
   B=0;
    
end
"""
ant = """

model toy
   R1: A -> B ; vmax*A / (km + A)
   R2: B -> A ; k2*B
   
   vmax=1
   km=5
   k2 = 0.1;
   A=10;
   B=0;
    
end
"""

N = 5


rr = te.loada(ant)
fig = plt.figure()
for i in range(N):
    rr.reset()
    rr.A = np.random.uniform(3, 17, 1)[0]
    data = rr.simulate(0, 100, 101)
    c = iter(['red', 'blue'])
    for j in data.colnames:
        if j.lower() != 'time':
            plt.plot(data['time'], data[j], label=i, color=next(c))
    sns.despine(fig=fig, top=True, right=True)

plt.show()









