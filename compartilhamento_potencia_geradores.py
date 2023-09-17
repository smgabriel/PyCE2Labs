# Codigo solução trabalho 2 -  08/04/2023


import math
import cmath as c
import matplotlib.pyplot as plt

#definindo valores dos geradores:
Snom = 3.75

fn1 = 61.00
fn2 = 61.50
fn3 = 60.50

sd1 = 3.4
sd2 = 3
sd3 = 2.6

f1 = fn1 / ( (sd1/100) +1)
f2 = fn2 / ( (sd2/100) +1)
f3 = fn3 / ( (sd3/100) +1)

print ('f1 = '+ str(f1))
print ('f2 = '+ str(f2))
print ('f3 = '+ str(f3))

spa = Snom /( fn1-f1 )
spb = Snom /( fn2-f2 )
spc = Snom /( fn3-f3 )

print ('spa = '+ str(spa))
print ('spb = '+ str(spb))
print ('spc = '+ str(spc))


cont = 11

x = []
p1 = []
p2 = []
p3 = []

fsys = (spa*f1 + spb*f2 + spc*f3 - 9)/(spa + spb + spc)
print ('fsys = ' + str(fsys))


for Pload in range(cont):

    #for calculate the frequency system
    fsys = (spa*f1 + spb*f2 + spc*f3 - Pload)/(spa + spb + spc)

    #for calculate the power of each generator
    pa = spa*(f1 - fsys)
    pb = spb*(f2 - fsys)
    pc = spc*(f3 - fsys)
   
    p1.append(pa)
    p2.append(pb)
    p3.append(pc)
    x.append(Pload)

plt.plot(x, p1,linestyle = '-', color = 'blue',lw=2.0,label='Gerador A')
plt.plot(x, p2,linestyle = '-', color = 'red',lw=2.0,label='Gerador B')
plt.plot(x, p3,linestyle = '-', color = 'green',lw=2.0,label='Gerador C')
plt.legend()

plt.ylabel("Potência Ativa Fornecida por Cada Gerador (MW)")
plt.xlabel("Potência Total Fornecida à Carga (MW)")

plt.axhline(y = 3.75, color = 'k', linestyle = 'dotted')
plt.text(4, 3.8, 'Limite Potência', fontsize = 8)
plt.text(8.75, 0.1, 'Carga', fontsize = 8,rotation = 90)
plt.axvline(x = 9, color = 'k', linestyle = 'dotted')
plt.title("Compartilhamento de Potência x Carga Total")
plt.xlim(left=0)
plt.xlim(right=10)
plt.grid(True)
plt.show()