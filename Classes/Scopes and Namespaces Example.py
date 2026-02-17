
def Scope_testing():
    x='It is namespace..... '
    
    def Local():
        x = ' local Kartik'
        print("1.inside the local function:",x)
          
    def Non_local():
        nonlocal x
        x=' nlocal kartik'
                         
    def Global():
        global x
        x =' global kartik'
        print(f'5.inside the global function it is:{x}')
    print(f'6.outside the global function is:::::{x}')
                
           
    Local()
    print(f'2.outside the function value of x is:::::: {x}')
    Non_local()
    print(f'4.value of x outside the non local function is ::::{x}')
    Global()
    print(f'3.value of x inside the non local function is: {x}')
     
    
Scope_testing()
print(f'7.aftter global scope:{x}')



# local: it is for the own method aur function
# nonlocal: it is used to defined outer class from inner class like from non local() to the scope_testing() or function of variable
# global: it used to defined variable outside the function or class outside scope_testing()


