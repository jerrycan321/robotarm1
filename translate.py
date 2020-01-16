



def translate(start,end):
    max_steps = 0
    for servo in range(0,6):
        steps=abs(start[servo] - end[servo])
        # Determine size of location matrix array
        # and note which servo has the most steps to make
        if steps > max_steps:
            max_steps = steps
            hi_servo = servo

    # Create the locmat array with steps for servo that
    # moves the most
    locmat =[]
    start_hi = start[hi_servo]
    for step in range(0,max_steps):
      locmat.append([0,0,0,0,0,0])

      if start[hi_servo] < end[hi_servo]:
         start_hi = start_hi + 1
      else:
         start_hi = start_hi - 1

      locmat[step][hi_servo] = start_hi

      # Populate the matrix with the other servos positoins
      # required so that all servos arrive at final location 
      # when the servo with the most steps does.
    for servo in range(0,6):
       if servo != hi_servo:
          for step in range(0,max_steps):
             if start[servo] > end[servo]:

                 locmat[step][servo] = start[servo] - abs(start[servo] - end[servo]) * step / max_steps 
             else:
                locmat[step][servo] =  start[servo] + abs(start[servo] - end[servo]) * step / max_steps
             locmat[step][servo] = round(locmat[step][servo])


    
    return locmat
        

if __name__ == '__main__':

   location = [[1,2,3,4,95,6],
               [10,1,50,90,5,25],
               [10,11,12,13,14,15]]


   print(location[0])
   print(location[1])

   for servos_move in translate(location[0],location[1]):
      print(servos_move)

