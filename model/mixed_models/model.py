import torch.nn.functional as F
import torch.nn as nn

class BLACkpang(nn.Module):
    def __init__(self):
        super(BLACkpang, self).__init__()

        self.fc1 = nn.Linear(98,200)
        self.fc2 = nn.Linear(200,128)
        self.fc3 = nn.Linear(128,4)

    def forward(self,x):
        
        out = self.fc1(x)
        out = F.relu(out)
        out = self.fc2(out)
        out = F.relu(out)
        out = self.fc3(out)

        return out