import numpy as np

inputs = [1, 2, 3, 2.5]
weights = [[0.2, 0.8, -0.5, 1.0], [0.5, -0.91, 0.26, -0.5], [-0.26, -0.27, 0.17, 0.87]]
biases = [2, 3, 0.5]
layers_output = []

output=np.dot(weights,inputs)+biases
print(output)
'''
for neuron_weights, neuron_bias in zip(weights, biases):
    neuron_output = 0
    for n_output, weight in zip(inputs, neuron_weights):
        neuron_output += neuron_bias
        layers_output.append(neuron_output)
print(layers_output)
'''