import qiskit
from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

class QuantumBackend:
    def __init__(self):
        self.qc = QuantumCircuit(9, 9)
        self.simulator = AerSimulator()

    def apply_entangled_move(self, sq1, sq2):
        self.qc.h(sq1)
        self.qc.x(sq2)
        self.qc.cx(sq1, sq2)

    def measure_and_collapse(self):
        # Apply measurement gates to all 9 qubits
        self.qc.measure(range(9), range(9))
        result = self.simulator.run(self.qc, shots=1).result()
        counts = result.get_counts()

        measured_state = list(counts.keys())[0]
        return measured_state[::-1]