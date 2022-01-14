class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        # Because from and to is between 0 and 1000. Idea is to store counts in an array of size 1001.
        roadOfTrips = [0 for i in range(1001)]
        
        # Update passenger change for each trip
        for numPassengers, start, end in trips:
            roadOfTrips[start] += numPassengers # Increment when passenger is on board
            roadOfTrips[end]   -= numPassengers # decrement when they depart
        
        carLoad = 0
        # Count total passenger for each bus top
        # we have the count array, we perform a line sweep from 0 to 1000 and track its total
        for passengers in roadOfTrips:
            carLoad += passengers
            if carLoad > capacity: # Reject when the car is overloaded somewhere
                return False
        
        return True  # Accept only if all trip is safe