#06/16/2024 Attempt #1
# class Solution(object):
#     def equalPairs(self, grid):
#         """
#         :type grid: List[List[int]]
#         :rtype: int
#         """
#         side = len(grid)
#         row_set = set()
#         pairs = 0

#         for row in grid:
#             row_set.add(row)

#         transposed = [list(row) for row in zip(*grid)]

#         for col in transposed:
#             if col in row_set:
#                 pairs += 1

#         return pairs

#         # for i in range(0, side):

#06/16/2024 Attempt #2
class Solution(object):
    def equalPairs(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        pairs = 0

        row_dict = dict()

        for row in grid:
            row_dict[row] = row_dict.get(row, 0) + 1

        transposed = [list(row) for row in zip(*grid)]

        for col in transposed:
            if col in row_dict:
                pairs += row_dict.get(col)

        return pairs