# -*- coding: utf-8 -*-
"""
Created on Sun Jul 31 19:34:17 2022

@author: Tyrone_Mapp_1623576
"""

# The code in below does not fully work, I've run out of time to finish troubleshooting it. It's been a lot to take
# in learning Python as well as try and take in metahueristic concepts that are completely foreign to me.

# The commentary below goes through my initial thinking that I worked out over the last couple of weeks, 
# The code below the comments is the evolution of my thought process and where i got to
# Amoung lots of reading I also purchased a UDEMY course to attempt to help, it did help with the conceptual but
# putting that conceptual work into code feels very difficult - especially turning a forumula into code
# There will be a better way to do it than I have attempted below im sure.

# There is a bug in the logic that is making the variables loop through in an odd manner,
# But essentially what the bug is is that each Y co-ordinate when being set, if the Y co-ordinate
# being set is lower than the height of the previous it will add the co-ordinate y and the height y of the previous
# together, but it wont do it if the corresponding y co-ordinate is lower. Its something to do with the if statement
# but im out of time to take a look.

# I've also run out of time to do any report or video. There was just too much to do learning Python, trying to 
# understand metahueristics, try and translate that into code and put it all together, debug and get it working.


"""



    We want the lowest Height
    
    i is an element of I and a Width (W)
    i is the number of the rectangle or reference of the rectangle in the array
    I is the variable containing all the rectangles which is why i is a member of I
    wi is the width of a specific rectangle - member of I
    hi is the height of a specific rectangle - member of I    
    W is the width of the sheet. it is our constraint and = 100
    xi is the location of the bottom left corner of the rectangle on the X plane
    yi is the location of the bottom left corner of the rectangle on the Y plane
    we use xi and yi as locating anchors because we can then get the co-ordinates of all other parts from dimensions of the xy
    H is the maximum height constraint - we could use this to specify no solution higher than an arbitrary decision based off a prespecified solution
    
    
    
    subject to:
        
    1...   xi + wi <= W   --> This is a constraint, location of x co-ord plus width of rectangle must be less than total width
    2...   yi + hi <= H   --> This is a constraint, location of y co-ord plus height of rectangle must be less than height constraint
    3...      
    For each i in I that is not current-i as j
    if xj + wj > xi AND xi > xj = overlap on x co-ordinates but not neccessarily y coordinates
    AND 
    if yj + hj > yi AND yi > yj = overlap on y co-ordinates but not neccessarily x coordinates
    THEN 
    The solution is infeasible and we must try something else --> This is a constraint, It prevents rectangles from overlapping
            
            This is a fail if:
                the x position of i plus width of i is less than or equal to the x position any rectangle in the set. 
                the x position of any rectangle plus width of next rectangle is less than or equal to position of xi (we want to work from left to right)
                the y position of i plus height of i is less than or equal to y position of any rectangle (j)
                the y position of next rectangle plus the height of next rectangle is less than or equal to height of i
            
    4...   xi,yi >=0  --> This constraint means that the starting position of xi and yi must be greater than or equal to zero - we don't want them to be less than the bottom left of our sheet position.
    5.. Finally the string must have been set to a YES so that we know it was already set and dealt with.  
      
   //******************************************************************************


    The big E looking symbol called Sigma indicates summation, sum of the terms that follow a pattern
    
    EieI ^wi hi = WH --> This means all the elements of i in I and the summation of all their areas are equal to the desired Width, height area.
    
    We could use this equation to to validate that if we found a solution where the area of all rectangles equals the area
    that is in the chart, then we have found the perfect solution and can stop the equation. Or we could use it to say we
    have found a near perfect solution so could add that to a tabu list - i.e it may not be possible to perfectly pack
    but we know this is close to perfect so is worth keeping as a potential solution.
     
    
    Our array of values should be:
        
        IDi , wi , yi , xi , yi
        
        ID of Rectangle,  Width of rectangle, Height of Rectangle, X-coordiante (initialised 0), Y-Coordinate (initialised 0).
        
        Then we should have a base solution set as the initial solution. This one is manually generated due to low number
        
        
        ID  wi, hi,  xi,  yi is-set
        1,	13,	6,   0,   0   no/yes
        2,	10,	7,   13,  0   no/yes
        3,	5,	9,   23,  0   no/yes
        4,	11,	7,   28,  0   no/yes
        5,	12,	11,  39,  0   no/yes
        6,	1,	11,  51,  0   no/yes
        7,	7,	5,   52,  0   no/yes
        8,	16,	6,   59,  0   no/yes
        9,	11,	8,   75,  0   no/yes
        10,	10,	1,   86,  0   no/yes
        11,	2,	14,  96,  0   no/yes
        12,	10,	13,  0,   6   no/yes
        13,	1,	19,  10,  6   no/yes
        14,	6,	18,  11,  9   no/yes
        15,	17,	9,   17,  9   no/yes
        16,	12,	2,   34,  11  no/yes
        17,	7,	9,   46,  11  no/yes
        18,	6,	18,  53,  11  no/yes
        19,	10,	4,   59,  6   no/yes
        20,	8,	5,   69,  8   no/yes
        
        
        Build a baseline solution with code.
        
        //Set all the variables
        
        x-position = 0
        y-position = 0
        first-loop = yes
        Current-max-height = 0
        row = 0
        count = 0
        count-monitor = 0
        right-align = 0
        
        //Loop through entire array
        
        While i <= I
            
            SET xi = right-align
            
            right-align = xi + x-position + wi
            
                    
            IF right-align > 100 
                THEN x-position = 0
                AND SET xi = 0
                AND y-position = current-max-height 
                AND right-align = 0 + wi 
                AND count = count + 1
                AND count-monitor = count 
            ELSE
                Do Nothing
                
            //If you move up to the next row, set the bottom left y position on yi of the current max height.
            SET yi = y-position
            
            top-align = y-position + hi
            
            if top-align > current-max-height then current-max-height = top-align
            
            
        EXIT
        
      # Get Max height for solution - if the solution comes up with a height more than this we already have a better solution.
      
      H = current-max-height  
            
      #Get Total area of rectangles
      
      area = 0
      
      while i <= I
          area = area + (wi * hi)
          
          EXIT
      
      #The area of the proposed solution can then be compared to the total area of rectangles
      # a 1-1 match indicates perfect solution and the program should exit.
      
      
      # Now we need to build the metahueristic part of the solution
      
      
      The item to be minimised (f) is the area.
      
      Set number-of-runs = #value
      count = 0
      is-initial = yes
      current-array = I
      Solution-Found = NO
      Optimum-Area = NUMBER
      
      while count <= number-of-runs & Solution-Found = NO
      
      if is-initial = yes 
         
          Create new array-of-values with same layout as original array
          
          ELSE
          
              I = numpy.roll(I, 1) # Rotate Array by 1.
              
              if I array is the same as initial-array OR I array is same as current-array  #Move out of its neighbourhood
                  THEN I = np.random.shuffle(I)
                  AND current-array = I
                  
     
      
      
      For each i in I
      
          put i xi on 0
          
          pass = no
          
          while pass = no
               
              run overlap check
              
              if pass. set pass = yes AND set is-set = YES AND goto next i
              if fail. xi = xi + 1      
              if xi + wi > 100 then xi = 0 AND yi = yi+1
        EXIT
        
              
        
      END
      
      SET is-initial = NO
      count = count + 1
      Calculate Area in newly filled rectangle (S)
            
      Is-better = NO
      
      While Is-better = NO
          for each s in TABU 
      
            if S < s
                THEN append S as s to TABU
                AND Add to Solutions-Array the I with the AREA as an Index
                AND SET Is-better to YES
                
                END
      
            ENDFOREACH
        
        Is-better = NOTYET
                
        if S = Optimum-Area Then Solution-Found = YES
        
        
      END
      
      
      

"""

# Pre populated solution plus all dimensions of rectangles and their unique identifier
import numpy as np
#import matplotlib.pyplot as plt 
#import pandas as pd
#import itertools as itr

I = np.array([ 
    [1,	 13,	6,   0,   0,   1],
    [2,	 10,	7,   13,  0,   1],
    [3,	 5,	    9,   23,  0,   1],
    [4,	 11,	7,   28,  0,   1],
    [5,	 12,	11,  39,  0,   1],
    [6,	 1,	    11,  51,  0,   1],
    [7,	 7,	    5,   52,  0,   1],
    [8,	 16,	6,   59,  0,   1],
    [9,	 11,	8,   75,  0,   1],
    [10, 10,	1,   86,  0,   1],
    [11, 2,	    14,  96,  0,   1],
    [12, 10,	13,  0,   6,   1],
    [13, 1,	    19,  10,  6,   1],
    [14, 6,	    18,  11,  9,   1],
    [15, 17,	9,   17,  9,   1],
    [16, 12,	2,   34,  11,  1],
    [17, 7,	    9,   46,  11,  1],
    [18, 6,	    18,  53,  11,  1],
    [19, 10,	4,   59,  6,   1],
    [20, 8,	    5,   69,  8,   1]
    ])

solutionCount = 0 # how many solutions added to TABU, also works as an indexing number for cross solution outputs

tabuList = np.array([[0,0]]) #Initialise Tabu Array - this will dynamically extend, we are not running millions of possible solutions

arraysOfSolutions = np.array([[[0]],[[0]]])
            
            
            


# if I want to output part of an array starting at 0 --> print (I[0]) or print(I[0,0]) for just one element of an array 0

#Get the Maximum height of first solution
MaxHeight = 0
H = 0
BaseArea = 0

for index in range(len(I)): 
    
    x = I[index,2] #height of rectangle
    y = I[index,4] #height of bottom of rectangle
    H = x+y # what is the height of this rectangle 
    
    BaseArea = BaseArea + (I[index,1]*I[index,2])
    ###print(H)
    if H > MaxHeight: #always checking to see if our rectangle is actually the highest
        MaxHeight = H

MaxArea = MaxHeight * 100

#Get optimum solution
ox = 0
oy = 0

for o in range(len(I)):
    ox = 100
    oy = oy + I[o,2] / 20

optimumArea = ox * oy

#Now I know the baseline Maximum area and the baseline Area of all rectangles so I can compare how close I am getting towards a perfect or feasible solution


 # The item to be minimised (f) is the area.
 
numberOfRuns = 5
count = 0
isInitial = "yes"
currentArray = I
solutionFound = "NO"
newArray = np.array
W=100
cA = np.array       
        
while (count < numberOfRuns) and (solutionFound == "NO"):
   
        if isInitial == "no": 
      
           newArray = I
       
            
           I = np.roll(I, 1) # Rotate Array by 1 to get a neighbourhood solution.
           
           if (I[0] == newArray[0]) or (I[0] == currentArray[0]):  #Move out of its neighbourhood by randomising the order
               I = np.random.shuffle(I)
               currentArray = I
        
        #Reset values to Zero because our new array sequence needs to drop the first rectangle in the array at x,y 0
        #We are using bottom left first as the placement option
        countReorder = 1
        for xx in range(len(I)):
            I[xx,3] = 0
            I[xx,4] = 0
            I[xx,5] = 0
            I[xx,0] = countReorder
            countReorder = countReorder + 1 # this is to make the logi re-work below
        
        
        cA = I      #Check Array Counter --> previously used I[j,x] 
        
        for i in range(len(I)): 
            
            
            isInitial == "no"   
            overlapPass = "NO"
            
            while overlapPass == "NO":
                 
                #Run overlap check
                """ 
                i is an element of I and a Width (W)
                i is the number of the rectangle or reference of the rectangle in the array
                I is the variable containing all the rectangles which is why i is a member of I
                wi is the width of a specific rectangle - member of I
                hi is the height of a specific rectangle - member of I    
                W is the width of the sheet. it is our constraint and = 100
                xi is the location of the bottom left corner of the rectangle on the X plane
                yi is the location of the bottom left corner of the rectangle on the Y plane
                we use xi and yi as locating anchors because we can then get the co-ordinates of all other parts from dimensions of the xy
                H is the maximum height constraint - we could use this to specify no solution higher than an arbitrary decision based off a prespecified solution
                
                """
              
               
                xi = I[i,3]
                yi = I[i,4]
                wi = I[i,1]
                hi = I[i,2]
                isSet = I[i,5]
                H = MaxHeight
                A = MaxArea
    
                widthPass = "NO"
                heightPass = "NO"
                widthZeroPass = "NO"
                heightZeroPass = "NO"
                xPositionPass = "NO"
                yPositionPass = "NO"
                overlapBurden = "NA"  #This must be set to NO to break out of overlap moves that move us out of overlap 
                unitPass = "NO"
                nextYPass = "YES"
                nextXPass = "YES"
                firstCompleted = "NO"
                
                # xi + wi <= W  # --> This is a constraint, location of x co-ord plus width of rectangle must be less than total width
                # yi + hi <= H  # --> This is a constraint, location of y co-ord plus height of rectangle must be less than height constraint
              
                while overlapBurden != "NO":
                  
                             
                  for j in range(len(cA)):
                   
                      ###print("In the Range Statement line 395")
                      ###print("This lines ID (i) is: ", I[i,0])
                      ###print("The next lines (j) ID is: ", I[j,0])
                      
                      jxi = cA[j,3]
                      jyi = cA[j,4]
                      jwi = cA[j,1]
                      jhi = cA[j,2]
                      jisSet = cA[j,5]
                      
                      print ("We are in index cA ", cA[j,0], " and index I ", I[i,0])
                      
                      if cA[j,0] != I[i,0]: 
                          print("Moved into if statement line 409") 
                          print("Moved into if statement line 409")
                          print("Moved into if statement line 409")
                          unitPass = "NO"
                          
                          while unitPass == "NO":
                              ###print("Count status is: ", count)
                              ###print("OverlapBurden set to: ", overlapBurden)
                              ###print("Moved into Unit Pass While Statement line 405 and our i ID is ", I[i,0], " and our next test j is ", I[j,0])
                              
                              
                              ###print("jxi and jwi = " , jxi+jwi)
                              ###print("xi = ",xi, " and jxi = ", jxi, " and we are on j index ", I[j,0])
                              ###print("wi = ",wi)
                              ###print("yi = ",yi)
                              #print("is j Zero ", I[j,5], " For Row ", I[j,0])
                              #print("jyi and jhi = " , jyi+jhi)
                              
                              #print("jxi and jwi = " , jxi+jwi)
                              #Test for overlap on X Co-ordinates
                              if widthPass == "NO":
                                  if jxi == 0 and jyi == 0 and cA[j,0] != 1: # had to do the count reorder in resequencing the array above to make this work each time.
                                      widthPass = "YES"
                                      print("@@@ first X after first run test PASSED", I[i,0], " at co-ord", jxi )
                                  elif (jxi + jwi) > xi and xi > jxi:
                                      widthPass = "NO"
                                      print("first X test failed", I[i,0], " at co-ord", jxi )
                                  elif (jxi + jwi) > xi and (xi + wi) <= jxi:
                                      widthPass = "YES"
                                      print("@@@ second X test passed", I[i,0], " at co-ord", jxi )
                                  elif xi >= (jxi + jwi):
                                      print("@@@ third X test passed", I[i,0], " at co-ord", jxi )
                                      widthPass = "YES"
                                  elif jxi == 0 and (I[i,0] == 1 or I[i,0] == 0) and firstCompleted != "YES":
                                      print("@@@ fourth X test passed", I[i,0], " at co-ord", jxi )
                                      widthPass = "YES"
                                  else:
                                      widthPass = "NO"
                                  ###print("final widthpass fails here")
                              
                            
                              ###print("Moved past the X test")
                                  
                              #Test for overlap on Y Co-ordinates
                              nextYPass = "YES" # Getting the loop out of auto counting up due to line 491
                              if heightPass == "NO":
                                  if jxi == 0 and jyi == 0 and cA[j,0] != 1: # had to do the count reorder in resequencing the array above to make this work each time.
                                      heightPass = "YES"
                                      print("@@@ first Y after first run test PASSED", I[i,0])
                                  elif (jyi + jhi) > yi and yi > jyi:
                                      heightPass = "NO"
                                      print("first Y test failed", I[i,0])
                                  elif (jyi + jhi) > yi and yi + hi <= jyi:
                                      heightPass = "YES"
                                      print("@@@ second Y test passed", I[i,0])
                                  elif yi >= (jyi + jhi):
                                      heightPass = "YES"
                                      print("@@@ third Y test passed", I[i,0])
                                  elif jyi == 0 and (I[i,0] == 1 or I[i,0] == 0) and firstCompleted != "YES":
                                      print("@@@ height test passed", I[i,0])
                                      heightPass = "YES"
                                  else:
                                      heightPass = "NO"
                                      print("final height pass fail here", I[i,0])
                              
                                #Ensure that the starting point is not in the negatives.
                              if xi >= 0:
                                  widthZeroPass = "YES"
                              else:
                                  widthZeroPass = "NO"
                              if yi >= 0:
                                  heightZeroPass = "YES"
                              else:
                                 heightZeroPass = "NO"
                                  
                              """
                                        This is a fail if:
                                        the x position of i plus width of i is less than or equal to the x position any rectangle in the set. 
                                        the x position of any rectangle plus width of next rectangle is less than or equal to position of xi (we want to work from left to right)
                                        the y position of i plus height of i is less than or equal to y position of any rectangle (j)
                                        the y position of next rectangle plus the height of next rectangle is less than or equal to height of i
                               """
                            
                              if widthPass == "NO" or widthZeroPass == "NO":
                                  I[i,3] = I[i,3] + 1
                                  xi = I[i,3]
                                  
                                  if I[i,3] + I[i,1] > 100: #We need to check if the box size exceeds the alotted space.
                                      I[i,3] = 0
                                      #nextYPass = "NO"
                                      unitPass = "NO"
                                      xi = I[i,3]
                                      
                                                                        
                                  
                              if heightPass == "NO" or heightZeroPass == "NO": # or nextYPass == "NO":
                                  ###print("Height Fail at height y coordinate", yi, "and x coord ", xi, "(I) row: ", I[i,0])
                                  I[i,4] = I[i,4] + 1
                                  unitPass = "NO"
                                  yi = I[i,4]
                                  
                                  
                              #If we get past here we now need to check and see if everything is a YES because
                              #if we have had a fail, we want it to loop back up the top, recheck everything
                              #and only pass if everything has been verified otherwise I want it to hunt for
                              #the next position.
                              
                              if widthPass == "YES" and heightPass == "YES" and widthZeroPass == "YES" and heightZeroPass == "YES":
                                  I[i,5] = 1 #This value is now set meaning each subsequent check will also include this one
                                  print("FULL PASS GIVEN")
                                  unitPass = "YES"
                                  overlapBurden = "NO"
                                  overlapPass = "YES"
                                  yi = 0
                                  #Re-initialise passes
                                  widthPass = "NO"
                                  heightPass = "NO"
                                  
                                  
                                  
                              else:
                                  unitPass = "NO"
                                  print("FULL PASS REVOKED")
                                  
                    
                          # Exit the While unitPass Statement (while unitPass == "NO":)- we have successfully placed this specific rectangle in the array
                          
                          #----> Dont need any code here, , so long as we have not reached the end of the array and
                          #the array items still have items left that have been set the unit pass will be reset to NO
                          #and at that point it will re-enter the loop and carry on through or it will exit 
                          
                      #Exit the If statement that checks to see if the rectangle has been placed yet (if I[j,0] != I[i,0] and I[i,5] != "0": )
                      
                      else:
                         I[i,5] = 1
                         firstCompleted = "YES"
                         ###print("i 5 is: ", I[i,0], " ", I[i,5])
                         ###print("j 5 is: ", I[j,0], " ", I[j,5])
                         
                    
                # Exit the (for j in range(len(I)):) - the loop that checks over the current array.
                
                #----> Everything has passed, reset the variable to boost us out of the while loop
               
                overlapBurden = "NO"
                
                #Exit the Overlap burden While statement (while overlapBurden != "NO":) - each array item we have passed through now has it's placement
            
            #----> The comparison between I[i] and I[j] is complete
            overlapPass = "YES"
            # Exit the overlapPass While statement Check (while overlapPass == "NO":)   
        
        # Exit the "for i in range(len(I)):" loop that ranges over the new array to hunt for placements
        checkindent = "YES"
        #----> Exiting this means a complete variable set has been run through. 
        #----> It is here we must now append our Tabu list with a sucessful placement if it meets placement criteria.
        #----> We must do the placement here otherwise we will lose the successful field placement.
        
    
        #Validate that the height of this solution does not exceed the baseline height
        vHMaxHeight = 0
        for vH in range(len(I)): 
        
            vHi = I[vH,2] #height of rectangle
            vHy = I[vH,4] #height of bottom of rectangle
            vHH = vHi+vHy # what is the height of this rectangle as it is placed on  the Y plane 
            
            if vHH > vHMaxHeight: #always checking to see if our rectangle is actually the highest
                vHMaxHeight = vHH
                print("vhmaxheight ", vHMaxHeight)
        
        vHArea = vHMaxHeight * 100 / 20
        
        
        
        if vHMaxHeight > MaxHeight:
            print("Discard Tabu because Height:", vHMaxHeight, " exceeds maximum of ", MaxHeight)
            tabu = "DISCARD"
        else:
            print("Add Tabu")
            tabu = "ADD"
            
        
        #for t in range(len(tabuList)):
         #   if tabuList[t,1] > vHMaxHeight:
          #      print("Tabu discard because over height", vHMaxHeight, MaxHeight)
          #      tabu = "DISCARD" #We don't want a repeat of solutions
        
        if tabu == "ADD":
            print("We are appending the Tabu List now")
            mylist = np.array([[solutionCount, vHMaxHeight]])
            np.append(tabu, mylist, axis=0)
            #Also add to the array of arrays with the height as a reference field
            #vMAXArray = np.array([[vHMaxHeight]]
            print("Tabu list is currently: ",tabuList)
            solutionCount = solutionCount + 1
            #arraysOfSolutions = arraysOfSolutions + [vHMaxHeight, I]
            #print("All solutions are: ", arraysOfSolutions)
       
        
        # Do this after adding to Tabu
        
       # if vHArea == optimumArea:
       #     solutionFound == "YES"
        
    
        count = count + 1
    
    #----> We now loop back through the while statement
    
        
        
        
    