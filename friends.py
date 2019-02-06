import math

def mean_num_friends(x):
    # TODO
    return sum(num_friends)/len(num_friends)

def median_num_friends(x):
    # TODO
    num_friends.sort();
    if len(num_friends) % 2 == 0:
        return ((num_friends[math.floor(len(num_friends)/2)-1]+num_friends[math.floor(len(num_friends)/2)])/2)
    else:
        return (num_friends[math.floor(len(num_friends)/2)])
    # print(num_friends)



num_friends=[100, 49, 41, 40, 25, 10, 5, 4, 7, 20, 60]

print("mean={}".format(mean_num_friends(num_friends)))

print("median={}".format(median_num_friends(num_friends)))