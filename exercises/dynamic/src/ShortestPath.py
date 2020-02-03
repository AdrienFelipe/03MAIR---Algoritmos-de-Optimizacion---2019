class ShortestPath:
    prices = []
    source_node = 0
    destination_node = 0
    middle_nodes = []
    # Default high value cost. Should use the max price value instead.
    default_cost = 9999

    @staticmethod
    def calculate(prices: list, source_node: int, destination_node: int) -> list:
        solver = ShortestPath()
        solver.prices = prices
        solver.source_node = source_node
        solver.destination_node = destination_node
        solver.middle_nodes = solver.__find_middle_nodes()

        return solver.__build_solution()

    def __find_middle_nodes(self) -> list:
        """
        Core of the dynamic programming:
        Pre-compute optimal last middle node to any destination node from source node.
        """
        # Replace unconnected nodes' price with a high value instead of 'None' for code simplification.
        prices = [
            [destination if destination is not None else self.default_cost for destination in source]
            for source in self.prices
        ]
        nodes_count = len(prices[0])
        # Path's lowest cost from source node to any other following node (key: destination node - value: cost).
        path_cost_to = [self.default_cost] * nodes_count
        # Optimal last middle node to any destination node, from source node
        # (key: destination node - value: middle node).
        middle_nodes = [self.source_node] * nodes_count

        # Explore any other following node from source node.
        for destination_node in range(self.source_node + 1, nodes_count):
            # Direct connection cost between source and destination.
            min_path_cost = prices[self.source_node][destination_node]
            middle_nodes[destination_node] = self.source_node

            # Explore all middle nodes from source node to destination node.
            for middle_node in range(self.source_node + 1, destination_node):
                # Middle node is always one step behind destination node,
                # and therefore path's cost to middle node is always defined.
                current_path_cost = path_cost_to[middle_node] + prices[middle_node][destination_node]
                if current_path_cost < min_path_cost:
                    min_path_cost = current_path_cost
                    middle_nodes[destination_node] = middle_node

            # Save current destination optimal path cost, for further use while searching middle nodes paths cost.
            path_cost_to[destination_node] = min_path_cost

        return middle_nodes

    def __build_solution(self) -> list:
        path = self.__recurse(self.source_node, self.destination_node)
        path.append(self.destination_node)

        return path

    def __recurse(self, source_node: int, destination_node: int) -> list:
        if source_node == destination_node:
            path = []
        else:
            path = self.__recurse(source_node, self.middle_nodes[destination_node])
            path.append(self.middle_nodes[destination_node])

        return path
