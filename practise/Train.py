import math

# ---------- Data ----------
# One training example, 2 inputs
x = [1.0, 2.0]
y_true = [0, 1]  # Class 1 is the correct class

# ---------- Parameters ----------
# Hidden neuron
w1, w2 = 0.1, 0.2
b_h = 0.0

# Output layer weights (2 classes)
w3, w4 = 0.3, -0.2  # weights from hidden to output classes
b_o1, b_o2 = 0.0, 0.0

# Learning rate
lr = 0.1

# ---------- Forward Pass ----------
# Hidden neuron output (identity activation)
h = w1*x[0] + w2*x[1] + b_h

# Output layer logits
z1 = w3*h + b_o1
z2 = w4*h + b_o2

# Softmax
exp_z1 = math.exp(z1)
exp_z2 = math.exp(z2)
sum_exp = exp_z1 + exp_z2
y_pred = [exp_z1 / sum_exp, exp_z2 / sum_exp]

# Cross-entropy loss
loss = - (y_true[0]*math.log(y_pred[0]) + y_true[1]*math.log(y_pred[1]))

print(f"Hidden output h: {h}")
print(f"Softmax prediction: {y_pred}")
print(f"Loss: {loss}")

# ---------- Backpropagation ----------
# Output layer error (softmax + cross-entropy)
delta_o1 = y_pred[0] - y_true[0]
delta_o2 = y_pred[1] - y_true[1]

# Gradients for output layer
dw3 = delta_o1 * h
dw4 = delta_o2 * h
db_o1 = delta_o1
db_o2 = delta_o2

# Hidden neuron error
delta_h = delta_o1*w3 + delta_o2*w4

# Gradients for hidden layer
dw1 = delta_h * x[0]
dw2 = delta_h * x[1]
db_h = delta_h

# ---------- Update weights ----------
w1 -= lr * dw1
w2 -= lr * dw2
b_h -= lr * db_h
w3 -= lr * dw3
w4 -= lr * dw4
b_o1 -= lr * db_o1
b_o2 -= lr * db_o2

print("\nUpdated weights and biases:")
print(f"w1: {w1}, w2: {w2}, b_h: {b_h}")
print(f"w3: {w3}, w4: {w4}, b_o1: {b_o1}, b_o2: {b_o2}")