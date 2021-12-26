# Neural Networks from Scratch - P.2 Coding a Layer
# https://www.youtube.com/watch?v=lGLto9Xd7bU

inputs = [1, 2, 3, 2.5]
weights = [0.2, 0.8, -0.5, 1.0]
bias = 2

output = inputs[0] * weights[0] + inputs[1] * weights[1] + inputs[2] * weights[2] + inputs[3] * weights[3]+ bias
print(output)