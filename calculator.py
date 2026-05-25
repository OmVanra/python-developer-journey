class calculator:
    def __init__(self):
        pass

    def add(self,a,b):
        return a+b
    def sub(self,a,b):
        return a-b
    def mul(self,a,b):
        return a*b
    def div(self,a,b):
        return a/b            
    def main(self):
        while True:
            print("*"*26)
            print("*  Simple  Calculator  *")
            print("*"*26)
            print("1. for addition")
            print("2. for subtraction")
            print("3. for multiplication")
            print("4. for division")
            print("5. exit")
            print("*"*26)
            choice = int(input("Enter your choice: "))

            a = int(input("Enter first number:"))
            b = int(input("Enter secound number:"))
            if(choice == 1):
                print("Result:",self.add(a,b))
            elif(choice == 2):
                print("Result:",self.sub(a,b))
            elif(choice == 3):
                print("Result:",self.mul(a,b))
            elif(choice == 4):
                print("Result:",self.div(a,b))
            elif(choice == 5):
                break
            else:
                print("Invalid choice!")
if __name__ == "__main__":
    c = calculator()
    c.main()