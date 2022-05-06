import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

WS = pd.read_excel("D:\MUSI7100-ChordWiki\Result.xlsx")
WS_np = np.array(WS)

#x = ['1980s', '1990s', '2000s', '2010s', '2020s']
x = [1980, 1990, 2000, 2010, 2020]
J_pop = []
Canon = []
Komuro = []
_251 = []
_451 = []
_456 = []
_6415 = []
for i in np.arange(start=8, stop=13):
    J_pop.append(WS_np[0][i])
    Canon.append(WS_np[1][i])
    Komuro.append(WS_np[2][i])
    _251.append(WS_np[3][i])
    _451.append(WS_np[4][i])
    _456.append(WS_np[5][i])
    _6415.append(WS_np[6][i])

plt.figure()
plt.plot(x, J_pop, color='g', label="J-pop/Oudou")
plt.plot(x, Canon, color='r', label="Canon")
plt.plot(x, Komuro, color='b', label="Komuro")
plt.plot(x, _251, color='y', label="251")
plt.plot(x, _451, color='c', label="451")
plt.plot(x, _456, color='m', label="456")
plt.plot(x, _6415, color='k', label="6415")
plt.xlabel("Year of release")
plt.ylabel("Used per song")
plt.legend()
plt.show()

print()