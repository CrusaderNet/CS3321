import entity

# Class to manage employees
# This class contains methods to add, update and delete employee details
# The employee details are stored in a list of employee objects
# Contributors: Seth Tourish
# Date: 11/28/2024
class ManageEmployees:
    employeeData = [] # list of employee objects

    def addEmployee(self): # method to add employee details
        temp = entity.Employee() # create a new employee object
        print("Enter employee details:") # prompt user to enter employee details
        temp.setEmployeeID(input("Employee ID: "))  # set employee ID
        temp.setEmployeeName(input("Employee Name: ")) # set employee name
        temp.setCommissions(input("Commissions: ")) # set commissions
        self.employeeData.append(temp) # add employee object to list

    def updateEmployee(self): # method to update employee details
        print("Update employee details:") # prompt user to enter employee details
        empId = input("Enter employee ID to update: ") # get employee ID to update
        for emp in self.employeeData: # iterate through employee list
            if emp.getEmployeeID() == empId: # check if employee ID matches
                emp.setEmployeeName(input("Employee Name: ")) # update employee name
                emp.setCommissions(input("Commissions: ")) # update commissions
                break
        else: # if employee ID not found
            print("Employee not found.") # print error message

    def deleteEmployee(self): # method to delete employee details
        print("Delete employee details:") # prompt user to enter employee details
        empId = input("Enter employee ID to delete: ") # get employee ID to delete
        for emp in self.employeeData: # iterate through employee list
            if emp.getEmployeeID() == empId: # check if employee ID matches
                self.employeeData.remove(emp) # remove employee object from list
                break
        else: # if employee ID not found
            print("Employee not found.") # print error message

# Class to manage Inventory
# This class contains methods to add, update and delete inventory details, and service record details
# The inventory details are stored in a list of inventory objects and service record details are stored in a list of service record objects
# Contributors: Seth Tourish
# Date: 11/28/2024
class ManageInventory:
    inventoryData = [] # list of inventory objects
    serviceRecordData = [] # list of service record objects

    def addInventory(self): # method to add inventory details
        temp = entity.Inventory() # create a new inventory object
        print("Enter inventory details:") # prompt user to enter inventory details
        temp.setVehicleID(input("Vehicle ID: ")) # set vehicle ID
        temp.setPurchasePrice(input("Purchase Price: ")) # set purchase price
        temp.setSalesPrice(input("Sales Price: ")) # set sales price
        self.inventoryData.append(temp) # add inventory object to list

    def updateInventory(self): # method to update inventory details
        print("Update inventory details:") # prompt user to enter inventory details
        vehicleId = input("Enter vehicle ID to update: ") # get vehicle ID to update
        for inv in self.inventoryData: # iterate through inventory list
            if inv.getVehicleID() == vehicleId: # check if vehicle ID matches 
                inv.setPurchasePrice(input("Purchase Price: "))  # update purchase price
                inv.setSalesPrice(input("Sales Price: ")) # update sales price
                break
        else: # if vehicle ID not found
            print("Vehicle not found.") # print error message

    def deleteInventory(self): # method to delete inventory details
        print("Delete inventory details:") # prompt user to enter inventory details
        vehicleId = input("Enter vehicle ID to delete: ") # get vehicle ID to delete
        for inv in self.inventoryData: # iterate through inventory list
            if inv.getVehicleID() == vehicleId: # check if vehicle ID matches
                self.inventoryData.remove(inv) # remove inventory object from list
                break 
        else: # if vehicle ID not found
            print("Vehicle not found.") # print error message

    #method to return array of inventory objects
    def getInventory(self):
        return self.inventoryData 
    
    def addServiceRecord(self): # method to add service record details
        temp = entity.ServiceRecord() # create a new service record object
        print("Enter service record details:")  # prompt user to enter service record details
        temp.setServiceID(input("Service ID: "))    # set service ID
        temp.setVehicleID(input("Vehicle ID: "))    # set vehicle ID
        temp.setServicePrice(input("Service Price: "))  # set service price
        self.serviceRecordData.append(temp)  # add service record object to list

    def updateServiceRecord(self): # method to update service record details
        print("Update service record details:") # prompt user to enter service record details
        serviceId = input("Enter service ID to update: ")   # get service ID to update
        for sr in self.serviceRecordData:    # iterate through service record list
            if sr.getServiceID() == serviceId:  # check if service ID matches
                sr.setVehicleID(input("Vehicle ID: "))  # update vehicle ID
                sr.setServicePrice(input("Service Price: "))    # update service price
                break
        else:   # if service ID not found
            print("Service record not found.")  # print error message

    def deleteServiceRecord(self): # method to delete service record details
        print("Delete service record details:") # prompt user to enter service record details
        serviceId = input("Enter service ID to delete: ")   # get service ID to delete
        for sr in self.serviceRecordData:    # iterate through service record list
            if sr.getServiceID() == serviceId:  # check if service ID matches
                self.serviceRecordData.remove(sr)    # remove service record object from list
                break
        else:   # if service ID not found
            print("Service record not found.") # print error message

# Class to manage Customers
# This class contains methods to add, update and delete customer details
# The customer details are stored in a list of customer objects
# Contributors: Seth Tourish
# Date: 11/28/2024
class ManageCustomers:
    customerData = [] # list of customer objects

    def addCustomer(self): # method to add customer details
        temp = entity.Customer()    # create a new customer object
        print("Enter customer details:")    # prompt user to enter customer details
        temp.setCustomerID(input("Customer ID: "))  # set customer ID
        temp.setCustomerName(input("Customer Name: "))  # set customer name
        temp.setAddress(input("Address: "))   # set address
        self.customerData.append(temp)   # add customer object to list

    def updateCustomer(self): # method to update customer details
        print("Update customer details:")   # prompt user to enter customer details
        custId = input("Enter customer ID to update: ")   # get customer ID to update
        for cust in self.customerData:   # iterate through customer list
            if cust.getCustomerID() == custId:  # check if customer ID matches
                cust.setCustomerName(input("Customer Name: "))  # update customer name
                cust.setAddress(input("Address: "))  # update address
                break
        else:   # if customer ID not found
            print("Customer not found.")    # print error message

    def deleteCustomer(self): # method to delete customer details
        print("Delete customer details:")   # prompt user to enter customer details
        custId = input("Enter customer ID to delete: ")  # get customer ID to delete
        for cust in self.customerData:   # iterate through customer list
            if cust.getCustomerID() == custId:  # check if customer ID matches
                self.customerData.remove(cust)   # remove customer object from list
                break
        else:   # if customer ID not found
            print("Customer not found.")    # print error message

# Class to Finalize Purchase
# This class contains a method to finalize purchase and set commissions
# Contributors: Seth Tourish
# Date: 11/30/2024
class FinalizePurchase:
    def FinalizePurchase(self, manageFinancialObj, calcEmployeeCommissionOBJ):    # method to finalize purchase
        manageFinancialObj.addSales()  # call addSales method
        manageFinancialObj.salesData[-1].setCommissions(calcEmployeeCommissionOBJ.calcEmployeeComm(float(manageFinancialObj.salesData[-1].getPrice())))    # set commissions
        manageFinancialObj.addReceipt()    # call addReceipt method

# Class to Manage Financials
# This class contains methods to add, update and delete receipt, lease, sales, financial and application details
# The receipt details are stored in a list of receipt objects, lease details are stored in a list of lease objects, sales details are stored in a list of sales objects, 
# financial details are stored in a list of financial objects and application details are stored in a list of application objects
# Contributors: Seth Tourish
# Date: 11/30/2024
class ManageFinancials:
    receiptData = [] # list of receipt objects
    leaseData = [] # list of lease objects
    salesData = [] # list of sales objects
    financialData = [] # list of financial objects
    applicationData = [] # list of application objects

    def addReceipt(self): # method to add receipt details
        temp = entity.Receipt() # create a new receipt object
        print("Enter receipt details:") # prompt user to enter receipt details
        temp.setSalesID(input("Sales ID: ")) # set sales ID
        temp.setCustomerID(input("Customer ID: "))  # set customer ID
        temp.setPrice(input("Price: ")) # set price
        temp.setLeaseID(input("Lease ID: ")) # set lease ID
        self.receiptData.append(temp)
    
    def updateReceipt(self): # method to update receipt details
        print("Update receipt details:")    # prompt user to enter receipt details
        salesId = input("Enter sales ID to update: ")   # get sales ID to update
        for rec in self.receiptData: # iterate through receipt list
            if rec.getSalesID() == salesId: # check if sales ID matches
                rec.setCustomerID(input("Customer ID: "))   # update customer ID
                rec.setPrice(input("Price: "))  # update price
                rec.setLeaseID(input("Lease ID: ")) # update lease ID
                break   
        else:   # if sales ID not found
            print("Receipt not found.") # print error message

    def deleteReceipt(self): # method to delete receipt details
        print("Delete receipt details:")    # prompt user to enter receipt details
        salesId = input("Enter sales ID to delete: ")   # get sales ID to delete
        for rec in self.receiptData: # iterate through receipt list
            if rec.getSalesID() == salesId: # check if sales ID matches
                self.receiptData.remove(rec) # remove receipt object from list
                break
        else:   # if sales ID not found
            print("Receipt not found.")

    def addLease(self): # method to add lease details
        temp = entity.Lease()
        print("Enter lease details:")   # prompt user to enter lease details
        temp.setLeaseID(input("Lease ID: "))    # set lease ID
        temp.setCustomerID(input("Customer ID: "))  # set customer ID
        temp.setVehicleID(input("Vehicle ID: "))    # set vehicle ID
        temp.setMonthlyPayment(input("Monthly Payment: "))  # set monthly payment
        temp.setPrice(input("Price: ")) # set price
        temp.setTermLength(input("Term Length: "))  # set term length
        self.leaseData.append(temp)  # add lease object to list
    
    def updateLease(self): # method to update lease details
        print("Update lease details:")  # prompt user to enter lease details
        leaseId = input("Enter lease ID to update: ")   # get lease ID to update
        for lea in self.leaseData:   # iterate through lease list
            if lea.getLeaseID() == leaseId: # check if lease ID matches
                lea.setCustomerID(input("Customer ID: "))  # update customer ID
                lea.setVehicleID(input("Vehicle ID: "))   # update vehicle ID
                lea.setMonthlyPayment(input("Monthly Payment: "))   # update monthly payment
                lea.setPrice(input("Price: "))  # update price
                lea.setTermLength(input("Term Length: "))   # update term length
                break
        else:   # if lease ID not found
            print("Lease not found.")   # print error message
    
    def deleteLease(self): # method to delete lease details
        print("Delete lease details:")  # prompt user to enter lease details
        leaseId = input("Enter lease ID to delete: ")   # get lease ID to delete
        for lea in self.leaseData:   # iterate through lease list
            if lea.getLeaseID() == leaseId: # check if lease ID matches
                self.leaseData.remove(lea)   # remove lease object from list
                break
        else:   # if lease ID not found
            print("Lease not found.")   # print error message
    
    def addSales(self): # method to add sales details
        temp = entity.Sales()   # create a new sales object
        print("Enter sales details:")   # prompt user to enter sales details
        temp.setSaleID(input("Sales ID: "))    # set sales ID
        temp.setEmployeeID(input("Employee ID: "))    # set employee ID
        temp.setCustomerID(input("Customer ID: "))    # set customer ID
        temp.setLeaseID(input("Lease ID: "))  # set lease ID
        temp.setApplicationID(input("Application ID: "))  # set application ID
        temp.setReceiptID(input("Receipt ID: "))    # set receipt ID
        temp.setPrice(input("Price: "))    # set price
        self.salesData.append(temp)  # add sales object to list

    def updateSales(self): # method to update sales details
        print("Update sales details:")  # prompt user to enter sales details
        salesId = input("Enter sales ID to update: ")   # get sales ID to update
        for sal in self.salesData:   # iterate through sales list
            if sal.getSaleID() == salesId: # check if sales ID matches
                sal.setEmployeeID(input("Employee ID: "))    # update employee ID
                sal.setCustomerID(input("Customer ID: "))   # update customer ID
                sal.setLeaseID(input("Lease ID: ")) # update lease ID
                sal.setApplicationID(input("Application ID: "))  # update application ID
                sal.setCommissions(input("Commissions: "))  # update commissions
                sal.setReceiptID(input("Receipt ID: ")) # update receipt ID
                sal.setPrice(input("Price: "))  # update price
                break
        else:   # if sales ID not found
            print("Sales not found.")   # print error message

    def deleteSales(self): # method to delete sales details
        print("Delete sales details:")  # prompt user to enter sales details
        salesId = input("Enter sales ID to delete: ")   # get sales ID to delete
        for sal in self.salesData:   # iterate through sales list
            if sal.getSaleID() == salesId: # check if sales ID matches
                self.salesData.remove(sal)   # remove sales object from list
                break
        else:   # if sales ID not found
            print("Sales not found.")   # print error message

    def addFinancial(self): # method to add financial details
        temp = entity.FinancialRecord()   # create a new financial object
        print("Enter financial details:")    # prompt user to enter financial details
        temp.setBudget(float(input("Budget: ")))   # set budget
        temp.setRevenue(float(input("Revenue: ")))  # set revenue
        temp.setExpenses(float(input("Expenses: ")))    # set expenses
        self.financialData.append(temp)  # add financial object to list

    def deleteFinancial(self):  # method to delete financial details
        print("Delete financial details:")   # prompt user to enter financial details 
        for fin in self.financialData:   # iterate through financial list
            self.financialData.remove(fin)   # remove financial object from list 

    def addApplication(self):   # method to add application details
        temp = entity.Application()
        print("Enter application details:") # prompt user to enter application details
        temp.setApplicationID(input("Application ID: "))    # set application ID
        temp.setCustomerID(input("Customer ID: "))  # set customer ID
        temp.setSaleID(input("Sale ID: "))  # set sale ID
        temp.setCreditScore(input("Credit Score: "))    # set credit score
        temp.setPrice(input("Price: "))    # set price 
        temp.setIncome(input("Income: "))  # set income
        self.applicationData.append(temp)

    def updateApplication(self):    # method to update application details
        print("Update application details:")    # prompt user to enter application details
        appId = input("Enter application ID to update: ")   # get application ID to update
        for app in self.applicationData: # iterate through application list
            if app.getApplicationID() == appId: # check if application ID matches
                app.setCustomerID(input("Customer ID: "))    # update customer ID
                app.setSaleID(input("Sale ID: "))   # update sale ID
                app.setCreditScore(input("Credit Score: ")) # update credit score
                app.setPrice(input("Price: "))  # update price
                app.setIncome(input("Income: "))    # update income
                break
        else:   # if application ID not found
            print("Application not found.")
    
    def deleteApplication(self):    # method to delete application details
        print("Delete application details:")    # prompt user to enter application details
        appId = input("Enter application ID to delete: ")   # get application ID to delete
        for app in self.applicationData: # iterate through application list
            if app.getApplicationID() == appId: # check if application ID matches
                self.applicationData.remove(app) # remove application object from list
                break
        else:   # if application ID not found
            print("Application not found.")   # print error message

    def updateApplicationStatus(self, appID: str, status: str):    # method to update application status
        for app in self.applicationData: # iterate through application list
            if app.getApplicationID() == appID: # check if application ID matches
                app.setStatus(status)   # update application status
                break
        else:   # if application ID not found
            print("Application not found.")  # print error message
    
    def getSales(self) -> entity.Sales: # method to get a sales record
        print("Sales details:") # prompt user to enter sales details
        salesId = input("Enter sales ID: ") # get sales ID
        for sal in self.salesData:   # iterate through sales list
            if sal.getSalesID() == salesId: # check if sales ID matches
                return sal  # return sales object
        else:   # if sales ID not found
            print("Sales not found.")   # print error message

    def getFinancial(self) -> entity.FinancialRecord:
        if not self.financialData:  # Check if the list is empty
            return None  # Return None or handle it as per your application logic
        return self.financialData[-1]  # Return the most recent financial record

# Class to Manage Inquiries
# This class contains methods to add and print inquiry details
# The inquiry details are stored in a list of inquiry objects
# Contributors: Seth Tourish
# Date: 11/30/2024
class ManageInquiry:
    inquiryData = [] # list of inquiry objects

    def addInquiry(self):   # method to add inquiry details
        temp = entity.Inquiry()    # create a new inquiry object
        print("Enter inquiry details:")  # prompt user to enter inquiry details
        temp.setCustomerID(input("Customer ID: "))  # set customer ID
        temp.setVehicleID(input("Vehicle ID: "))    # set vehicle ID
        self.inquiryData.append(temp)    # add inquiry object to list

    def getInquiry(self): # method to print inquiry details
        print("Inquiry details:")   # Section Header
        for inq in self.inquiryData: # iterate through inquiry list
            print("Customer ID: ", inq.getCustomerID())    # print customer ID
            print("Vehicle ID: ", inq.getVehicleID())   # print vehicle ID
            print("-----------------------------")  # print separator

# Method to Control User Logins
# This class contains methods to add, update, delete and login user details
# The user details are stored in a list of login objects
# Contributors: Seth Tourish
# Date: 11/30/2024
class UserLogin:
    loginData = []  # list of login objects

    def addLogin(self): # method to add login details
        temp = entity.Login()   # create a new login object
        print("Enter login details:")   # prompt user to enter login details
        temp.setLoginID(input("loginID (First Character E, M, or C depending on user role): "))    # set username
        temp.setPassword(input("Password: "))  # set password
        self.loginData.append(temp)  # add login object to list

    def updateLogin(self):  # method to update login details
        print("Update login details:")  # prompt user to enter login details
        loginID = input("Enter login ID to update: ")   # get login ID to update
        for log in self.loginData:   # iterate through login list
            if log.getLoginID() == loginID:  # check if login ID matches
                log.setPassword(input("Password: "))    # update password
                break
        else:   # if login ID not found
            print("Login not found.")   # print error message

    def deleteLogin(self):  # method to delete login details
        print("Delete login details:")  # prompt user to enter login details
        loginID = input("Enter login ID to delete: ")   # get login ID to delete
        for log in self.loginData:   # iterate through login list
            if log.getLoginID() == loginID: # check if login ID matches
                loginData.remove(log)   # remove login object from list
                break
        else:   # if login ID not found
            print("Login not found.")   # print error message

    def login(self, loginID: str, password: str) -> bool:    # method to login
        for log in self.loginData:   # iterate through login list
            if log.getLoginID() == loginID and log.getPassword() == password:    # check if login ID and password matches
                return True # return true if login successful
        else:   # if login ID or password not found
            return False    # return false if login unsuccessful

