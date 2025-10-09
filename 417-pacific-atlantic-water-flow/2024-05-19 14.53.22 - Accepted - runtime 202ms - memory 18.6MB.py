
from collections import deque


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        visitedNodes1 = set()
        visitedNodes2 = set()
        memo1 = {}
        memo2 = {}

        def validateFlow(row, column, h, v):
            if (row, column) in v:
                return False
            if (
                row < 0
                or column < 0
                or row > len(heights) - 1
                or column > len(heights[0]) - 1
            ):
                return False
            if heights[row][column] < h:
                return False
            return True

        def ConnectedToPacific(row, column):
            # print("Pacific Ocean : ",row,column)
            key = (row, column)
            h = heights[row][column]
            if key in visitedNodes1:
                return
            visitedNodes1.add(key)

            ##Up
            if validateFlow(row - 1, column, h, visitedNodes1):
                ConnectedToPacific(row - 1, column)

            ##Down
            if validateFlow(row + 1, column, h, visitedNodes1):
                ConnectedToPacific(row + 1, column)

            ##Left
            if validateFlow(row, column - 1, h, visitedNodes1):
                ConnectedToPacific(row, column - 1)

            ##Right
            if validateFlow(row, column + 1, h, visitedNodes1):
                ConnectedToPacific(row, column + 1)

        def ConnectedToAtlantic(row, column):
            key = (row, column)
            h = heights[row][column]
            if key in visitedNodes2:
                return
            visitedNodes2.add(key)

            ##Up
            if validateFlow(row - 1, column, h, visitedNodes2):
                ConnectedToAtlantic(row - 1, column)

            ##Down
            if validateFlow(row + 1, column, h, visitedNodes2):
                ConnectedToAtlantic(row + 1, column)

            ##Left
            if validateFlow(row, column - 1, h, visitedNodes2):
                ConnectedToAtlantic(row, column - 1)

            ##Right
            if validateFlow(row, column + 1, h, visitedNodes2):
                ConnectedToAtlantic(row, column + 1)

        ##Pacific Ocean loop

        for r in range(len(heights)):
            ConnectedToPacific(r, 0)
        for c in range(len(heights[0])):
            ConnectedToPacific(0, c)

        ##Atlantic Ocean
        for r in range(len(heights)):
            ConnectedToAtlantic(r, len(heights[0]) - 1)
        for c in range(len(heights[0])):
            ConnectedToAtlantic(len(heights) - 1, c)

        return list(visitedNodes1.intersection(visitedNodes2))
