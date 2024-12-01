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

