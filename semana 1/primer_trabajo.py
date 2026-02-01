def main():
    x=(int(input("Digite un numero: ")))
    if(x<0):
        print("el numero es negativo")
    elif(x>0):
        if(x%x==0 or x%1==0):
            print("el numero es primo")
        for i in range (x):
            fibo=x[i-1]+x[i-2]
            if(x==fibo):
                print("el numero es fibo")
        print("el numero es positivo")
    elif(x==0):
        print("el numero es cero")
   
    
main()