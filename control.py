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
        temp.setEmployeeId(input("Employee ID: "))  # set employee ID
        temp.setEmployeeName(input("Employee Name: ")) # set employee name
        temp.setCommissions(input("Commissions: ")) # set commissions
        employeeData.append(temp) # add employee object to list

    def updateEmployee(self): # method to update employee details
        print("Update employee details:") # prompt user to enter employee details
        empId = input("Enter employee ID to update: ") # get employee ID to update
        for emp in employeeData: # iterate through employee list
            if emp.getEmployeeId() == empId: # check if employee ID matches
                emp.setEmployeeName(input("Employee Name: ")) # update employee name
                emp.setCommissions(input("Commissions: ")) # update commissions
                break
        else: # if employee ID not found
            print("Employee not found.") # print error message

    def deleteEmployee(self): # method to delete employee details
        print("Delete employee details:") # prompt user to enter employee details
        empId = input("Enter employee ID to delete: ") # get employee ID to delete
        for emp in employeeData: # iterate through employee list
            if emp.getEmployeeId() == empId: # check if employee ID matches
                employeeData.remove(emp) # remove employee object from list
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
        inventoryData.append(temp) # add inventory object to list

    def updateInventory(self): # method to update inventory details
        print("Update inventory details:") # prompt user to enter inventory details
        vehicleId = input("Enter vehicle ID to update: ") # get vehicle ID to update
        for inv in inventoryData: # iterate through inventory list
            if inv.getVehicleID() == vehicleId: # check if vehicle ID matches 
                inv.setPurchasePrice(input("Purchase Price: "))  # update purchase price
                inv.setSalesPrice(input("Sales Price: ")) # update sales price
                break
        else: # if vehicle ID not found
            print("Vehicle not found.") # print error message

    def deleteInventory(self): # method to delete inventory details
        print("Delete inventory details:") # prompt user to enter inventory details
        vehicleId = input("Enter vehicle ID to delete: ") # get vehicle ID to delete
        for inv in inventoryData: # iterate through inventory list
            if inv.getVehicleID() == vehicleId: # check if vehicle ID matches
                inventoryData.remove(inv) # remove inventory object from list
                break 
        else: # if vehicle ID not found
            print("Vehicle not found.") # print error message

    def getInventory(self): # method to get inventory details
        print("Inventory details:") # prompt user to enter inventory details
        for inv in inventoryData: # iterate through inventory list
            print("-----------------------------") # print separator
            print("Vehicle ID: ", inv.getVehicleID())   # print vehicle ID
            print("Purchase Price: ", inv.getPurchasePrice())   # print purchase price
            print("Sales Price: ", inv.getSalesPrice())  # print sales price
            print("Service Record: ")   # print service record details
            for sr in serviceRecordData:    # iterate through service record list
                if sr.getVehicleID() == inv.getVehicleID(): # check if vehicle ID matches
                    print("Service ID: ", sr.getServiceID())    # print service ID
                    print("Service Price: ", sr.getServicePrice())  # print service price
            print("-----------------------------") # print separator

    def addServiceRecord(self): # method to add service record details
        temp = entity.ServiceRecord() # create a new service record object
        print("Enter service record details:")  # prompt user to enter service record details
        temp.setServiceID(input("Service ID: "))    # set service ID
        temp.setVehicleID(input("Vehicle ID: "))    # set vehicle ID
        temp.setServicePrice(input("Service Price: "))  # set service price
        serviceRecordData.append(temp)  # add service record object to list

    def updateServiceRecord(self): # method to update service record details
        print("Update service record details:") # prompt user to enter service record details
        serviceId = input("Enter service ID to update: ")   # get service ID to update
        for sr in serviceRecordData:    # iterate through service record list
            if sr.getServiceID() == serviceId:  # check if service ID matches
                sr.setVehicleID(input("Vehicle ID: "))  # update vehicle ID
                sr.setServicePrice(input("Service Price: "))    # update service price
                break
        else:   # if service ID not found
            print("Service record not found.")  # print error message

    def deleteServiceRecord(self): # method to delete service record details
        print("Delete service record details:") # prompt user to enter service record details
        serviceId = input("Enter service ID to delete: ")   # get service ID to delete
        for sr in serviceRecordData:    # iterate through service record list
            if sr.getServiceID() == serviceId:  # check if service ID matches
                serviceRecordData.remove(sr)    # remove service record object from list
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
        customerData.append(temp)   # add customer object to list

    def updateCustomer(self): # method to update customer details
        print("Update customer details:")   # prompt user to enter customer details
        custId = input("Enter customer ID to update: ")   # get customer ID to update
        for cust in customerData:   # iterate through customer list
            if cust.getCustomerID() == custId:  # check if customer ID matches
                cust.setCustomerName(input("Customer Name: "))  # update customer name
                cust.setAddress(input("Address: "))  # update address
                break
        else:   # if customer ID not found
            print("Customer not found.")    # print error message

    def deleteCustomer(self): # method to delete customer details
        print("Delete customer details:")   # prompt user to enter customer details
        custId = input("Enter customer ID to delete: ")  # get customer ID to delete
        for cust in customerData:   # iterate through customer list
            if cust.getCustomerID() == custId:  # check if customer ID matches
                customerData.remove(cust)   # remove customer object from list
                break
        else:   # if customer ID not found
            print("Customer not found.")    # print error message
    