print("EMPLOYEE SYSTEM!!!!!!!!!!!!")
emp=dict()
cab=dict()
emp_id=1
def func_hr(emp_id):
    n=int(input("enter the num"))
    for i in range (1,n+1):
        name=input("name")
        salary=int(input("salary"))
        increament=int(input("increament"))
        emp[i]={"name":name,
                     "salary":salary,
                     "increament":increament
                    }
def func_logistics():
    cab[1]={"12":"rajnagar extension",
           "21":"shastri nagar",
           "58":"vaishali"
           }
def func_emp():
    print(emp)
    print(cab)
func_hr(emp_id)
func_logistics()
func_emp()
    
        
            
            
            
    
    

