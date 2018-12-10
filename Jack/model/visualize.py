import matplotlib.pyplot as plt 
import numpy as np

def sanitizeTensors(ls):
    out = []
    for i in range(len(ls)):
            out.append(int(ls[i][-3:-1]))
    return out


ang = []
with open("ang_acc.blacke","r") as f:
    ang = sanitizeTensors(f.readline()[1:-1].split(","))

angL1 = []
with open("angL1_acc.blacke","r") as f:
    angL1= sanitizeTensors(f.readline()[1:-1].split(","))

angL2 = []
with open("angL2_acc.blacke","r") as f:
    angL2= sanitizeTensors(f.readline()[1:-1].split(","))

kp = []
with open("kp_acc.blacke","r") as f:
    kp= sanitizeTensors(f.readline()[1:-1].split(","))

kpL1 = []
with open("kpL1_acc.blacke","r") as f:
    kpL1= sanitizeTensors(f.readline()[1:-1].split(","))

kpL2 = []
with open("kpL2_acc.blacke","r") as f:
    kpL2= sanitizeTensors(f.readline()[1:-1].split(","))

# kpang = []
# with open("kpang_acc.blacke","r") as f:
#     kpang= sanitizeTensors(f.readline()[1:-1].split(","))

# kpangL1 = []
# with open("kpangL1_acc.blacke","r") as f:
#     kpangL1= sanitizeTensors(f.readline()[1:-1].split(","))

# kpangL2 = []
# with open("kpangL2_acc.blacke","r") as f:
#     kpangL2= sanitizeTensors(f.readline()[1:-1].split(","))

fig, ax = plt.subplots()

overall_opacity = 0.6

# red
plt.plot(ang,   alpha = overall_opacity, label="BLACangle")
plt.plot(angL1, alpha = overall_opacity, label="BLACangle L1")
plt.plot(angL2, alpha = overall_opacity, label="BLACangle L2")

# green
plt.plot(kp,   alpha = overall_opacity, label="BLACkp")
plt.plot(kpL1, alpha = overall_opacity, label="BLACkp L1")
plt.plot(kpL2, alpha = overall_opacity, label="BLACkp L2")

# # yellow for combined model
# plt.plot(kpang,   alpha = overall_opacity, label="BLACkpangle")
# plt.plot(kpangL1, alpha = overall_opacity, label="BLACkpangle L1")
# plt.plot(kpangL2, alpha = overall_opacity, label="BLACkpangle L2")

plt.title("accuracies of BLAC networks over training")
plt.xlabel("Epoch")
plt.ylabel("Accuracy in %")
plt.legend(loc = 4)
ax.set_ylim(0,100)
plt.show()