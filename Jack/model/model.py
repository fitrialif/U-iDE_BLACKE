import torch.nn.functional as F
import torch.nn as nn

class BLAC(nn.Module):
    def __init__(self):
        super(BLAC, self).__init__()
        self.fc1 = nn.Linear(210,100)
        self.fc2 = nn.Linear(100,10)
        self.fc3 = nn.Linear(10,7)

    def forward(self,x):

        # out = F.relu(self.fc1(x))
        # out = F.relu(self.fc2(x))
        
        out = self.fc1(x)
        out = F.relu(out)
        out = self.fc2(out)
        out = F.relu(out)
        out = self.fc3(out)

        return out