import torch.nn.functional as F
import torch.nn as nn

class BLACkp(nn.Module):
    def __init__(self):
        super(BLACkp1, self).__init__()

        self.fc1 = nn.Linear(75,10)
        self.fc2 = nn.Linear(10,10)
        self.fc3 = nn.Linear(10,4)

    def forward(self,x):
        
        out = self.fc1(x)
        out = F.relu(out)
        out = self.fc2(out)
        out = F.relu(out)
        out = self.fc3(out)
        # out = nn.Softmax(out)

        return out

class BLACangle(nn.Module):
    def __init__(self):
        super(BLACkangle1, self).__init__()

        self.fc1 = nn.Linear(48,10)
        self.fc2 = nn.Linear(10,10)
        self.fc3 = nn.Linear(10,4)

    def forward(self,x):
        
        out = self.fc1(x)
        out = F.relu(out)
        out = self.fc2(out)
        out = F.relu(out)
        out = self.fc3(out)
        # out = nn.Softmax(out)

        return out