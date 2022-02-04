# Definition for a undirected graph node
# class UndirectedGraphNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

class Solution(object):

    # def __init__(self):
    #     self.label_map = {}

    # def cloneGraph(self, node):
    #     """
    #     :type node: UndirectedGraphNode
    #     :rtype: UndirectedGraphNode
    #     """
    #     # DFS
    #     if node is None:
    #         return None
    #     res = UndirectedGraphNode(node.label)
    #     self.label_map[node.label] = res
    #     for ne in node.neighbors:
    #         if ne.label not in self.label_map:
    #             res.neighbors.append(self.cloneGraph(ne))
    #         else:
    #             res.neighbors.append(self.label_map[ne.label])
    #     return res

    def cloneGraph(self, node):
        # BFS
        if node is None:
            return None
        label_map = {}
        queue = [node]
        graphCopy = UndirectedGraphNode(node.label)
        label_map[node.label] = graphCopy
        while len(queue) > 0:
            curr = queue.pop(0)
            for ne in curr.neighbors:
                if ne.label in label_map:
                    label_map[curr.label].neighbors.append(label_map[ne.label])
                else:
                    neighborCopy = UndirectedGraphNode(ne.label)
                    label_map[curr.label].neighbors.append(neighborCopy)
                    label_map[ne.label] = neighborCopy
                    queue.append(ne)
        return graphCopy

