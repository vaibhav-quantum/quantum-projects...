# 2 QUBIT STATE

from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt


qc = QuantumCircuit(2, 2)

qc.h(0)
qc.h(1)

qc.measure([0,1], [0,1])

simulator = AerSimulator()
compiled_circuit = transpile(qc, simulator)
job = simulator.run(compiled_circuit, shots=2048)
result = job.result()
counts = result.get_counts()


plot_histogram(counts)
plt.title("2-Qubit Uniform Superposition (4 States)")
plt.savefig("../outputs/2_qubit_histogram.png")
plt.close()


# 3 QUBIT STATE

qc = QuantumCircuit(3, 3)

qc.h(0)
qc.h(1)
qc.h(2)

qc.measure([0, 1, 2], [0, 1, 2])

simulator = AerSimulator()
compiled_circuit = transpile(qc, simulator)
job = simulator.run(compiled_circuit, shots=4096)
result = job.result()
counts = result.get_counts()


plot_histogram(counts)
plt.title("3-Qubit Uniform Superposition (8 States)")
plt.savefig("../outputs/3_qubit_histogram.png")
plt.close()
