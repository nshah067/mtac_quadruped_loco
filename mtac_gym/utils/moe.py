import torch
import torch.nn as nn
import torch.nn.functional as F
import task_registry
import torch.optim as optim
import numpy as np

class Expert(nn.Module):
    def __init__(self, env, task):
        super(Expert, self).__init__()
        #Load a pretrained policy based on task
        self.ppo_runner, self.train_cfg = task_registry.make_alg_runner(env=env, name=task, args=None, train_cfg=self.train_cfg)
        self.train_cfg.runner.resume = True
        self.policy = self.ppo_runner.get_inference_policy(device=env.device)

    #Forward pass of the input token through the pretrained expert
    def forward(self):
        return self.policy(self.obs.detach())

class RoutingNetwork(nn.Module):
    #Top1 routing method implemented
    def __init__(self, tasks, envs, num_experts=3):
        self.tasks = tasks
        self.envs = envs
        super(RoutingNetwork, self).__init__()
        self.num_experts = num_experts 
        self.experts = nn.ModuleList([Expert(envs[i], tasks[i]) for i in range(num_experts)])
        self.routing_weights = nn.Parameter(torch.rand(num_experts))

    def forward(self, obs):
        expert_outputs = torch.stack([expert(obs) for expert in self.experts], dim=1)  # Stack outputs of all experts
        routing_logits = F.softmax(self.routing_weights, dim=0)  # Compute routing logits
        
        # Weighted sum of expert outputs based on routing probabilities
        weighted_expert_outputs = torch.sum(expert_outputs * routing_logits.view(1, -1, 1), dim=1)
        
        return weighted_expert_outputs

class Moe(nn.Module):
    def __init__(self, input_dim, output_dim, num_experts):
        super(Moe, self).__init__()
        self.routing_network = RoutingNetwork(input_dim, num_experts)

    def forward(self, x):
        x = self.routing_network(x)
        return x

def train():
    model = Moe(input_dim=10, output_dim=10, num_experts=3)
    criterion = nn.CrossEntropyLoss()
    optimizer = optim.Adam(model.parameters(), lr=0.001)

    # Training loop
    num_epochs = 10
    for epoch in range(num_epochs):
        running_loss = 0.0
        for i, (inputs, labels) in enumerate(dataloader):
            optimizer.zero_grad()

            # Forward pass
            outputs = model(inputs)

            # Compute loss
            loss = criterion(outputs, labels)

            # Backward pass and optimization
            loss.backward()
            optimizer.step()

            # Print statistics
            running_loss += loss.item()
            if (i + 1) % 10 == 0:  # Print every 10 mini-batches
                print(f"Epoch [{epoch + 1}/{num_epochs}], Step [{i + 1}/{len(dataloader)}], Loss: {running_loss / 10:.4f}")
                running_loss = 0.0

    print("Finished Training")