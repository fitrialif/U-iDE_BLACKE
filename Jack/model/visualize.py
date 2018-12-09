import matplotlib.pyplot as plt 
import numpy as np

def sanitizeTensors(ls):
    out = []
    for i in range(len(ls)):
        out.append(np.asarray(ls[i]))

    return out

ang = []
with open("ang_acc.blacke","r") as f:
    ang = sanitizeTensors(f.readline().split(","))

angL1 = []
with open("angL1_acc.blacke","r") as f:
    angL1= sanitizeTensors(f.readline().split(","))

angL2 = []
with open("angL2_acc.blacke","r") as f:
    angL2= sanitizeTensors(f.readline().split(","))

kp = []
with open("kp_acc.blacke","r") as f:
    kp= sanitizeTensors(f.readline().split(","))

kpL1 = []
with open("kpL1_acc.blacke","r") as f:
    kpL1= sanitizeTensors(f.readline().split(","))

kpL2 = []
with open("kpL2_acc.blacke","r") as f:
    kpL2= sanitizeTensors(f.readline().split(","))

plt.figure()
plt.title("accuracies of BLAC networks")

plt.plot(ang)
plt.plot(angL1)
plt.plot(angL2)
plt.plot(kp)
plt.plot(kpL1)
plt.plot(kpL2)


plt.show()