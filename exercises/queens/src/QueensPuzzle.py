import numpy as np


class QueensPuzzle:
    """Solve the Eight queens puzzle using a backtracking algorithm"""

    @staticmethod
    def solve(board_size: int) -> list:
        puzzle = QueensPuzzle(board_size)
        puzzle.__execute()

        return puzzle.solutions

    def __init__(self, board_size: int):
        self.board_size = board_size
        self.solutions = []

    def __execute(self, solution: tuple = ()) -> None:
        """Main recursive function to explore each solution tree"""
        column = len(solution)
        # Test all rows for current column.
        for row in range(self.board_size):
            local_solution = solution + (row,)

            if self.__constrains_are_valid(local_solution):
                if column < self.board_size - 1:
                    self.__execute(local_solution)
                else:
                    self.solutions += (local_solution,)

    @staticmethod
    def __constrains_are_valid(solution: tuple) -> bool:
        # Columns are not tested as they can't be duplicated by design.
        return QueensPuzzle.__rows_are_unique(solution) and QueensPuzzle.__diagonals_are_unique(solution)

    @staticmethod
    def __rows_are_unique(solution: tuple) -> bool:
        # A 'set' will return only unique values.
        return len(set(solution)) == len(solution)

    @staticmethod
    def __diagonals_are_unique(solution: tuple) -> bool:
        """
        Check whether diagonals have a unique value.
        To do so, rotate the solution board 45º so that diagonals become verticals and horizontals, and therefore having
        only one point per diagonal means having only unique x and y coordinates.
        """
        # Pre-calculate cosine and sine rotation values.
        angle = np.math.pi / 4  # 45º
        cos = np.math.cos(angle)
        sin = np.math.sin(angle)
        # Rotate each point 45º.
        # As x and y coordinate step is 0.7, we can use a 0.1 precision (hence int(10 * ))
        rotated_solution = [
            [int(10 * (x * cos - y * sin)), int(10 * (x * sin + y * cos))]
            for x, y in enumerate(solution)
        ]
        # Check for x and y unique values.
        x_is_unique = len(set(np.array(rotated_solution)[:, 0])) == len(rotated_solution)
        y_is_unique = len(set(np.array(rotated_solution)[:, 1])) == len(rotated_solution)

        return x_is_unique and y_is_unique
