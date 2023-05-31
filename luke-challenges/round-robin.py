# Implement a prototype of a round-robin load-balancing algorithm.

# There are n servers indexed from 1 to n, and m requests to be processed.
# The ith request arrives at time arrival[i] and takes burstTime[i] time to execute.
# The load balancer assigns the request to the available server with the minimum index.
# A server that is assigned the ith request is unavailable from time arrival[i] to arrival[i] + burstTime[i]. At arrival[i] + burstTime[i],
# the server is available to serve a new request.

# Given n, arrival, and burstTime for each request, find the index of the server that executes it.
# If no server is available at the time, the request is dropped, and -1 is reported.
# If multiple requests arrive at the same time, the one with the smaller index is assigned first.

# Example 
# Suppose n = 3, m = 5, arrival = [2, 4, 1,8,9], and
# burstTime = [7, 9, 2, 4, 5]

# Output: [2, 1, 1, 3, 2]


def round_robin(n, arrival, burstTime):
    pass
