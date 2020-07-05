- The barber has one barber's chair in a cutting room and a waiting room containing a number of chairs in it.
- When the barber finishes cutting a customer's hair, he dismisses the customer and goes to the waiting room to see if there are others waiting.
- If there are, he brings one of them back to the chair and cuts their hair.
- If there are none, he returns to the chair and sleeps in it.
- Each customer, when they arrive, looks to see what the barber is doing.
- If the barber is sleeping, the customer wakes him up and sits in the cutting room chair.
- If the barber is cutting hair, the customer stays in the waiting room.
- If there is a free chair in the waiting room, the customer sits in it and waits their turn.
- If there is no free chair, the customer leaves.

- Based on a naïve analysis, the above decisions should ensure that the shop functions correctly, with the barber cutting the hair of anyone who arrives until there are no more customers, and then sleeping until the next customer arrives.
- In practice, there are a number of problems that can occur that are illustrative of general scheduling problems.
- The problems are all related to the fact that the actions by both the barber and the customer (checking the waiting room, entering the shop, taking a waiting room chair, etc.) all take an unknown amount of time.
  - For example, a customer may arrive and observe that the barber is cutting hair, so he goes to the waiting room.  
    While they're on their way, the barber finishes their current haircut and goes to check the waiting room.  
    Since there is no one there (the customer not having arrived yet), he goes back to their chair and sleeps.  
    The barber is now waiting for a customer, but the customer is waiting for the barber.
  - In another example, two customers may arrive at the same time when there happens to be a single seat in the waiting room.  
    They observe that the barber is cutting hair, go to the waiting room, and both attempt to occupy the single chair. 

- Many possible solutions are available.
- The key element of each is a mutex, which ensures that only one of the participants can change state at once.
- The barber must acquire/enforce this mutual exclusion (of room status) before checking for customers and release it when they begin either to sleep or cut hair.
- A customer must acquire it before entering the shop and release it once they are sitting in either a waiting room chair or the barber chair, and also when they leave the shop because no seats were available.

```python
Mutex barberReady = 0
Mutex waitingRoom = 1           # if 1, the number of seats in the waiting room can be incremented or decremented
Semaphore custReady = 0         # the number of customers currently in the waiting room, ready to be served
int numberOfFreeWRSeats = N     # total number of seats in the waiting room

def Barber():
  while true:                   # Run in an infinite loop.
    wait(custReady)             # Try to acquire a customer - if none is available, go to sleep.
    wait(waitingRoom)         # Awake - try to get access to modify # of available seats, otherwise sleep.
    numberOfFreeWRSeats += 1    # One waiting room chair becomes free.
    signal(barberReady)         # I am ready to cut.
    signal(waitingRoom)       # Don't need the lock on the chairs anymore.
    # (Cut hair here.)

def Customer():
  while true:                   # Run in an infinite loop to simulate multiple customers.
    wait(waitingRoom)         # Try to get access to the waiting room chairs.
    if numberOfFreeWRSeats > 0: # If there are any free seats:
      numberOfFreeWRSeats -= 1  #   sit down in a chair
      signal(custReady)         #   notify the barber, who's waiting until there is a customer
      signal(waitingRoom)     #   don't need to lock the chairs anymore
      wait(barberReady)         #   wait until the barber is ready
      # (Have hair cut here.)
    else:                       # otherwise, there are no free seats; tough luck --
      signal(waitingRoom)     #   but don't forget to release the lock on the seats!
      # (Leave without a haircut.)
```