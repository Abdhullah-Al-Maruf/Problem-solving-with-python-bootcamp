# # def calculator (firstNumber,secondNumber,symbol):
# #     print(firstNumber,secondNumber,symbol)


# # # function calling
# # calculator(4,56,"+")

def calculator (firstNumber,secondNumber,symbol):
    
    # function body
    if(symbol=="+"):
        sum= firstNumber+secondNumber
        print(sum)

    elif(symbol=="-"):
        sub=firstNumber -secondNumber
        print(sub) 

    elif(symbol=="*"):
        return firstNumber * secondNumber
          

    elif(symbol=="/"):
        div=firstNumber -secondNumber
        print(f"{firstNumber}/{secondNumber}=" ,div)  
    else:
        modulus= firstNumber % secondNumber 
        print(modulus)    
        # return firstNumber+secondNumber


print(calculator(44555,776,"*"))
calculator(4444,666,"/")


# # plus=calculator(44,55,"+")
# # print(plus)
# # calculator(44,55,"+")
# # print(calculator(44,55,"+"))

# num=int(input("enter your number"))
# num2=int(input("enter your number"))
# sub= num-num2

# print(f"{num} - {num2}= ", sub)

# # 
# def showName():
#   number=5

   

# # 1 function will end there 
  
 
# num =showName()
# print(num)