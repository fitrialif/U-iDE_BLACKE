import torch.nn.functional as F
import torch.nn as nn

class BLACK(nn.Module):
    def __init__(self):
        super(BLACK, self).__init__()

        self.c1 = nn.Conv1d(48,48,2) #kernel size 2
        self.p1 = nn.AvgPool1d(2)

        self.fc1 = nn.Linear(24,10)
        self.fc2 = nn.Linear(10,10)
        self.fc3 = nn.Linear(10,7)

    def forward(self,x):
        
        out = self.c1(x)
        out = self.p1(out)
        out = self.fc1(out)
        out = F.relu(out)
        out = self.fc2(out)
        out = F.relu(out)
        out = self.fc3(out)

        return out