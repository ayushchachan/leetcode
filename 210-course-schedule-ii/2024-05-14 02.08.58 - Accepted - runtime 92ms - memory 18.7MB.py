#
# @lc app=leetcode id=210 lang=python3
#
# [210] Course Schedule II
#


# @lc code=start
#
# @lc app=leetcode id=207 lang=python3
#
# [207] Course Schedule
#

# @lc code=start


def makeGraph(prereq, n):
    G = {}
    for i in range(n):
        G[i] = []
    for ele in prereq:
        fro, to = ele
        G[fro].append(to)
    return G


def Finish(numCourses: int, prerequisites: List[List[int]]) -> bool:
    G = makeGraph(prerequisites, numCourses)
    res = []
    currStack = set()
    visitedNodes = set()

    def dfs(root, currStack, visitedNode):
        nonlocal res
        currStack.add(root)
        for neigh in G[root]:
            if neigh in currStack:
                res = -1
                return
            if neigh not in visitedNode:
                visitedNode.add(neigh)
                dfs(neigh, currStack, visitedNode)
        currStack.remove(root)
        if res != -1:
            res.append(root)

    for i in range(numCourses):
        if i not in visitedNodes:
            visitedNodes.add(i)
            dfs(i, currStack, visitedNodes)
    if(res == -1):
        return []
    return res



class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
       return Finish(numCourses,prerequisites)



# @lc code=end
