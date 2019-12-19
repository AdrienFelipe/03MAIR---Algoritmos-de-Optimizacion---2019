import numpy as np


class ProximityFinder:

    @staticmethod
    def search(points: list, threshold=2 / 3, processed_blocks=()):
        finder = ProximityFinder()

        # Number of dimensions
        dims = len(points[0])
        blocks, blocks_ranges, blocks_hashes = finder.__initialize_blocks(dims, points, threshold)

        # Classify points into their blocks
        for point in points:
            for block_id, block in enumerate(blocks):
                finder.__add_point_to_block(point, block, block_id, blocks_ranges, blocks_hashes)

        proximity_length = None
        proximity_points = None

        for block_id, block in enumerate(blocks):
            # Avoid processing same blocks twice
            if blocks_hashes[block_id] in processed_blocks:
                continue

            processed_blocks += (blocks_hashes[block_id],)
            block_size = len(block)
            # Ignore block with less than 2 points
            if block_size < 2:
                continue

            # This is the target size block
            if block_size == 2:
                # Calculate points distance
                local_length = np.linalg.norm(np.array(block[1]) - np.array(block[0]))
                local_points = block

            # More than 2 points, keep subdividing
            else:
                local_length, local_points = finder.search(block, threshold, processed_blocks)

            # A value was found, check whether it should be used
            if local_length is not None:
                if proximity_length is None or local_length < proximity_length:
                    proximity_length = local_length
                    proximity_points = local_points

        # Case when no block has more than one point
        if proximity_length is None:
            # No other choice than to compare all points altogether
            proximity_length, proximity_points = finder.brute_force(points)

        return proximity_length, proximity_points

    def __add_point_to_block(self, point, block, block_id, blocks_ranges, blocks_hashes):
        hash = '|'
        for dim, value in enumerate(point):
            hash += str(value) + '-'
            block_range = blocks_ranges[block_id][dim]
            if not block_range[0] <= value <= block_range[1]:
                # Skip block for this point as not in range
                return

        # All coordinates are in range
        block.append(point)
        blocks_hashes[block_id] += hash

    @staticmethod
    def brute_force(points):
        proximity_length = None
        proximity_points = None
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                local_length = np.linalg.norm(np.array(points[i]) - np.array(points[j]))
                if proximity_length is None or local_length < proximity_length:
                    proximity_length = local_length
                    proximity_points = [points[i], points[j]]

        return proximity_length, proximity_points

    def __initialize_blocks(self, dims: int, points: list, threshold: float):
        # Max and min of each column
        max = np.max(points, axis=0)
        min = np.min(points, axis=0)
        # Range on witch to group points
        dist = (max - min) * threshold

        # Initialize blocks list
        blocks = []
        # Blocks min and max coordinates list
        blocks_ranges = []
        # Block unique identifiers
        blocks_hashes = []

        # We generate 2 blocks per dimension
        for block_id in range(2 ** dims):
            blocks.append([])
            blocks_ranges.append([])
            blocks_hashes.append('')
            for dim in range(dims):
                # Boolean from position in dimension
                if int(block_id / (2 ** dim)) % 2:
                    blocks_ranges[block_id].append([min[dim], min[dim] + dist[dim]])
                else:
                    blocks_ranges[block_id].append([max[dim] - dist[dim], max[dim]])

        return blocks, blocks_ranges, blocks_hashes
