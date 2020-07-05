'''
Given hour and minute, write a function to calculate an angle between hour/minute hand.

SOLUTION:

Hour hand moves at the rate of 0.5 degree per minutes.
Minute hand moves at the rate of 6 degrees per minutes.

Angle of minute hand, posm = 6*M
Angle of hour hand, posh = 0.5 * (60*H + M)

Answer = abs(posh - posm)

Follow-up question:
At what times do the hour and minute hand collide??

Make an equation posh = posm.
You will get an equation.
'''
