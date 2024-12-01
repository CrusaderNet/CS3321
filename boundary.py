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
         print("Budget: ", financialObject.getBudget()) # print budget
         print("Revenue: ", financialObject.getRevenue()) # print revenue
         print("Expenses: ", financialObject.getExpenses()) # print expenses
         print("Profit: ", financialObject.getRevenue() - financialObject.getExpenses()) # print profit
         print("-----------------------------") # print separator

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
    def calcEmployeeComm(self, saleObject : entity.Sales) -> float:
        return saleObject.getSalesPrice() * 0.10 # return 10% of sales price

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
#Contributors: Seth Tourish
#Date: 12/1/2024
class UI:
    def menuLogin(self):
        print("-----------------------------")  # print separator
        print("Welcome to the Car Dealership System")    # print welcome message
        print("1. Create Login") # print create login option
        print("2. Login")    # print login option
        print("0. Exit") # print exit option
        inputChoice = input("Enter Choice: ")   # get user input
        print("-----------------------------")
        return inputChoice  # return user input
    
    def menuMainCustomer(self):
        print("-----------------------------")
        print("Main Menu")
        print("1. Inventory")
        print("2. Inquiries")
        print("3. Customer Information")
        print("4. Applications")
        print("5. Receipts")
        print("0. Logout")
        inputChoice = input("Enter Choice: ")
        print("-----------------------------")
        return inputChoice

    def menuMainEmployee(self):
        print("-----------------------------")
        print("Main Menu")
        print("1. Inventory")
        print("2. Inquiries")
        print("3. Customer Information")
        print("4. Employee Information")
        print("5. Applications")
        print("6. Sales")
        print("0. Logout")
        inputChoice = input("Enter Choice: ")
        print("-----------------------------")
        return inputChoice

    def menuMainManager(self):
        print("-----------------------------")
        print("Main Menu")
        print("1. Inventory")
        print("2. Inquiries")
        print("3. Customer Information")
        print("4. Employee Information")
        print("5. Applications")
        print("6. Sales")
        print("7. Financials")
        print("0. Logout")
        inputChoice = input("Enter Choice: ")
        print("-----------------------------")
        return inputChoice

    def menuInventoryCustomer(self):
        print("-----------------------------")
        print("Inventory")
        print("1. View Inventory")
        print("0. Back")
        inputChoice = input("Enter Choice: ")
        print("-----------------------------")
        return inputChoice
    
    def menuInventoryStaff(self):
        print("-----------------------------")
        print("Inventory")
        print("1. View Inventory")
        print("2. Add Inventory")
        print("3. Remove Inventory")
        print("4. Update Inventory")
        print("0. Back")
        inputChoice = input("Enter Choice: ")
        print("-----------------------------")
        return inputChoice
    
    def menuInquiriesCustomer(self):
        print("-----------------------------")
        print("Inquiries")
        print("1. Make Inquiry")
        print("0. Back")
        inputChoice = input("Enter Choice: ")
        print("-----------------------------")
        return inputChoice
    
    def menuInquiriesStaff(self):
        print("-----------------------------")
        print("Inquiries")
        print("1. View Inquiries")
        print("0. Back")
        inputChoice = input("Enter Choice: ")
        print("-----------------------------")
        return inputChoice

    def menuCustomerInfoCustomer(self):
        print("-----------------------------")
        print("Customer Information")
        print("1. Add Customer Information")
        print("2. Update Customer Information")
        print("0. Back")
        inputChoice = input("Enter Choice: ")
        print("-----------------------------")
        return inputChoice
    
    def menuCustomerInfoStaff(self):
        print("-----------------------------")
        print("Customer Information")
        print("1. Add Customer Information")
        print("2. Update Customer Information")
        print("3. Delete Customer Information")
        print("0. Back")
        inputChoice = input("Enter Choice: ")
        print("-----------------------------")
        return inputChoice

    def menuEmployeeInfoStaff(self):
        print("-----------------------------")
        print("Employee Information")
        print("1. Add Employee Information")
        print("2. Update Employee Information")
        print("3. Delete Employee Information")
        print("0. Back")
        inputChoice = input("Enter Choice: ")
        print("-----------------------------")
        return inputChoice

    def menuApplicationsCustomer(self):
        print("-----------------------------")
        print("Applications")
        print("1. Add Application")
        print("2. Update Application")
        print("0. Back")
        inputChoice = input("Enter Choice: ")
        print("-----------------------------")
        return inputChoice

    def menuApplicationsStaff(self):
        print("-----------------------------")
        print("Applications")
        print("1. Create Application")
        print("2. Delete Application")
        print("3. Approve Application")
        print("4. Deny Application")
        print("0. Back")
        inputChoice = input("Enter Choice: ")
        print("-----------------------------")
        return inputChoice

    def menuFinancialsManager(self):
        print("-----------------------------")
        print("Financials")
        print("1. Add Financial Information")
        print("2. Delete Financial Information")
        print("3. Generate Financial Report")
        print("0. Back")
        inputChoice = input("Enter Choice: ")
        print("-----------------------------")
        return inputChoice

    def menuSalesStaff(self):
        print("-----------------------------")
        print("Sales")
        print("1. Add Sale")
        print("2. Delete Sale")
        print("3. Update Sale")
        print("4. Add Lease")
        print("5. Update Lease")
        print("6. Delete Lease")
        print("7. Add Receipt")
        print("8. Update Receipt")
        print("9. Delete Receipt")
        print("0. Back")
        inputChoice = input("Enter Choice: ")
        print("-----------------------------")
        return inputChoice

    def menuReceiptsCustomer(self):
        print("-----------------------------")
        print("Receipts")
        print("1. View Receipts")
        print("0. Back")
        inputChoice = input("Enter Choice: ")
        print("-----------------------------")
        return inputChoice

    def customerMenuLoop(self, manageEmployeesController, manageFinancialsController, manageInventoryController, manageCustomersController, manageInquiryController, viewInventoryOBJ, generateFinancialReportOBJ, approveDenyApplicationsOBJ, calcEmployeeCommissionOBJ, viewApplicationResultsOBJ, loggedIn, userType):
        while (loggedIn and userType == "Customer"):
            inputChoice = self.menuMainCustomer()
            if inputChoice == "1":
                inputChoiceTwo = self.menuInventoryCustomer()
                if inputChoiceTwo == "1":
                    viewInventoryOBJ.viewInventory(manageInventoryController.inventoryData)
                elif inputChoiceTwo == "0":
                    continue
            elif inputChoice == "2":
                inputChoiceTwo = self.menuInquiriesCustomer()
                if inputChoiceTwo == "1":
                    manageInquiryController.addInquiry()
                elif inputChoiceTwo == "0":
                    continue
            elif inputChoice == "3":
                inputChoiceTwo = self.menuCustomerInfoCustomer()
                if inputChoiceTwo == "1":
                    manageCustomersController.addCustomer()
                elif inputChoiceTwo == "2":
                    manageCustomersController.updateCustomer()
                elif inputChoiceTwo == "0":
                    continue
            elif inputChoice == "4":
                inputChoiceTwo = self.menuApplicationsCustomer()
                if inputChoiceTwo == "1":
                    manageFinancialsController.addApplication()
                elif inputChoiceTwo == "2":
                    manageFinancialsController.updateApplication()
                elif inputChoiceTwo == "0":
                    continue
            elif inputChoice == "5":
                inputChoiceTwo = self.menuReceiptsCustomer()
                if inputChoiceTwo == "1":
                    receiptID = input("Enter Customer ID: ")
                    for rec in manageFinancialsController.receiptData:
                        if rec.customerID == receiptID:
                            print("Sales ID: " + rec.salesID)
                            print("Customer ID: " + rec.customerID)
                            print("Price: " + rec.price)
                            print("Lease ID: " + rec.leaseID)
                elif inputChoiceTwo == "0":
                    continue
            elif inputChoice == "0":
                break
            else:
                print("Invalid Choice")

    def employeeMenuLoop(self, manageEmployeesController, manageFinancialsController, manageInventoryController, manageCustomersController, manageInquiryController, viewInventoryOBJ, generateFinancialReportOBJ, approveDenyApplicationsOBJ, calcEmployeeCommissionOBJ, viewApplicationResultsOBJ, loggedIn, userType):
        while (loggedIn and userType == "Employee"):
            inputChoice = self.menuMainEmployee()
            if inputChoice == "1":
                inputChoiceTwo = self.menuInventoryStaff()
                if inputChoiceTwo == "1":
                    viewInventoryOBJ.viewInventory(manageInventoryController.inventoryData)
                elif inputChoiceTwo == "2":
                    manageInventoryController.addInventory()
                elif inputChoiceTwo == "3":
                    manageInventoryController.removeInventory()
                elif inputChoiceTwo == "4":
                    manageInventoryController.updateInventory()
                elif inputChoiceTwo == "0":
                    continue
            elif inputChoice == "2":
                inputChoiceTwo = self.menuInquiriesStaff()
                if inputChoiceTwo == "1":
                    for inquiry in manageInquiryController.inquiryData:
                        print("Customer ID: " + inquiry.customerID)
                        print("Vehicle ID: " + inquiry.vehicleID)
                        print("###############")
                elif inputChoiceTwo == "0":
                    continue
            elif inputChoice == "3":
                inputChoiceTwo = self.menuCustomerInfoStaff()
                if inputChoiceTwo == "1":
                    manageCustomersController.addCustomer()
                elif inputChoiceTwo == "2":
                    manageCustomersController.updateCustomer()
                elif inputChoiceTwo == "3":
                    manageCustomersController.deleteCustomer()
                elif inputChoiceTwo == "0":
                    continue
            elif inputChoice == "4":
                inputChoiceTwo = self.menuEmployeeInfoStaff()
                if inputChoiceTwo == "1":
                    manageEmployeesController.addEmployee()
                elif inputChoiceTwo == "2":
                    manageEmployeesController.updateEmployee()
                elif inputChoiceTwo == "3":
                    manageEmployeesController.deleteEmployee()
                elif inputChoiceTwo == "0":
                    continue
            elif inputChoice == "5":
                inputChoiceTwo = self.menuApplicationsStaff()
                if inputChoiceTwo == "1":
                    manageFinancialsController.addApplication()
                elif inputChoiceTwo == "2":
                    manageFinancialsController.deleteApplication()
                elif inputChoiceTwo == "3":
                    appID = input("Enter Application ID to Approve: ")
                    approveDenyApplicationsOBJ.approveApplication(appID, manageFinancialsController.applicationData)
                elif inputChoiceTwo == "4":
                    appID = input("Enter Application ID to Deny: ")
                    approveDenyApplicationsOBJ.denyApplication(appID, manageFinancialsController.applicationData)
                elif inputChoiceTwo == "0":
                    continue
            elif inputChoice == "6":
                inputChoiceTwo = self.menuSalesStaff()
                if inputChoiceTwo == "1":
                    manageFinancialsController.addSale()
                elif inputChoiceTwo == "2":
                    manageFinancialsController.deleteSale()
                elif inputChoiceTwo == "3":
                    manageFinancialsController.updateSale()
                elif inputChoiceTwo == "4":
                    manageFinancialsController.addLease()
                elif inputChoiceTwo == "5":
                    manageFinancialsController.updateLease()
                elif inputChoiceTwo == "6":
                    manageFinancialsController.deleteLease()
                elif inputChoiceTwo == "7":
                    manageFinancialsController.addReceipt()
                elif inputChoiceTwo == "8":
                    manageFinancialsController.updateReceipt()
                elif inputChoiceTwo == "9":
                    manageFinancialsController.deleteReceipt()
                elif inputChoiceTwo == "0":
                    continue
            elif inputChoice == "0":
                break
            else:
                print("Invalid Choice")
