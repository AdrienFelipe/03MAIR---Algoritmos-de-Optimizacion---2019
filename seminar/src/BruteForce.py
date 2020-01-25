from SolutionCost import calculate_cost


def brute_force(costs: tuple, max_takes: int) -> tuple:
    # Generate all solutions from all takes combinations.
    solutions = next_level(costs)

    best_solution = None
    best_solution_cost = None
    # Check all solutions to find the best one.
    for solution in solutions:
        solution_cost = calculate_cost(solution, max_takes, costs)
        if best_solution is None or solution_cost < best_solution_cost:
            best_solution = solution
            best_solution_cost = solution_cost

    return best_solution


def next_level(costs: tuple, solution: tuple = ()) -> list:
    """From a partial solution, generate all remaining combinations"""
    children = []
    for take_id in range(len(costs)):
        # Do not duplicate takes in a solution.
        if take_id in solution:
            continue

        local_solution = solution + (take_id,)
        if len(local_solution) < len(costs):
            # Recursively add levels until solution full length is reached.
            children += next_level(costs, local_solution)
        else:
            children.append(local_solution)

    return children
