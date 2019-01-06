

# implement hash table
graph = {}
# store neighbors (a & b) and cost (6 & 2) for starting node by using another hash table
graph['start'] = {}
graph['start']['a'] = 6
graph['start']['b'] = 2

# start another hash table for the a node's neighbors and weights
graph['a'] = {}
graph['a']['fin'] = 1

# node b neighbors and weights
graph['b'] = {}
graph['b']['a'] = 3
graph['b']['fin'] = 5

# final hash table for finish node is empty
graph['fin'] = {}


# create hash table to store the costs for each node
# cost of node = how long it takes to get from that node to the start
# assume node to finish is infinity
infinity = float('inf')
costs = {}
costs['a'] = 6
costs['b'] = 2
costs['fin'] = infinity

# create hash table for node parents
parents = {}
parents['a'] = 'start'
parents['b'] = 'start'
parents['fin'] = None

# keep track of nodes already processed
processed = []

# function to find lowest cost node
def find_lowest_cost_node(costs):
    lowest_cost = float('inf')
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node

def findFinCost(costs):
    # call function to find lowest cost node not processed yet
    node = find_lowest_cost_node(costs)
    while node is not None:
        cost = costs[node]
        neighbors = graph[node]
        # for loop to go through all the neighbors of node
        for n in neighbors.keys():
            new_cost = cost + neighbors[n]
            # compare new cost to current node cost
            if costs[n] > new_cost:
                # update current node cost to lower new_cost
                costs[n] = new_cost
                # update node parents
                parents[n] = node
        # move to next node by marking current node as processed
        processed.append(node)
        node = find_lowest_cost_node(costs)
    return costs['fin']

# print out final cost to get from start to fin
print(findFinCost(costs))