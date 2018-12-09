import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from torchvision import datasets, transforms
from torch.autograd import Variable

import pandas
import numpy as np

from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
import itertools

import matplotlib.pyplot as plt
overall_loss = []

from model import *
from tools import *

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

dt = pandas.read_csv("angle_models/data.csv", header=None)
dt.head()
dataset = dt.values
dataset = dataset[1:]

x = dataset[:,0:-1]
t = dataset[:,-1]

encoder = LabelEncoder()
encoder.fit(t)
t = encoder.transform(t)

x_tr, x_te, t_tr, t_te = train_test_split(x,t,test_size = 0.3)

x_tr = torch.FloatTensor(x_tr)
t_tr = torch.LongTensor(t_tr)
x_te,t_te = torch.FloatTensor(x_te),torch.LongTensor(t_te)

trainset = torch.utils.data.TensorDataset(x_tr,t_tr)
testset  = torch.utils.data.TensorDataset(x_te,t_te)

trainloader = torch.utils.data.DataLoader(dataset = trainset,
                                            batch_size=5,
                                            shuffle=True)
testloader  = torch.utils.data.DataLoader(dataset = testset,
                                            batch_size=1,
                                            shuffle=True)

model = BLACangle().to(device)
criterion = nn.CrossEntropyLoss()
optimizer = torch.optim.SGD(model.parameters(),lr=0.01)

all_params = torch.cat([x.view(-1) for  x in model.parameters()])

def train(epoch):
    model.train()
    optimizer.lr = 1/epoch

    epoch_loss = []
    for batch_ind, (data, target) in enumerate(trainloader):
        
        data = Variable(data).to(device)
        target = Variable(target).to(device)

        optimizer.zero_grad()
        output = model(data)

        loss = F.cross_entropy(output,target) + 0.01*torch.norm(all_params,1)
        epoch_loss.append(loss.data)
        loss.backward()
        optimizer.step()

        if batch_ind%10 == 0:
            print('epoch: {} [{}/{} ({:.0f}%)]\tLoss: {:.6f}'.format(
                epoch, batch_ind*len(data),len(trainloader.dataset),
                100. * batch_ind/len(trainloader), loss.data
            ))

    overall_loss.append(np.mean(epoch_loss))

def test():
    model.eval()
    test_loss = 0
    correct = 0 
    
    t_predictions = []

    for batch_ind, (data, target) in enumerate(testloader):
        
        data = Variable(data).to(device)
        target = Variable(target).to(device)

        output = model(data)

        test_loss += F.cross_entropy(output, target, size_average=False).data

        pred = output.data.max(1, keepdim=True)[1]
        t_predictions.append(pred)
        correct += pred.eq(target.data.view_as(pred)).cpu().sum()

    test_loss /= len(testloader.dataset)

    accuracy = 100. * correct / len(testloader.dataset)

    print('\nTest set: Average loss: {:.4f}, Accuracy: {}/{} ({:.0f}%)\n'.format(
        test_loss, correct, len(testloader.dataset), accuracy
    ))

    return torch.FloatTensor(t_predictions), accuracy

accuracies = []

## TRAINING
for epoch in range(1,700):
    train(epoch)
    _,accuracy = test()
    accuracies.append(accuracy)
    torch.save(model.state_dict(),'angL1.pt') # make .pt file have different names

## LOSS
plt.figure()
plt.title("loss over epochs")
plt.plot(overall_loss)

## accuracies
plt.figure()
plt.title("accuracy over epochs")
plt.plot(accuracies)

## Confusion Matrix
t_pred,_ = test()
torch.reshape(t_pred,(-1,))
cnf_matrix = confusion_matrix(np.asarray(t_te), t_pred)
plt.figure()
class_names=("angry","fear","happy","sad")
plot_confusion_matrix(cnf_matrix, classes=class_names, normalize=True,
                      title='Confusion Matrix')

# plt.show()

with open("angL1_acc.blacke","w") as f:
    f.write(str(accuracies))