import numpy as np

from SolutionCost import calculate_cost


def estimate_lowest_cost(solution: tuple, max_takes: int, costs: tuple) -> int:
    """Calculate an estimation of the lowest cost from the remaining takes"""
    estimated_cost = None
    for take_id, take in enumerate(costs):
        if take_id not in solution:
            take_cost = np.array(take)
            estimated_cost = take_cost if estimated_cost is None else take_cost + estimated_cost

    # Estimate best case scenario cost, by summing the minimal needed sessions per actor in the remaining takes.
    return np.ceil(estimated_cost / max_takes).sum() if estimated_cost is not None else 0


def create_child_solutions(solution: tuple, costs: tuple, max_takes: int, explored_nodes=None) -> list:
    """From a node solution, create its child solutions"""
    # Auto-initialization for tests simplicity.
    if explored_nodes is None:
        explored_nodes = []

    # Calculate takes number in the current session.
    session_takes_count = max_takes - (len(solution) + 1) % max_takes

    child_solutions = []
    for take_id in range(len(costs)):
        # Ignore already used takes.
        if take_id not in solution:
            local_solution = solution + (take_id,)
            # Sort takes in the current session to have unique solutions, regardless of its takes order.
            session_takes = tuple(sorted(local_solution[-session_takes_count:]))
            local_solution = local_solution[:-session_takes_count] + session_takes
            # Only add a child if it was not previously added.
            if local_solution not in explored_nodes:
                child_solutions.append(local_solution)
                # Keep track of generated solutions.
                explored_nodes.append(local_solution)

    return child_solutions


def branch_and_pound(costs: tuple, max_takes: int, nodes_limit: int = 500) -> tuple:
    """
    Iteratively branch and pound the node tree based on 3 types of pounding:
    - Node child pounding
    - Full session nodes pounding
    - Nodes limit pounding
    """
    best_solution = None
    best_solution_cost = None
    explored_nodes = []
    iteration = 0

    # Initialize the tree with an empty root node.
    nodes = [{
        's': (),
        'cost': 0,
        'depth': 0,
        'estimation': estimate_lowest_cost((), max_takes, costs),
    }]

    # Loop as long as there are nodes to loop over.
    while nodes:
        iteration += 1

        # Active nodes max and min depths.
        min_depth = min(nodes, key=lambda node: node['depth'])['depth']
        max_depth = max(nodes, key=lambda node: node['depth'])['depth']

        # Whether all nodes are at the same depth.
        if max_depth != 0 and min_depth == max_depth:
            # Whether it is a 'full session' depth.
            if min_depth % max_takes == 0:
                # As all nodes have full sessions, pound the ones with higher estimated cost.
                best_node = min(nodes, key=lambda node: node['cost'] + node['estimation'])
                best_cost = best_node['cost'] + best_node['estimation']
                nodes = [node for node in nodes if node['cost'] + node['estimation'] <= best_cost]

            # Hard pound if nodes list becomes too big. This might result in removing the best solution.
            elif len(nodes) > nodes_limit:
                # Sort nodes by current estimated cost.
                nodes = sorted(nodes, key=lambda node: node['cost'] + node['estimation'])
                nodes = nodes[:nodes_limit]

        # Extract first node of the list.
        # Node is expected to have the lowest depth as children are appended at the bottom of the list.
        selected_node = nodes.pop(0)

        # Branch selected node.
        child_nodes = [
            {
                's': solution,
                'depth': len(solution),
                'cost': calculate_cost(solution, max_takes, costs),
                'estimation': estimate_lowest_cost(solution, max_takes, costs),
            }
            for solution in create_child_solutions(selected_node['s'], costs, max_takes, explored_nodes)
        ]

        # Pound new branches with a higher estimated utopian cost.
        if child_nodes:
            best_cost = min(child_nodes, key=lambda node: node['estimation'])['estimation']
            child_nodes = [node for node in child_nodes if node['estimation'] == best_cost]
            nodes.extend(child_nodes)

        # Whether node is final and cannot have children.
        is_final_node = len(selected_node['s']) == len(costs)
        # Select node as best solution if its cost has improved.
        if is_final_node and (best_solution_cost is None or selected_node['cost'] < best_solution_cost):
            best_solution_cost = selected_node['cost']
            best_solution = selected_node['s']

    return best_solution
