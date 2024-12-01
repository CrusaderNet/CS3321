import entity
import control

# Class to view inventory objects
# This class will be used to view the inventory objects
# Contributors: Seth Tourish
# Date: 12/1/2024
class ViewInventory:
    def viewInventory(self, inventoryArray):
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
    def calcEmployeeComm(self, saleObject : entity.Sale) -> float:
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
        print("Please enter your username and password")  # print prompt for username and password
    
    def menuMainCustomer(self):
        print("-----------------------------")
        print("Main Menu")
        print("1. Inventory")
        print("2. Inquiries")
        print("3. Customer Information")
        print("4. Applications")
        print("5. Logout")

    def menuMainEmployee(self):
        print("-----------------------------")
        print("Main Menu")
        print("1. Inventory")
        print("2. Inquiries")
        print("3. Customer Information")
        print("4. Employee Information")
        print("5. Applications")
        print("6. Logout")

    def menuMainManager(self):
        print("-----------------------------")
        print("Main Menu")
        print("1. Inventory")
        print("2. Inquiries")
        print("3. Customer Information")
        print("4. Employee Information")
        print("5. Applications")
        print("6. Financials")
        print("7. Logout")

    def menuInventoryCustomer(self):
        print("-----------------------------")
        print("Inventory")
        print("1. View Inventory")
        print("2. Back")
    
    def menuInventoryStaff(self):
        print("-----------------------------")
        print("Inventory")
        print("1. View Inventory")
        print("2. Add Inventory")
        print("3. Remove Inventory")
        print("4. Update Inventory")
        print("5. Back")
    
    def menuInquiriesCustomer(self):
        print("-----------------------------")
        print("Inquiries")
        print("1. Make Inquiry")
        print("2. Back")
    
    def menuInquiriesStaff(self):
        print("-----------------------------")
        print("Inquiries")
        print("1. View Inquiries")
        print("2. Back")

    def menuCustomerInfoCustomer(self):
        print("-----------------------------")
        print("Customer Information")
        print("1. Add Customer Information")
        print("2. Update Customer Information")
        print("3. Back")
    
    def menuCustomerInfoStaff(self):
        print("-----------------------------")
        print("Customer Information")
        print("1. Add Customer Information")
        print("2. Update Customer Information")
        print("3. Delete Customer Information")
        print("4. Back")

    def menuEmployeeInfoStaff(self):
        print("-----------------------------")
        print("Employee Information")
        print("1. Add Employee Information")
        print("2. Update Employee Information")
        print("3. Delete Employee Information")
        print("4. Back")

    def menuApplicationsCustomer(self):
        print("-----------------------------")
        print("Applications")
        print("1. View Applications")
        print("2. Back")

    def menuApplicationsStaff(self):
        print("-----------------------------")
        print("Applications")
        print("1. Create Application")
        print("2. Delete Application")
        print("3. Approve Application")
        print("4. Deny Application")
        print("5. Back")

    def menuFinancialsManager(self):
        print("-----------------------------")
        print("Financials")
        print("1. Add Financial Information")
        print("2. Delete Financial Information")
        print("3. Generate Financial Report")
        print("4. Back")
