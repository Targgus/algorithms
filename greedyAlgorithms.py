'''
Greedy algorithms, if run to calcualte exact solutions, can take O(2^N)
Approximate solutions can be used to reduce run time ot O(n^2)
'''
# set-covering problem

# create list of states needed to cover
states_needed = set(['mt', 'wa', 'or', 'id', 'nv', 'ut', 'ca', 'az'])

# creaty empty hash table
stations = {}

# create sets of stations and the states they cover
stations['kone'] = set(['id', 'nv', 'ut'])
stations['ktwo'] = set(['wa', 'id', 'mt'])
stations['kthree'] = set(['or', 'nv', 'ca'])
stations['kfour'] = set(['nv', 'ut'])
stations['kfive'] = set(['ca', 'az'])

# place holder for final stations
final_stations = set()

# loop until states needed is empty
while states_needed:
    # best_station is the station that covers the most uncovered states
    best_station = None
    # set of all states covered this station covers that haven't been covered yet
    states_covered = set()
    # loop over every station to find best station
    for station, states in stations.items():
        # set logic to find common states between two sets
        covered = states_needed & states
        # check to see if station covers mote states than current best station
        if len(covered) > len(states_covered):
            best_station = station
            states_covered = covered
            # print(best_station)

    # update states_needed
    states_needed -= states_covered

    # add best station to final_station list
    final_stations.add(best_station)



# print solution
print(final_stations)