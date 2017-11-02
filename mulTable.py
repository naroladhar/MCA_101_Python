import pdb
pdb.set_trace()

def mulTable(num,uIndexLimit):
    '''
    Objective : To create a multiplication table of numbers
    Input Variables :
        num : A number
        uIndexLimit: The size of the multiplication table
    Output Variables: 
        res : The result of the product
    return value:none 
    '''
    for i in range(0,uIndexLimit+1):
        res=num*i
        print("%d X %d = %d" %(num,i,res))
def main():
    '''
        Objective : To create a multiplication table of numbers
        Input Variables :
            num : A number
            uIndexLimit: The size of the multiplication table
        Output Variables:
            res : The result of the product
        return value:none
    '''
    start=int(input(" Enter a start: "))
    finish = int(input(" Enter a finish: "))
    uIndexLimit = int(input(" Enter size of the table: "))
    for start in range(start,finish+1):
        print("*******Time Table for ",start,"*********")
        mulTable(start,uIndexLimit)
if __name__=='__main__':
    main()
