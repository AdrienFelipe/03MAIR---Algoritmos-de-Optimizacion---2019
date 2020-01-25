import numpy as np


def calculate_cost(solution: tuple, max_takes: int, costs: tuple) -> int:
    """
    Calculate the real cost of a single solution.

    :param solution: a flat list of takes, representing a complete or partial solution.
    :param max_takes: the max allowed number of takes per session.
    :param costs: a two dimensions list of all takes with their corresponding needed actors.

    :return: the cost of the solution.
    """
    # Solution total cost.
    solution_cost = 0
    # Takes per session counter.
    takes_count = 0
    session_cost = None
    session_is_full = False

    for take in solution:
        takes_count += 1
        # Whether a session reached its max allowed takes.
        session_is_full = takes_count == max_takes
        # Use a numpy array to ease bitwise operations.
        take_cost = np.array(costs[take])
        # Use bitwise 'or' operation to join the takes' costs per session,
        # as an actor gets paid the same amount regardless of his takes by session.
        session_cost = take_cost if session_cost is None else session_cost | take_cost

        if session_is_full:
            # Total cost is the cost sum of all sessions.
            solution_cost += session_cost.sum()
            # Reset session cost and counters.
            session_cost = None
            takes_count = 0

    # Sum last session if partial, as it would not have been previously added.
    if not session_is_full and session_cost is not None:
        solution_cost += session_cost.sum()

    return solution_cost
