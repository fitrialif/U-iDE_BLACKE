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

import matplotlib.pyplot as plt
overall_loss = []

from model import *

# device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
device = 'cpu'

dt = pandas.read_csv("data.csv", header=None)
dt.head()
dataset = dt.values
dataset = dataset[1:]

x = dataset[:,0:-1]
t = dataset[:,-1]

encoder = LabelEncoder()
encoder.fit(t)
t = encoder.transform(t)

x_tr, x_te, t_tr, t_te = train_test_split(x,t,test_size = 0.1)

x_tr = torch.FloatTensor(x_tr)
t_tr = torch.LongTensor(t_tr)
x_te,t_te = torch.FloatTensor(x_te),torch.LongTensor(t_te)

trainset = torch.utils.data.TensorDataset(x_tr,t_tr)
testset  = torch.utils.data.TensorDataset(x_te,t_te)

trainloader = torch.utils.data.DataLoader(dataset = trainset,
                                            batch_size=5,
                                            shuffle=True)
testloader  = torch.utils.data.DataLoader(dataset = testset,
                                            batch_size=5,
                                            shuffle=True)

model = BLACkp1().to(device)
criterion = nn.CrossEntropyLoss()
# optimizer = torch.optim.SGD(model.parameters(),lr=0.01)
optimizer = torch.optim.SGD(model.parameters(),lr=0.01)


def train(epoch):
    model.train()
    optimizer.lr = 1/epoch

    epoch_loss = []
    for batch_ind, (data, target) in enumerate(trainloader):
        
        data = Variable(data).to(device)
        target = Variable(target).to(device)

        optimizer.zero_grad()
        output = model(data)

        loss = F.cross_entropy(output,target)
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

    
    for batch_ind, (data, target) in enumerate(testloader):
        
        data = Variable(data).to(device)
        target = Variable(target).to(device)

        output = model(data)

        test_loss += F.cross_entropy(output, target, size_average=False).data[0]

        pred = output.data.max(1, keepdim=True)[1]
        correct += pred.eq(target.data.view_as(pred)).cpu().sum()

    test_loss /= len(testloader.dataset)

    print('\nTest set: Average loss: {:.4f}, Accuracy: {}/{} ({:.0f}%)\n'.format(
        test_loss, correct, len(testloader.dataset),
        100. * correct / len(testloader.dataset)
    ))

    


for epoch in range(1,1000):
    train(epoch)
    torch.save(model.state_dict(),'model.pt') # make .pt file have different names

test()

plt.plot(overall_loss)

plt.show()