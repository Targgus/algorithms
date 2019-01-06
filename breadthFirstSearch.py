"""
Breadth First Running Time:
O(number of edges) + O(number of nodes)
Commonly written as O(number of nodes + number of edges) => O(V+E)
where V is number of vertices and E is number of edges
"""

from collections import deque

# implement the graph with a hash table
graph = {}
# populate hash table with node "you" and the neightbor nodes "alice, bob, claire"
graph["you"] = ['alice', 'bob', 'claire']
# add more nodes and neighbors
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []

# function to check if node is a mango seller
def person_is_seller(name):
    return name[-1] == 'm'
    #return len(name) > 3


def search(name):
    # create new queue
    search_queue = deque()
    # add my neighbors to search queue
    search_queue += graph[name]
    # create empty array of searched nodes
    searched = []

    # while loop that checks if queue is empty
    while search_queue:
        # assign person variable to first person in queue
        person = search_queue.popleft()
        # check if person is a mango seller and not in searched array
        if not person in searched and person_is_seller(person):
            print(person, " is a mango seller!")
            return True
        else:
            # if person is not a mango seller, add person's neighbors to search queue
            search_queue += graph[person]
            # add person to searched array
            searched.append(person)
    # if no one is a mango seller
    return False

# run beadthfirst search
search('you')