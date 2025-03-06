import matplotlib.pyplot as plt
import numpy as np

# Define the sequence
numbers = [1, 3, 2, 6, 3, 11, 4, 18, 5, 27]

# Define x positions (equal spacing)
x = np.arange(len(numbers))

# Define y positions (wave effect)
y = [1 if i % 2 == 0 else 2 for i in range(len(numbers))]  # Alternating heights

# Plot points
plt.figure(figsize=(10, 5))
plt.plot(x, y, 'ko-', markersize=10)  # Solid black line connecting points

# Annotate numbers on points
for i, num in enumerate(numbers):
    plt.text(x[i], y[i] + 0.1, str(num), fontsize=12, ha='center', fontweight='bold')

# Draw curved arrows for transitions
for i in range(len(numbers) - 1):
    dx = x[i+1] - x[i]
    dy = y[i+1] - y[i]
    curvature = 0.3 if i % 2 == 0 else -0.3  # Alternate curve direction
    plt.annotate("",
                 xy=(x[i+1], y[i+1]), xytext=(x[i], y[i]),
                 arrowprops=dict(arrowstyle="<-", lw=1.5, color='black', 
                                 connectionstyle=f"arc3,rad={curvature}"))

# Hide axes for clean look
plt.xticks([])
plt.yticks([])
plt.axis('off')

plt.title("Wave-Like Number Sequence", fontsize=14)
plt.show()
