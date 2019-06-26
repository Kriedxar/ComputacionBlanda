from math import exp

# Calculate neuron activation for an input
def activate(weights, inputs):
	activation = weights[-1]
	for i in range(len(weights)-1):
		activation += weights[i] * inputs[i]
	return activation

# Transfer neuron activation
def transfer(activation):
	return 1.0 / (1.0 + exp(-activation))

# Forward propagate input to a network output
def forward_propagate(network, row):
	inputs = row
	for layer in network:
		new_inputs = []
		for neuron in layer:
			activation = activate(neuron['weights'], inputs)
			neuron['output'] = transfer(activation)
			new_inputs.append(neuron['output'])
		inputs = new_inputs
	return inputs

# Make a prediction with a network
def predict(network, row):
	outputs = forward_propagate(network, row)
	return outputs.index(max(outputs))


network = [[{'weights': [-0.7222136884434861, 1.6783069335983907, 0.9659430140366018], 'output': 0.9999731784492195, 'delta': 5.9445522656752265e-06}, {'weights': [4.605769204576073, -2.1188641590297657, -0.9893634597019437], 'output': 0.9999999999574221, 'delta': -3.753395884100543e-11}], [{'weights': [-6.710337864888824, 1.111051143044252, 0.199576826047714], 'output': 0.004498513103731745, 'delta': -2.014558544355119e-05}, {'weights': [-1.080132895323388, 0.5979396950462385, -1.4075383107206278], 'output': 0.1339598661730522, 'delta': -0.015541303026645647}, {'weights': [0.8943063348391809, 0.7773896274280798, -2.9498293509805054], 'output': 0.22832093616056934, 'delta': -0.04022797676805613}, {'weights': [2.306135702353857, 2.4561136936362398, -5.023499656612129], 'output': 0.4795668638837113, 'delta': -0.11969149054616701}, {'weights': [4.305569259382121, -4.295655112616918, -1.2927065571304652], 'output': 0.18718510568264426, 'delta': 0.12366721921415831}]]  

def calcular(eCarretera, riesgold):
	prediction = predict(network,[eCarretera, riesgold])
	return prediction
