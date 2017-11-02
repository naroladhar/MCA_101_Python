import pdb
pdb.set_trace()
def calcPercentage( totalMarks , maxMarks ):
    
    '''
      objective: To calculate the percentage of the marks obtained by a student
      approach: -> Dividing total marks by maximum
                -> Multiplying this result with 100 to produce the final result
      parameters: -> totalMarks : Total marks obtained by students
                  -> maxMarks : Maximum marks that can be obtained
      return value: Percentage calculated
    '''
    # Enter Your Code Here
    percentage = totalMarks / maxMarks * 100
    return percentage
    
def main():
    
    '''
     objective: To calculate the total percentage of the marks obtained by students in different subjects 
     approach: ->Taking total marks as input from user
               ->Passing total marks to function calcPercentile as parameter
    '''

    # Enter Your Code Here
    totalMarks = int(input(" Enter your total mark : "))
    maxMarks = int(input(" Enter the maximum marks : "))
    
    print( "Marks obtained = " , totalMarks)
    print( "Maximum Marks  = " , maxMarks)
    print( "Percentage = " , calcPercentage( totalMarks , maxMarks ) )
    
    print(" End of main ")
    
if __name__ == "__main__":
    main()
print(" End of program ")
