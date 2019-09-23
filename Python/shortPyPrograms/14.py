#access specifiers

# Public -
# Protected -
# Private -

class Employee:
    
    var = 8
    _protec = 9
    __pr = 98

emp = Employee()
print(emp.var)  #Accesssing public
print(emp._protec)  #Accessing protected
print(emp._Employee__pr)    #Accessing private
