import entity
import control

# Class to view inventory objects
# This class will be used to view the inventory objects
# Contributors: Seth Tourish
# Date: 12/1/2024
class ViewInventory:
    def viewInventory(self, inventoryData):
        for inv in inventoryData: # iterate through inventory list
            print("Vehicle ID: ", inv.getVehicleID())   # print vehicle ID
            print("Purchase Price: ", inv.getPurchasePrice())   # print purchase price
            print("Sales Price: ", inv.getSalesPrice())  # print sales price
            print("-----------------------------") # print separator

# Class to generate a financial report
# This class will be used to generate a financial report
# Contributors: Seth Tourish
# Date: 12/1/2024
class GenerateFinancialReport:
    def generateReport(self, financialObject):
        if financialObject is None:  # Check if financialObject is None
            print("No financial data available to generate the report.")
            print("-----------------------------")
            return
        print("Budget: ", financialObject.getBudget())  # Print budget
        print("Revenue: ", financialObject.getRevenue())  # Print revenue
        print("Expenses: ", financialObject.getExpenses())  # Print expenses
        print("Profit: ", financialObject.getRevenue() - financialObject.getExpenses())  # Print profit
        print("-----------------------------")  # Print separator

# Class to Approve or Deny Applications
# This class will be used to approve or deny applications
# Contributors: Seth Tourish
# Date: 12/1/2024
class ApproveDenyApplications:
    def approveApplication(self, appID : int, manageFinancialsObject : control.ManageFinancials):
        manageFinancialsObject.updateApplicationStatus(appID, "Y") # update application status to approved
        print("Application Approved")   # print application approved
        print("-----------------------------")  # print separator

    def denyApplication(self, appID : int, manageFinancialsObject : control.ManageFinancials):
        manageFinancialsObject.updateApplicationStatus(appID, "N") # update application status to denied
        print("Application Denied") # print application denied
        print("-----------------------------")  # print separator

# Class to calculate employee Commissions
# This class will be used to calculate employee commissions
# Contributors: Seth Tourish
# Date: 12/1/2024
class CalculateEmployeeCommission:
    def calcEmployeeComm(self, price : float) -> float:
        return price * 0.10 # return 10% of sales price

# Class to View Application Results
# This class will be used to view application results
# Contributors: Seth Tourish
# Date: 12/1/2024
class ViewApplicationResults:
    def viewResult(self, manageFinancialObj : control.ManageFinancials):    # function to view application results
        inputAppID = input("Enter Application ID: ") # get application ID from user
        for app in manageFinancialObj.applicationData:  # iterate through application list
            if app.getApplicationID() == inputAppID:    # if application ID matches
                print("Application ID: ", app.getApplicationID())   # print application ID
                print("Application Status: ", app.getStatus())   # print application status
                print("-----------------------------")  # print separator

# Class for the User Interface
# This class will be used to display the UI Menus and deal with inputs
# Methods include menuLogin, menuMainCustomer, menuMainEmployee, menuMainManager, menuInventoryCustomer, menuInventoryStaff, menuInquiriesCustomer, menuInquiriesStaff, 
# menuCustomerInfoCustomer, menuCustomerInfoStaff, menuEmployeeInfoStaff, menuApplicationsCustomer, menuApplicationsStaff, menuFinancialsManager, menuSalesStaff, 
# menuReceiptsCustomer, customerMenuLoop, employeeMenuLoop
# Contributors: Seth Tourish
# Date: 12/1/2024
class UI:
    # Menu for Login
    # Contributors: Seth Tourish
    # Date: 12/1/2024
    def menuLogin(self):    # function for login menu
        print("-----------------------------")  # print separator
        print("Welcome to the Car Dealership System")    # print welcome message
        print("1. Create Login") # print create login option
        print("2. Login")    # print login option
        print("0. Exit") # print exit option
        inputChoice = input("Enter Choice: ")   # get user input
        print("-----------------------------")
        return inputChoice  # return user input
    
    # Main Menu for Customer
    # Contributors: Seth Tourish
    # Date: 12/1/2024
    def menuMainCustomer(self): # function for main menu for customer
        print("-----------------------------")  # print separator
        print("Main Menu")  # print main menu
        print("1. Inventory")   # print inventory option
        print("2. Inquiries")   # print inquiries option
        print("3. Customer Information")    # print customer information option
        print("4. Applications")    # print applications option
        print("5. Receipts")    # print receipts option
        print("0. Logout")  # print logout option
        inputChoice = input("Enter Choice: ")   # get user input
        print("-----------------------------")  # print separator
        return inputChoice  # return user input

    # Main Menu for Employee
    # Contributors: Seth Tourish
    # Date: 12/1/2024
    def menuMainEmployee(self): # function for main menu for employee
        print("-----------------------------")  # print separator
        print("Main Menu")  # print main menu
        print("1. Inventory")   # print inventory option
        print("2. Inquiries")   # print inquiries option
        print("3. Customer Information")    # print customer information option
        print("4. Employee Information")    # print employee information option
        print("5. Applications")    # print applications option
        print("6. Sales")   # print sales option
        print("7. Finalize Purchase")   # print finalize purchase option
        print("0. Logout")  # print logout option
        inputChoice = input("Enter Choice: ")   # get user input
        print("-----------------------------")  # print separator
        return inputChoice  # return user input

    # Main Menu for Manager
    # Contributors: Seth Tourish
    # Date: 12/1/2024
    def menuMainManager(self):  # function for main menu for manager
        print("-----------------------------")  # print separator
        print("Main Menu")  # print main menu
        print("1. Inventory")   # print inventory option
        print("2. Inquiries")   # print inquiries option
        print("3. Customer Information")    # print customer information option
        print("4. Employee Information")    # print employee information option
        print("5. Applications")    # print applications option
        print("6. Sales")   # print sales option
        print("7. Financials")  # print financials option
        print("0. Logout")  # print logout option
        inputChoice = input("Enter Choice: ")   # get user input
        print("-----------------------------")  # print separator
        return inputChoice  # return user input

    # Menu for Inventory for Customer
    # Contributors: Seth Tourish
    # Date: 12/1/2024
    def menuInventoryCustomer(self):    # function for inventory menu for customer
        print("-----------------------------")  # print separator
        print("Inventory")  # print inventory
        print("1. View Inventory")  # print view inventory option
        print("0. Back")    # print back option
        inputChoice = input("Enter Choice: ")   # get user input
        print("-----------------------------")  # print separator
        return inputChoice  # return user input
    
    # Menu for Inventory for Staff
    # Contributors: Seth Tourish
    # Date: 12/1/2024
    def menuInventoryStaff(self):   # function for inventory menu for staff
        print("-----------------------------")  # print separator
        print("Inventory")  # print inventory
        print("1. View Inventory")  # print view inventory option
        print("2. Add Inventory")   # print add inventory option
        print("3. Remove Inventory")    # print remove inventory option
        print("4. Update Inventory")    # print update inventory option
        print("0. Back")    # print back option
        inputChoice = input("Enter Choice: ")   # get user input
        print("-----------------------------")  # print separator
        return inputChoice  # return user input
    
    # Menu for Inquiries for Customer
    # Contributors: Seth Tourish
    # Date: 12/1/2024
    def menuInquiriesCustomer(self):    # function for inquiries menu for customer
        print("-----------------------------")  # print separator
        print("Inquiries")  # print inquiries
        print("1. Make Inquiry")    # print make inquiry option
        print("0. Back")    # print back option
        inputChoice = input("Enter Choice: ")   # get user input
        print("-----------------------------")  # print separator
        return inputChoice  # return user input
    
    # Menu for Inquiries for Staff
    # Contributors: Seth Tourish
    # Date: 12/1/2024
    def menuInquiriesStaff(self):   # function for inquiries menu for staff
        print("-----------------------------")  # print separator
        print("Inquiries")  # print inquiries
        print("1. View Inquiries")  # print view inquiries option
        print("0. Back")    # print back option
        inputChoice = input("Enter Choice: ")   # get user input
        print("-----------------------------")  # print separator
        return inputChoice  # return user input

    # Menu for Customer Information for Customer
    # Contributors: Seth Tourish
    # Date: 12/1/2024
    def menuCustomerInfoCustomer(self): # function for customer information menu for customer
        print("-----------------------------")  # print separator
        print("Customer Information")   # print customer information
        print("1. Add Customer Information")    # print add customer information option
        print("2. Update Customer Information") # print update customer information option
        print("0. Back")    # print back option
        inputChoice = input("Enter Choice: ")   # get user input
        print("-----------------------------")  # print separator
        return inputChoice  # return user input
    
    # Menu for Customer Information for Staff
    # Contributors: Seth Tourish
    # Date: 12/1/2024
    def menuCustomerInfoStaff(self):    # function for customer information menu for staff
        print("-----------------------------")  # print separator
        print("Customer Information")   # print customer information
        print("1. Add Customer Information")    # print add customer information option
        print("2. Update Customer Information") # print update customer information option
        print("3. Delete Customer Information") # print delete customer information option
        print("0. Back")    # print back option
        inputChoice = input("Enter Choice: ")   # get user input    
        print("-----------------------------")  # print separator
        return inputChoice  # return user input

    # Menu for Employee Information for Staff
    # Contributors: Seth Tourish
    # Date: 12/1/2024
    def menuEmployeeInfoStaff(self):    # function for employee information menu for staff
        print("-----------------------------")  # print separator
        print("Employee Information")   # print employee information
        print("1. Add Employee Information")    # print add employee information option
        print("2. Update Employee Information") # print update employee information option
        print("3. Delete Employee Information") # print delete employee information option
        print("0. Back")    # print back option
        inputChoice = input("Enter Choice: ")       # get user input    
        print("-----------------------------")  # print separator
        return inputChoice  # return user input

    # Menu for Applications for Customer
    # Contributors: Seth Tourish
    # Date: 12/1/2024
    def menuApplicationsCustomer(self): # function for applications menu for customer
        print("-----------------------------")  # print separator
        print("Applications")   # print applications
        print("1. Add Application")  # print add application option
        print("2. Update Application")  # print update application option
        print("3. View Application Status")   # print view application status option
        print("0. Back")    # print back option
        inputChoice = input("Enter Choice: ")   # get user input
        print("-----------------------------")  # print separator
        return inputChoice  # return user input

    # Menu for Applications for Staff
    # Contributors: Seth Tourish
    # Date: 12/1/2024
    def menuApplicationsStaff(self):    # function for applications menu for staff
        print("-----------------------------")  # print separator
        print("Applications")   # print applications
        print("1. Create Application")  # print create application option
        print("2. Delete Application")  # print delete application option
        print("3. Approve Application")     # print approve application option
        print("4. Deny Application")    # print deny application option
        print("0. Back")    # print back option
        inputChoice = input("Enter Choice: ")   # get user input
        print("-----------------------------")  # print separator
        return inputChoice  # return user input

    # Menu for Financials for Manager
    # Contributors: Seth Tourish
    # Date: 12/1/2024
    def menuFinancialsManager(self):    # function for financials menu for manager
        print("-----------------------------")  # print separator
        print("Financials")   # print financials
        print("1. Add Financial Information")   # print add financial information option
        print("2. Delete Financial Information")    # print delete financial information option
        print("3. Generate Financial Report")   # print generate financial report option
        print("0. Back")    # print back option
        inputChoice = input("Enter Choice: ")   # get user input
        print("-----------------------------")  # print separator
        return inputChoice      # return user input

    # Menu for Staff - Sales Menu
    # Contributors: Seth Tourish
    # Date: 12/1/2024
    def menuSalesStaff(self):   # function for sales menu for staff
        print("-----------------------------")  # print separator
        print("Sales")  # print sales
        print("1. Add Sale")    # print add sale option
        print("2. Delete Sale") # print delete sale option
        print("3. Update Sale") # print update sale option
        print("4. Add Lease")   # print add lease option
        print("5. Update Lease")    # print update lease option
        print("6. Delete Lease")    # print delete lease option
        print("7. Add Receipt") # print add receipt option
        print("8. Update Receipt")  # print update receipt option
        print("9. Delete Receipt")  # print delete receipt option
        print("0. Back")    # print back option
        inputChoice = input("Enter Choice: ")   # get user input
        print("-----------------------------")  # print separator
        return inputChoice  # return user input

    # Menu for Receipts for Customer
    # Contributors: Seth Tourish
    # Date: 12/1/2024
    def menuReceiptsCustomer(self):   # function for receipts menu for customer
        print("-----------------------------")  # print separator
        print("Receipts")   # print receipts
        print("1. View Receipts")   # print view receipts option
        print("0. Back")    # print back option
        inputChoice = input("Enter Choice: ")   # get user input
        print("-----------------------------")  # print separator
        return inputChoice  # return user input 

    # Customer Menu Loop. a Method for the UI class that will display 
    # the customer UI Menus and deal with inputs
    # Parameters are the manageEmployeesController, manageFinancialsController, manageInventoryController, manageCustomersController, 
    # manageInquiryController, viewInventoryOBJ, generateFinancialReportOBJ, approveDenyApplicationsOBJ, calcEmployeeCommissionOBJ, 
    # viewApplicationResultsOBJ, loggedIn, userType
    # Contributors: Seth Tourish
    # Date: 12/1/2024
    def customerMenuLoop(self, manageEmployeesController, manageFinancialsController, manageInventoryController, manageCustomersController, manageInquiryController, viewInventoryOBJ, generateFinancialReportOBJ, approveDenyApplicationsOBJ, calcEmployeeCommissionOBJ, viewApplicationResultsOBJ, finalizePurchaseController, loggedIn, userType):
        while (loggedIn and userType == "Customer"):    # loop while user is logged in and is a customer
            inputChoice = self.menuMainCustomer()   # get user input
            if inputChoice == "1":  # if user chooses inventory
                inputChoiceTwo = self.menuInventoryCustomer()   # get user input
                if inputChoiceTwo == "1":   # if user chooses view inventory
                    viewInventoryOBJ.viewInventory(manageInventoryController.inventoryData)   # call viewInventory function
                elif inputChoiceTwo == "0": # if user chooses back
                    continue    # continue loop
            elif inputChoice == "2":    # if user chooses inquiries
                inputChoiceTwo = self.menuInquiriesCustomer()   # get user input
                if inputChoiceTwo == "1":   # if user chooses make inquiry
                    manageInquiryController.addInquiry()    # call addInquiry function
                elif inputChoiceTwo == "0": # if user chooses back
                    continue    # continue loop
            elif inputChoice == "3":    # if user chooses customer information
                inputChoiceTwo = self.menuCustomerInfoCustomer()    # get user input
                if inputChoiceTwo == "1":   # if user chooses add customer information
                    manageCustomersController.addCustomer()  # call addCustomer function
                elif inputChoiceTwo == "2": # if user chooses update customer information
                    manageCustomersController.updateCustomer()  # call updateCustomer function
                elif inputChoiceTwo == "0": # if user chooses back
                    continue    # continue loop
            elif inputChoice == "4":    # if user chooses applications
                inputChoiceTwo = self.menuApplicationsCustomer()    # get user input
                if inputChoiceTwo == "1":   # if user chooses add application
                    manageFinancialsController.addApplication()   # call addApplication function
                elif inputChoiceTwo == "2": # if user chooses update application
                    manageFinancialsController.updateApplication()  # call updateApplication function
                elif inputChoiceTwo == "3": # if user chooses view application status
                    viewApplicationResultsOBJ.viewResult(manageFinancialsController)    # call viewResult function
                elif inputChoiceTwo == "0": # if user chooses back
                    continue    # continue loop
            elif inputChoice == "5":    # if user chooses receipts
                inputChoiceTwo = self.menuReceiptsCustomer()    # get user input
                if inputChoiceTwo == "1":   # if user chooses view receipts
                    receiptID = input("Enter Customer ID: ")    # get customer ID from user
                    for rec in manageFinancialsController.receiptData:  # iterate through receipt list
                        if rec.customerID == receiptID: # if customer ID matches
                            print("Sales ID: " + rec.salesID)   # print sales ID
                            print("Customer ID: " + rec.customerID) # print customer ID
                            print("Price: " + rec.price)    # print price
                            print("Lease ID: " + rec.leaseID)   # print lease ID
                elif inputChoiceTwo == "0": # if user chooses back
                    continue    # continue loop
            elif inputChoice == "0":    # if user chooses logout 
                break   # break loop
            else:   # if user enters invalid choice
                print("Invalid Choice") # print invalid choice

    # Employee Menu Loop. a Method for the UI class that will display
    # the employee UI Menus and deal with inputs
    # Parameters are the manageEmployeesController, manageFinancialsController, manageInventoryController, manageCustomersController,
    # manageInquiryController, viewInventoryOBJ, generateFinancialReportOBJ, approveDenyApplicationsOBJ, calcEmployeeCommissionOBJ,
    # viewApplicationResultsOBJ, loggedIn, userType
    # Contributors: Seth Tourish
    # Date: 12/1/2024
    def employeeMenuLoop(self, manageEmployeesController, manageFinancialsController, manageInventoryController, manageCustomersController, manageInquiryController, viewInventoryOBJ, generateFinancialReportOBJ, approveDenyApplicationsOBJ, calcEmployeeCommissionOBJ, viewApplicationResultsOBJ, finalizePurchaseController, loggedIn, userType):
        while (loggedIn and userType == "Employee"):    # loop while user is logged in and is an employee
            inputChoice = self.menuMainEmployee()   # get user input
            if inputChoice == "1":  # if user chooses inventory
                inputChoiceTwo = self.menuInventoryStaff()  # get user input
                if inputChoiceTwo == "1":   # if user chooses view inventory
                    viewInventoryOBJ.viewInventory(manageInventoryController.inventoryData)  # call viewInventory function
                elif inputChoiceTwo == "2": # if user chooses add inventory
                    manageInventoryController.addInventory()    # call addInventory function
                elif inputChoiceTwo == "3": # if user chooses remove inventory
                    manageInventoryController.deleteInventory() # call deleteInventory function
                elif inputChoiceTwo == "4": # if user chooses update inventory
                    manageInventoryController.updateInventory() # call updateInventory function
                elif inputChoiceTwo == "0": # if user chooses back
                    continue    # continue loop
            elif inputChoice == "2":    # if user chooses inquiries
                inputChoiceTwo = self.menuInquiriesStaff()  # get user input
                if inputChoiceTwo == "1":   # if user chooses view inquiries
                    for inquiry in manageInquiryController.inquiryData:   # iterate through inquiry list
                        print("Customer ID: " + inquiry.customerID)   # print customer ID
                        print("Vehicle ID: " + inquiry.vehicleID)   # print vehicle ID
                        print("###############")    # print separator
                elif inputChoiceTwo == "0": # if user chooses back
                    continue    # continue loop
            elif inputChoice == "3":    # if user chooses customer information
                inputChoiceTwo = self.menuCustomerInfoStaff()   # get user input
                if inputChoiceTwo == "1":   # if user chooses add customer information
                    manageCustomersController.addCustomer() # call addCustomer function
                elif inputChoiceTwo == "2": # if user chooses update customer information
                    manageCustomersController.updateCustomer()  # call updateCustomer function
                elif inputChoiceTwo == "3": # if user chooses delete customer information
                    manageCustomersController.deleteCustomer()      # call deleteCustomer function
                elif inputChoiceTwo == "0": # if user chooses back
                    continue    # continue loop
            elif inputChoice == "4":    # if user chooses employee information
                inputChoiceTwo = self.menuEmployeeInfoStaff()   # get user input
                if inputChoiceTwo == "1":   # if user chooses add employee information
                    manageEmployeesController.addEmployee() # call addEmployee function
                elif inputChoiceTwo == "2": # if user chooses update employee information
                    manageEmployeesController.updateEmployee()  # call updateEmployee function
                elif inputChoiceTwo == "3": # if user chooses delete employee information
                    manageEmployeesController.deleteEmployee()  # call deleteEmployee function
                elif inputChoiceTwo == "0": # if user chooses back
                    continue    # continue loop
            elif inputChoice == "5":    # if user chooses applications
                inputChoiceTwo = self.menuApplicationsStaff()   # get user input
                if inputChoiceTwo == "1":   # if user chooses create application
                    manageFinancialsController.addApplication() # call addApplication function
                elif inputChoiceTwo == "2": # if user chooses delete application
                    manageFinancialsController.deleteApplication()  # call deleteApplication function
                elif inputChoiceTwo == "3": # if user chooses approve application
                    appID = input("Enter Application ID to Approve: ")  # get application ID from user
                    approveDenyApplicationsOBJ.approveApplication(appID, manageFinancialsController.applicationData)    # call approveApplication function
                elif inputChoiceTwo == "4": # if user chooses deny application
                    appID = input("Enter Application ID to Deny: ") # get application ID from user
                    approveDenyApplicationsOBJ.denyApplication(appID, manageFinancialsController.applicationData)   # call denyApplication function
                elif inputChoiceTwo == "0": # if user chooses back  
                    continue    # continue loop
            elif inputChoice == "6":    # if user chooses sales
                inputChoiceTwo = self.menuSalesStaff()  # get user input
                if inputChoiceTwo == "1":   # if user chooses add sale
                    manageFinancialsController.addSales()   # call addSales function
                elif inputChoiceTwo == "2": # if user chooses delete sale
                    manageFinancialsController.deleteSales()    # call deleteSales function
                elif inputChoiceTwo == "3": # if user chooses update sale
                    manageFinancialsController.updateSales()    # call updateSales function
                elif inputChoiceTwo == "4": # if user chooses add lease
                    manageFinancialsController.addLease()   # call addLease function
                elif inputChoiceTwo == "5": # if user chooses update lease
                    manageFinancialsController.updateLease()    # call updateLease function
                elif inputChoiceTwo == "6": # if user chooses delete lease
                    manageFinancialsController.deleteLease()    # call deleteLease function
                elif inputChoiceTwo == "7": # if user chooses add receipt
                    manageFinancialsController.addReceipt() # call addReceipt function
                elif inputChoiceTwo == "8": # if user chooses update receipt
                    manageFinancialsController.updateReceipt()  # call updateReceipt function
                elif inputChoiceTwo == "9": # if user chooses delete receipt
                    manageFinancialsController.deleteReceipt()  # call deleteReceipt function
                elif inputChoiceTwo == "0": # if user chooses back
                    continue    # continue loop
            elif inputChoice == "7":    # if user chooses financials
                finalizePurchaseController.FinalizePurchase(manageFinancialsController, calcEmployeeCommissionOBJ)  # call FinalizePurchase function
            elif inputChoice == "0":    # if user chooses logout
                break   # break loop
            else:   # if user enters invalid choice
                print("Invalid Choice") # print invalid choice

    # Manager Menu Loop. a Method for the UI class that will display
    # the manager UI Menus and deal with inputs
    # Parameters are the manageEmployeesController, manageFinancialsController, manageInventoryController, manageCustomersController,
    # manageInquiryController, viewInventoryOBJ, generateFinancialReportOBJ, approveDenyApplicationsOBJ, calcEmployeeCommissionOBJ,
    # viewApplicationResultsOBJ, loggedIn, userType
    # Contributors: Seth Tourish
    # Date: 12/1/2024
    def managerMenuLoop(self, manageEmployeesController, manageFinancialsController, manageInventoryController, manageCustomersController, manageInquiryController, viewInventoryOBJ, generateFinancialReportOBJ, approveDenyApplicationsOBJ, calcEmployeeCommissionOBJ, viewApplicationResultsOBJ, finalizePurchaseController, loggedIn, userType):
        while (loggedIn and userType == "Manager"):   # loop while user is logged in and is a manager
            inputChoice = self.menuMainManager()    # get user input
            if inputChoice == "1":  # if user chooses inventory
                inputChoiceTwo = self.menuInventoryStaff()  # get user input
                if inputChoiceTwo == "1":   # if user chooses view inventory
                    viewInventoryOBJ.viewInventory(manageInventoryController.inventoryData) # call viewInventory function
                elif inputChoiceTwo == "2": # if user chooses add inventory
                    manageInventoryController.addInventory()    # call addInventory function
                elif inputChoiceTwo == "3": # if user chooses remove inventory
                    manageInventoryController.deleteInventory() # call deleteInventory function
                elif inputChoiceTwo == "4": # if user chooses update inventory
                    manageInventoryController.updateInventory() # call updateInventory function
                elif inputChoiceTwo == "0": # if user chooses back
                    continue    # continue loop
            elif inputChoice == "2":    # if user chooses inquiries
                inputChoiceTwo = self.menuInquiriesStaff()  # get user input
                if inputChoiceTwo == "1":   # if user chooses view inquiries
                    for inquiry in manageInquiryController.inquiryData:  # iterate through inquiry list
                        print("Customer ID: " + inquiry.customerID)  # print customer ID
                        print("Vehicle ID: " + inquiry.vehicleID)   # print vehicle ID
                        print("###############")    # print separator
                elif inputChoiceTwo == "0": # if user chooses back
                    continue    # continue loop
            elif inputChoice == "3":    # if user chooses customer information
                inputChoiceTwo = self.menuCustomerInfoStaff()   # get user input
                if inputChoiceTwo == "1":   # if user chooses add customer information
                    manageCustomersController.addCustomer() # call addCustomer function
                elif inputChoiceTwo == "2": # if user chooses update customer information
                    manageCustomersController.updateCustomer()  # call updateCustomer function
                elif inputChoiceTwo == "3":     # if user chooses delete customer information
                    manageCustomersController.deleteCustomer()  # call deleteCustomer function
                elif inputChoiceTwo == "0": # if user chooses back
                    continue    # continue loop
            elif inputChoice == "4":    # if user chooses employee information
                inputChoiceTwo = self.menuEmployeeInfoStaff()   # get user input
                if inputChoiceTwo == "1":   # if user chooses add employee information
                    manageEmployeesController.addEmployee() # call addEmployee function
                elif inputChoiceTwo == "2": # if user chooses update employee information
                    manageEmployeesController.updateEmployee()  # call updateEmployee function
                elif inputChoiceTwo == "3": # if user chooses delete employee information
                    manageEmployeesController.deleteEmployee()  # call deleteEmployee function
                elif inputChoiceTwo == "0": # if user chooses back
                    continue    # continue loop
            elif inputChoice == "5":    # if user chooses applications
                inputChoiceTwo = self.menuApplicationsStaff()   # get user input
                if inputChoiceTwo == "1":   # if user chooses create application
                    manageFinancialsController.addApplication() # call addApplication function
                elif inputChoiceTwo == "2": # if user chooses delete application
                    manageFinancialsController.deleteApplication()  # call deleteApplication function
                elif inputChoiceTwo == "3": # if user chooses approve application
                    appID = input("Enter Application ID to Approve: ")  # get application ID from user
                    approveDenyApplicationsOBJ.approveApplication(appID, manageFinancialsController)    # call approveApplication function
                elif inputChoiceTwo == "4": # if user chooses deny application
                    appID = input("Enter Application ID to Deny: ") # get application ID from user
                    approveDenyApplicationsOBJ.denyApplication(appID, manageFinancialsController)   # call denyApplication function
                elif inputChoiceTwo == "0": # if user chooses back
                    continue    # continue loop
            elif inputChoice == "6":    # if user chooses sales
                inputChoiceTwo = self.menuSalesStaff()  # get user input
                if inputChoiceTwo == "1":   # if user chooses add sale
                    manageFinancialsController.addSales()   # call addSales function
                elif inputChoiceTwo == "2": # if user chooses delete sale
                    manageFinancialsController.deleteSales()    # call deleteSales function
                elif inputChoiceTwo == "3": # if user chooses update sale
                    manageFinancialsController.updateSales()    # call updateSales function
                elif inputChoiceTwo == "4": # if user chooses add lease
                    manageFinancialsController.addLease()   # call addLease function
                elif inputChoiceTwo == "5": # if user chooses update lease
                    manageFinancialsController.updateLease()    # call updateLease function
                elif inputChoiceTwo == "6": # if user chooses delete lease
                    manageFinancialsController.deleteLease()    # call deleteLease function
                elif inputChoiceTwo == "7": # if user chooses add receipt
                    manageFinancialsController.addReceipt() # call addReceipt function
                elif inputChoiceTwo == "8": # if user chooses update receipt
                    manageFinancialsController.updateReceipt()  # call updateReceipt function
                elif inputChoiceTwo == "9": # if user chooses delete receipt
                    manageFinancialsController.deleteReceipt()  # call deleteReceipt function
                elif inputChoiceTwo == "0": # if user chooses back
                    continue    # continue loop
            elif inputChoice == "7":    # if user chooses financials
                inputChoiceTwo = self.menuFinancialsManager()   # get user input
                if inputChoiceTwo == "1":   # if user chooses add financial information
                    manageFinancialsController.addFinancial()   # call addFinancial function
                elif inputChoiceTwo == "2": # if user chooses delete financial information
                    manageFinancialsController.deleteFinancial()    # call deleteFinancial function
                elif inputChoiceTwo == "3": # if user chooses generate financial report
                    generateFinancialReportOBJ.generateReport(manageFinancialsController.getFinancial())    # call generateReport function
                elif inputChoiceTwo == "0": # if user chooses back
                    continue    # continue loop
            elif inputChoice == "0":    # if user chooses logout
                break   # break loop
            else:   # if user enters invalid choice
                print("Invalid Choice") # print invalid choice
