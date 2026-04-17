import torch.nn as nn
import torch

class RNN(nn.Module):

    def __init__(self, input_size, hidden_size = 128, num_of_layers = 1):

        super().__init__()

        self.hidden_size = hidden_size
        self.num_of_layers = num_of_layers

        self.rnn = nn.RNN(input_size, hidden_size, num_of_layers, batch_first = True)

        self.fc = nn.Linear(hidden_size, 1)

    def forward(self, x):
        h0 = torch.zeros(self.num_of_layers, x.size(0), self.hidden_size).to(x.device)
        out, _ = self.rnn(x, h0) # (batch_size, seq_size, hidden_size)
        out = self.fc(out[:,-1,:])

        return out