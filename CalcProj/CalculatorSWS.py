


class Calc:
    def __init__(self, numx, numy):
        

        self.num1 = numx;
        self.num2 = numy;
        self.ans = 0;
    


    def add(self):
    
        self.ans = self.num1 + self.num2;
        
        return print(self.ans)
       

    def sub(self):
       
        self.ans = self.num1 - self.num2;
       
        return print(self.ans)
        

    def div(self):
        
        self.ans = self.num1 / self.num2;
       
        return print(self.ans)
       

    def mul(self):
       
        self.ans = self.num1 * self.num2;
        
        return print(self.ans)
        


    
    def endCalc(self):
        exit();



    
