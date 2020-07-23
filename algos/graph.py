from collections import deque

from numpy import inf

from ds import Node, LinkedList


def tarjan(adjlist):
    """
    Tarjan algorithm for finding strongly connected components
    """
    seen = set()
    counter = 0

    # init
    for node in adjlist:
        node.label = None
        node.low_link = None

    for node in adjlist:
        # full explore
        if node in seen:
            continue

        # run dfs with bookkeeping
        stack = []
        node.label = counter
        counter += 1
        stack.append(node)

        node.low_link = node.label
        while len(stack):
            curr = stack.pop()
            seen.add(curr)
            children = adjlist.array[curr].tolist()
            for child in children:
                if child in seen:
                    curr.low_link = min(curr.low_link, child.low_link)
                    continue
                child.label = counter
                counter += 1
                child.low_link = child.label
                stack.append(child)

        for n in adjlist:
            print(n.label, n.low_link)
