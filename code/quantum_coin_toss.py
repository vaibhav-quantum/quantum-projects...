import os
from qiskit import QuantumCircuit
from qiskit.visualization import plot_histogram
from qiskit_aer import Aer
from qiskit import transpile

# Ensure outputs directory exists
#os.makedirs("../outputs", exist_ok=True)

# Create a quantum circuit with 1 qubit and 1 classical bit
qc = QuantumCircuit(1, 1)

# Put qubit into superposition
qc.h(0)

# Measure
qc.measure(0, 0)

# Simulator
simulator = Aer.get_backend('qasm_simulator')
compiled = transpile(qc, simulator)
result = simulator.run(compiled, shots=1000).result()

counts = result.get_counts()

# Save histogram
fig = plot_histogram(counts)
fig.savefig("../quantum-coin-toss/outputs/histogram.png")

print("Histogram saved in outputs/")
print("Counts:", counts)
