from quantum import QuantumBackend

class QuantumTicTacToe:
    def __init__(self):
       self.board = [[] for _ in range(9)] 
       self.collapsed_board = [' ' for _ in range(9)]
        
       self.current_player = 'X'
       self.turn_num = 1
       self.is_collapsed = False
       self.moves_history = []

       self.backend = QuantumBackend()

    def display_board(self):
        print("\n" + "="*30)
        target_board = self.collapsed_board if self.is_collapsed else self.board
        
        for i in range(0, 9, 3):
            row_display = []
            for j in range(3):
                if self.is_collapsed:
                    cell_content = target_board[i+j]
                else:
                    cell_content = ",".join(target_board[i+j]) if target_board[i+j] else " "
                row_display.append(f"{cell_content:^7}")
            
            print(" | ".join(row_display))
            if i < 6:
                print("-" * 29)
        print("="*30 + "\n")

    def play_quantum_move(self, sq1, sq2):
        if sq1 < 0 or sq1 > 8 or sq2 < 0 or sq2 > 8:
            print("Invalid squares. Must be between 0 and 8.")
            return

        move_label = f"{self.current_player}{self.turn_num}"
    
        self.board[sq1].append(move_label)
        self.board[sq2].append(move_label)
        self.moves_history.append({
            'player': self.current_player,
            'label': move_label,
            'sq1': sq1,
            'sq2': sq2
        })

        self.backend.apply_entangled_move(sq1, sq2)
        self.current_player = 'O' if self.current_player == 'X' else 'X'
        if self.current_player == 'X':
            self.turn_num += 1

    def collapse(self):
        print("Initiating state collapse...")
        
        # Get the collapsed binary string from the simulator
        measured_state = self.backend.measure_and_collapse()

        # Reset collapsed board
        self.collapsed_board = [' ' for _ in range(9)]

        # Map quantum results to the classical board based on move history
        for move in self.moves_history:
            s1, s2 = move['sq1'], move['sq2']
            player = move['player']
            
            # Whichever entangled qubit measured as '1' gets the definitive classical mark
            if measured_state[s1] == '1' and self.collapsed_board[s1] == ' ':
                self.collapsed_board[s1] = player
            elif measured_state[s2] == '1' and self.collapsed_board[s2] == ' ':
                self.collapsed_board[s2] = player

        self.is_collapsed = True
        print("Reality has chosen an outcome!")

    def check_win(self):
        if not self.is_collapsed:
            return None

        winning_lines = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Rows
            (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Columns
            (0, 4, 8), (2, 4, 6)              # Diagonals
        ]

        x_wins = 0
        o_wins = 0

        for line in winning_lines:
            a, b, c = line
            if self.collapsed_board[a] == self.collapsed_board[b] == self.collapsed_board[c]:
                if self.collapsed_board[a] == 'X':
                    x_wins += 1
                elif self.collapsed_board[a] == 'O':
                    o_wins += 1

        # Handle Edge Cases: Fractional Scoring
        if x_wins > 0 and o_wins == 0:
            return "Player X Wins!"
        elif o_wins > 0 and x_wins == 0:
            return "Player O Wins!"
        elif x_wins > 0 and o_wins > 0:
            return "Tie! Fractional Score: Player X = 0.5, Player O = 0.5"
        
        # Check for draw
        if ' ' not in self.collapsed_board:
            return "It's a classical draw!"
            
        return None

    def play(self):
        print("=== Welcome to Quantum Tic-Tac-Toe! ===")
        print("Squares are indexed 0-8, from top-left to bottom-right.")
        
        while not self.is_collapsed:
            self.display_board()
            prompt = f"Player {self.current_player}, enter two squares (e.g. '0 1') or type 'collapse': "
            cmd = input(prompt).strip().lower()

            if cmd == 'collapse':
                self.collapse()
                break
            
            try:
                sq1, sq2 = map(int, cmd.split())
                if sq1 == sq2:
                    print("You must choose two distinct squares for a quantum move.")
                    continue
                self.play_quantum_move(sq1, sq2)
            except ValueError:
                print("Invalid input. Please enter two numbers separated by a space, or 'collapse'.")

        self.display_board()
        win_status = self.check_win()
        if win_status:
            print(win_status)
        else:
            print("Game over! The quantum dust has settled, but there is no winner.")

if __name__ == "__main__":
    game = QuantumTicTacToe()
    game.play()