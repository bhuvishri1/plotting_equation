import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

def system(t, variables):
    x, y, z = variables
    a = 1.0  # Replace with your desired values for a, b, and c
    b = 2.0
    c = 3.0
    dxdt = a * (y - b)
    dydt = b * x - y - x * z
    dzdt = x * y - c * z
    return [dxdt, dydt, dzdt]

# Define the time span for the integration
t_span = (0, 10)  # Adjust the time range as needed


# Define initial conditions
initial_conditions = [1.0, 2.0, 3.0]  # Replace with your desired initial values for x, y, and z


# Solve the system of differential equations
sol = solve_ivp(system, t_span, initial_conditions, t_eval=np.linspace(t_span[0], t_span[1], 1000))


# Extract the solutions
t = sol.t
x = sol.y[0]
y = sol.y[1]
z = sol.y[2]


# Plot the solutions
plt.figure(figsize=(10, 6))
plt.plot(t, x, label='x(t)')
plt.plot(t, y, label='y(t)')
plt.plot(t, z, label='z(t)')
plt.xlabel('Time (t)')
plt.ylabel('Values')
plt.title('Solutions to the System of Differential Equations')
plt.legend()

plt.grid(True)
plt.show()

