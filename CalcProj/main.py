



def init(): #what to do automaticlly when game starts
    import CalculatorSWS as c
    y = 'Y';
    n = 'N';

    userIn = input("Start[Y/N]: ").upper()
     

    while userIn:
        
        if userIn[:1] == y:
            i = input("num1[?]: ")
            ii = input("num2[?]: ")

            calc = c.Calc(int(i), int(ii))

            operation(i,ii,calc)

            print("\n")
            print("____Calculator_______")

          
        elif userIn[:1] == n:
            exit()
            break

        userIn = input("Start[Y/N]: ").upper()


def operation(A,B,C):
    while(A != 0 and B != 0):
        print("Select Operation: ADD, SUB, DIV, MUL, EXT" + "\n")
        print("Your nums: " + A + " , " + B)
        opIn = input("operation[?]: ")
        if opIn == 'ADD':
            C.add()
        if opIn == 'SUB':
            C.sub()
        
        if opIn == 'DIV':
            C.div()
        
        if opIn == 'MUL':
            C.mul()
    
        if opIn == 'EXT':
            C.endCalc()
    
    



##Script to auto run the promgram/main only
if __name__ == '__main__':
    init()
#all rights resrved for @SoWhatStudios & @MrSoWhat
