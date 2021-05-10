# -*- coding: utf-8 -*-
"""
Created on Sun May  9 20:05:40 2021

@author: Gautam Agarwal
"""

class CustomerManagement:
    def __init__(self,):
        print("<-----CUSTOMER MANAGEMENT SYSTEM----->\n")
        self.customer_id = []
        self.customer_name = []
        self.customer_mobile = []
        
    def addCustomer(self,cust_id,name,mobile):
        self.customer_id.append(cust_id)
        self.customer_name.append(name)
        self.customer_mobile.append(mobile)
        return "\n\ncustomer has been added in our system!\n\n"
        
    def updateCustomer(self,cust_id,name,mobile):
        indexNumber =self.customer_id.index(cust_id)
        self.customer_name[indexNumber] = name
        self.customer_mobile[indexNumber] =mobile
        
    def deleteCustomer(self,customer_id):
        indexNumber =self.customer_id.index(customer_id)  
        self.customer_id.pop(indexNumber)
        self.customer_name.pop(indexNumber)
        self.customer_mobile.pop(indexNumber)
        return "The customer details of customer id {cust_id} has been deleted \n"
        
    def viewCustomer(self,cust_id):
        indexNumber =self.customer_id.index(cust_id)  
        name = self.customer_name[indexNumber]
        mobile = self.customer_mobile[indexNumber]
        return name,mobile 
               
       
    def viewAllCustomer(self):
          
          return (self.customer_id,
        self.customer_name,
        self.customer_mobile)     
      
cm_obj = CustomerManagement() 

while True:
      def menu():           
           print("add customer: Type 1 and press enter\n")
           print("update customer: Type 2 and press enter\n")
           print("delete customer: Type 3 and press enter\n")
           print("view customer details: Type 4 and press enter\n")
           print("view all customers details: Type 5 and press enter\n")
           print("type 6 for exit")    
      menu()
      oper = (input("Enter your choice:"))
      if oper == "1":
           cust_id = int(input("enter new customer id:::"))
           name = input("enter new customer name:::")
           mobile = int(input("enter new customer mobile number:::"))
           oper1 =  cm_obj.addCustomer(cust_id,name,mobile)
           print(oper1)       
           
           
      elif oper == "2":
           cust_id = int(input("enter the customer id to update the details:::"))
           name = input("enter the update name:::")
           mobile = int(input("enter the update mobile number:::"))
           oper2 = cm_obj.updateCustomer(cust_id,name,mobile)
           print(f"The name and mobile number of customer id  {cust_id} has been updated in our system!\n")
           
           
      elif oper == "3":
           cust_id = int(input("enter the customer id to delete the details:::"))
           oper3 =  cm_obj.deleteCustomer(cust_id)
           print(oper3.format(cust_id=cust_id))
           
           
      elif oper == "4":
         cust_id = int(input("enter the customer id to view the details:::"))
         oper4 = cm_obj.viewCustomer(cust_id)
         print(f"The customer id is {cust_id} , name of  customer is {oper4[0]} and the mobile numnber of customer is {oper4[1]}\n\n") 
       
      elif oper == "5":
          oper5=cm_obj.viewAllCustomer()
          print("customer_id\tcustomer_name\tcustomer_mobileNumber")
          for x in range(len(cm_obj.customer_id)):
              print(f"{oper5[0][x]}\t\t{oper5[1][x]}\t\t{oper5[2][x]}\n\n")                
     
      elif oper =="6":
        print("BYE BYE")
        break
      else:
          print("You choose invalid operation")
