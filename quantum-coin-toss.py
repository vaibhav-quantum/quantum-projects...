
from qiskit import QuantumCircuit
from qiskit.visualization import plot_histogram
from qiskit_aer import Aer
from qiskit import transpile

# Create a quantum circuit with 1 qubit and 1 classical bit
qc = QuantumCircuit(1, 1)

# Put the qubit into superposition
qc.h(0)

# Measure the qubit
qc.measure(0, 0)

# Use simulator
simulator = Aer.get_backend('qasm_simulator')
compiled_circuit = transpile(qc, simulator)

# Run the circuit
result = simulator.run(compiled_circuit, shots=1000).result()

# Get and display results
counts = result.get_counts()
plot_histogram(counts)
