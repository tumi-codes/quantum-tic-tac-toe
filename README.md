🎮 Quantum Tic-Tac-Toe (CLI + Qiskit)

📌 Overview

This project implements a modified version of Tic-Tac-Toe where each player places **two moves per turn**, and integrates it with a quantum circuit using Qiskit.

The game runs in a **Command Line Interface (CLI)** and maps board positions to qubits, demonstrating how classical game logic can be represented in a quantum system.

🚀 Features

* ✅ 3×3 Tic-Tac-Toe board (CLI-based)
* ✅ Two moves per turn (custom game rule)
* ✅ Input validation and error handling
* ✅ Win and draw detection
* ✅ Quantum circuit representation of moves
* ✅ Measurement of board state via simulation

🧠 How It Works

🎲 Classical Game Logic

* Players alternate turns (`X` and `O`)
* Each player selects **two distinct cells per turn**
* The board updates after both moves are validated
* The game checks for:

  * Winner
  * Draw (full board)

---

⚛️ Quantum Mapping

Each board cell is mapped to a qubit:

```
(0,0) → q0   (0,1) → q1   (0,2) → q2
(1,0) → q3   (1,1) → q4   (1,2) → q5
(2,0) → q6   (2,1) → q7   (2,2) → q8
```

Move Encoding:

* Player `X` → applies X gate
* Player `O` → applies Z gate

Each turn:

* Two qubits are modified (representing two moves)
* A barrier separates turns in the circuit

## 🎮 How to Play

* The board uses 0-based indexing
* Input format:

```bash
row col row col
```

Example:

```
0 0 1 1
```

This places marks in:

* Row 0, Col 0
* Row 1, Col 1

⚠️ Limitations

* This implementation uses quantum circuits as a representation, not full quantum gameplay
* No superposition or entanglement yet
* Game logic is still fundamentally classical
If you want, I can next:

* Turn this into a **portfolio-ready GitHub repo (with badges, screenshots, and demos)**
* Or upgrade the README to something that helps you **attract freelance/tech opportunities**
