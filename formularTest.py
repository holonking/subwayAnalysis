import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

df=pd.DataFrame()
r=10
c=np.array((range(3,30)))
# df['r']=r
# df['c']=c

f1=r/c
print(max(f1))
nf1=f1/max(f1)
df['r/c']=f1
df['n(r/c)']=nf1

print(df)
df.plot()
plt.show()
