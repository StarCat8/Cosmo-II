import matplotlib.pyplot as plt
import numpy as np
from matplotlib import colors
from matplotlib.ticker import PercentFormatter

#integrare

def f(z, Om, Ok, Olambda, c, H_0):
    return c/(H_0*(Om*(1+z)**3 + Ok*(1+z)**2 + Olambda)**0.5)

n_bins = 12



# We can set the number of bins with the *bins* keyword argument.
s = np.random.normal(-0.011, 0.013, 150)
d_VH = np.zeros(200)
d_PH = np.zeros(200)
for I in range(len(s)):
    t_start=0
    t_end=11000.
    n=4
    t_step= 10**(-n)
    Om = 0.315
    Ok = s[I]
    Olambda = 1.0 - Om - Ok
    c = 2.997*10**5 #km/s
    H_0 = 67.4      #km/s/Mpc
    t = t_start
    k = 0
    i=0
    while (t < t_end):
        f_t1 = f(t, Om, Ok, Olambda, c, H_0)
        k = k + f_t1 * t_step
        t = t + t_step
        f_t2 = f(t, Om, Ok, Olambda, c, H_0)
        k_2 = 0.5 * t_step * (f_t2-f_t1)
        k = k+k_2
        if t < t_end/10:
            d_VH[I] = k
        if i==15000000:
            t_step = t_step*10
        if(int(t)%1000==0):
            print(t)
        i=i+1
        d_PH[I]=k
    o = round(k, n)
    print("%.15f" %k)

fig, axs = plt.subplots(1, 2, sharey=True, tight_layout=True)
axs[0].hist(a, bins=n_bins)
axs[1].hist(s, bins=n_bins)
plt.show()

axs[0].hist(a, bins=n_bins)


axs[1].hist(dist2, bins=n_bins)


(14256.683680594009275 - 14256.683677502878709)*10**6
14256.683680594009275









































































import numpy as np

#integrare

def f(z, Om, Ok, Olambda, c, H_0):
    return c/(H_0*(Om*(1+z)**3 + Ok*(1+z)**2 + Olambda)**0.5)


t_start=0
t_end=11000.
n=4
t_step= 10**(-n)
Om = 0.315
Ok = 0
Olambda = 1.0 - Om - Ok
c = 2.997*10**5 #km/s
H_0 = 67.4      #km/s/Mpc

t = t_start
k = 0
while (t < t_end):
    f_t1 = f(t, Om, Ok, Olambda, c, H_0)
    k = k + f_t1 * t_step
    t = t + t_step
    f_t2 = f(t, Om, Ok, Olambda, c, H_0)
    k_2 = 0.5 * t_step * (f_t2-f_t1)
    k = k+k_2
    if(int(t)%100==0):
        print(t)

o = round(k, n)

print(k/10**3*3.26156)

import numpy as np

#integrare

def f(z, Om, Ok, Olambda, c, H_0):
    return c/(H_0*(Om*(1+z)**3 + Ok*(1+z)**2 + Olambda)**0.5)


t_start=0
t_end=11000.
n=4
t_step= 10**(-n)
Om = 0.315
Ok = 0
Olambda = 1.0 - Om - Ok
c = 2.997*10**5 #km/s
H_0 = 67.4      #km/s/Mpc

t = t_start
k = 0
while (t < t_end):
    f_t1 = f(t, Om, Ok, Olambda, c, H_0)
    k = k + f_t1 * t_step
    t = t + t_step
    f_t2 = f(t, Om, Ok, Olambda, c, H_0)
    k_2 = 0.5 * t_step * (f_t2-f_t1)
    k = k+k_2
    if(int(t)%100==0):
        print(t)

o = round(k, n)

print(k/10**3*3.26156)

t_start=0
t_end=11000.
n=4
t_step= 10**(-n)
Om = 0.315
Ok = -0.011
Olambda = 1.0 - Om - Ok
c = 2.997*10**5 #km/s
H_0 = 67.4      #km/s/Mpc

t = t_start
k = 0
while (t < t_end):
    f_t1 = f(t, Om, Ok, Olambda, c, H_0)
    k = k + f_t1 * t_step
    t = t + t_step
    f_t2 = f(t, Om, Ok, Olambda, c, H_0)
    k_2 = 0.5 * t_step * (f_t2-f_t1)
    k = k+k_2
    if(int(t)%100==0):
        print(t)

print("PARTICLE HORIZON -0.011")
o = round(k, n)

print(k/10**3*3.26156)

t_start=0
t_end=11000.
n=4
t_step= 10**(-n)
Om = 0.315
Ok = -0.024
Olambda = 1.0 - Om - Ok
c = 2.997*10**5 #km/s
H_0 = 67.4      #km/s/Mpc

t = t_start
k = 0
while (t < t_end):
    f_t1 = f(t, Om, Ok, Olambda, c, H_0)
    k = k + f_t1 * t_step
    t = t + t_step
    f_t2 = f(t, Om, Ok, Olambda, c, H_0)
    k_2 = 0.5 * t_step * (f_t2-f_t1)
    k = k+k_2
    if(int(t)%100==0):
        print(t)

print("VISIBLE HORIZON 0.002")
o = round(k, n)


print(k/10**3)

t_start=0
t_end=11000.
n=4
t_step= 10**(-n)
Om = 0.315
Ok = 0.002
Olambda = 1.0 - Om - Ok
c = 2.997*10**5 #km/s
H_0 = 67.4      #km/s/Mpc

t = t_start
k = 0
while (t < t_end):
    f_t1 = f(t, Om, Ok, Olambda, c, H_0)
    k = k + f_t1 * t_step
    t = t + t_step
    f_t2 = f(t, Om, Ok, Olambda, c, H_0)
    k_2 = 0.5 * t_step * (f_t2-f_t1)
    k = k+k_2
    if(int(t)%100==0):
        print(t)

o = round(k, n)

print("PARTICLE HORIZON 0.002")
print(k/10**3*3.26156)
