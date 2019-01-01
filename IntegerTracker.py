
# Write a class IntegerTracker with these methods:
# track(int) - Receives an integer for tracking.
# get_max() - Returns the max (int) of all integers seen so far.
# get_min() - Returns the min (int) of all integers seen so far.
# get_mean() - Returns the mean (float) of all integers seen so far.
# get_mode() - Returns the mode (most frequent) (int) of all integers seen so far.

#Each method should run run in constant time (O(1) time complexity).

# For example, in python:
# integer_tracker = IntegerTracker()
# integer_tracker.track(1)
# integer_tracker.track(0)
# integer_tracker.get_max() # => 1
# integer_tracker.get_min() # => 0
# integer_tracker.get_mean() # => 0.5
# integer_tracker.get_mode() # => 1 (1 or 0 is acceptable)
# integer_tracker.track(3)
# integer_tracker.track(1)
# integer_tracker.get_max() # => 3
# integer_tracker.get_min() # => 0
#integer_tracker.get_mean() # => 1.25
#integer_tracker.get_mode() # => 1

class IntegerTracker(object):

    #placeholders for everything
    frequent: dict = {}
    numTrackers: int = 0
    total: int
    minInt: int
    maxInt: int
    mode: int
    mean: float
    trackers = []

    def track(self,val):
        # update everything on insert so all returns are O(1)

        # update the count
        IntegerTracker.numTrackers += 1

        # update the total
        if IntegerTracker.numTrackers == 1:
            IntegerTracker.total = val
        else:
            IntegerTracker.total += val

        # update the list
        IntegerTracker.trackers.append(val)

        # update the max
        if IntegerTracker.numTrackers == 1:
            IntegerTracker.maxInt = val
        else:
            if IntegerTracker.maxInt < val:
                IntegerTracker.maxInt = val

        # update the min
        if IntegerTracker.numTrackers == 1:
            IntegerTracker.minInt = val
        else:
            if IntegerTracker.minInt > val:
                IntegerTracker.minInt = val

        # update the most frequent
        if IntegerTracker.numTrackers == 1:
            IntegerTracker.frequent.update({val:1})
            IntegerTracker.mode = val
        else:
            if IntegerTracker.frequent.get(val) is None:
                IntegerTracker.frequent.update({val:1})
            else:
                IntegerTracker.frequent.update({val: IntegerTracker.frequent[val]+1})

            if IntegerTracker.frequent[IntegerTracker.mode] < IntegerTracker.frequent[val]:
                IntegerTracker.mode = val



        # update the mean
        IntegerTracker.mean = IntegerTracker.total / IntegerTracker.numTrackers

    def get_max(self):
        return IntegerTracker.maxInt

    def get_min(self):
        return IntegerTracker.minInt

    def get_mean(self):
        return IntegerTracker.mean

    def get_mode(self):
        return IntegerTracker.mode

integer_tracker = IntegerTracker()
integer_tracker.track(1)
integer_tracker.track(0)
print(integer_tracker.get_max()) #should be 1
print(integer_tracker.get_min()) #should be 0
print(integer_tracker.get_mean()) # #should be 0.5
print(integer_tracker.get_mode()) # => 1 (1 or 0 is acceptable)
integer_tracker.track(3)
integer_tracker.track(1)
print(integer_tracker.get_max()) # => 3
print(integer_tracker.get_min()) # => 0
print(integer_tracker.get_mean()) # => 1.25
print(integer_tracker.get_mode()) # => 1
integer_tracker.track(4)
integer_tracker.track(5)
integer_tracker.track(5)
integer_tracker.track(5)
integer_tracker.track(-5)
print(integer_tracker.get_max()) # => 3
print(integer_tracker.get_min()) # => 0
print(integer_tracker.get_mean()) # => 1.25
print(integer_tracker.get_mode()) # => 1
