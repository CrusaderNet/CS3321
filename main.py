import entity
import control
import boundary

# Controller Objects
# Contributors: Seth Tourish
# Date: 12/1/2024
manageEmployeesController = control.ManageEmployees()
manageFinancialsController = control.ManageFinancials()
manageInventoryController = control.ManageInventory()
manageCustomersController = control.ManageCustomers()
manageInquiryController = control.ManageInquiry()
userLoginController = control.UserLogin()

#Boundary Objects
# Contributors: Seth Tourish
# Date: 12/1/2024
ui = boundary.UI()
viewInventoryOBJ = boundary.ViewInventory()
generateFinancialReportOBJ = boundary.GenerateFinancialReport()
approveDenyApplicationsOBJ = boundary.ApproveDenyApplications()
calcEmployeeCommissionOBJ = boundary.CalculateEmployeeCommission()
viewApplicationResultsOBJ = boundary.ViewApplicationResults()

# User Login Function
# This function will allow the user to login and Validate the user
# Contributors: Seth Tourish
# Date: 12/1/2024
loggedIn = False    # set loggedIn to False
while True: # loop until user logs in
    inputChoice = ui.menuLogin()    # get user input
    if inputChoice == "1":  # if user chooses to create login
        userLoginController.addLogin()  # call addLogin function
    elif inputChoice == "2":    # if user chooses to login
        print("Login:") # print login message
        username = input("Enter LoginID: ")  # get username from user
        password = input("Enter Password: ")    # get password from user
        loggedIn = userLoginController.login(username, password)    # call login function
        if loggedIn:    # if login is successful
            if (loggedIn and (username[0] == 'E' or username[0] == 'e')):   # if user is employee
                userType = "Employee"   # set userType to Employee
                ui.employeeMenuLoop(manageEmployeesController, manageFinancialsController, manageInventoryController, manageCustomersController, manageInquiryController, viewInventoryOBJ, generateFinancialReportOBJ, approveDenyApplicationsOBJ, calcEmployeeCommissionOBJ, viewApplicationResultsOBJ, loggedIn, userType)
            elif (loggedIn and (username[0] == 'M' or username[0] == 'm')): # if user is manager
                userType = "Manager"    # set userType to Manager
            elif (loggedIn and (username[0] == 'C' or username[0] == 'c')): # if user is customer
                userType = "Customer"   # set userType to Customer
                ui.customerMenuLoop(manageEmployeesController, manageFinancialsController, manageInventoryController, manageCustomersController, manageInquiryController, viewInventoryOBJ, generateFinancialReportOBJ, approveDenyApplicationsOBJ, calcEmployeeCommissionOBJ, viewApplicationResultsOBJ, loggedIn, userType)
        else:   # if login is unsuccessful
            print("Login Failed, Please Retry") # print login failed message
            continue    # continue loop
    elif inputChoice == "0":    # if user chooses to exit
        break   # break loop
    else:   # if user enters invalid choice
        print("Invalid Choice")   # print invalid choice message

# Customer Menus
# This loop will display the customer UI Menus based on the user type
# Contributors: Seth Tourish
# Date: 12/1/2024
#while (loggedIn and inputChoice != "0" and userType == "Customer"):
#    inputChoice = ui.menuMainCustomer()
#    if inputChoice == "1":
#        inputChoiceTwo = ui.menuInventoryCustomer()
#        if inputChoiceTwo == "1":
#            viewInventoryOBJ.viewInventory(manageInventoryController.inventoryData)
#        elif inputChoiceTwo == "0":
#            continue
#    elif inputChoice == "2":
#        inputChoiceTwo = ui.menuInquiriesCustomer()
#        if inputChoiceTwo == "1":
#            manageInquiryController.addInquiry()
#        elif inputChoiceTwo == "0":
#            continue
#    elif inputChoice == "3":
#        inputChoiceTwo = ui.menuCustomerInformation()
#        if inputChoiceTwo == "1":
#            manageCustomersController.addCustomer()
#        elif inputChoiceTwo == "2":
#            manageCustomersController.updateCustomer()
#        elif inputChoiceTwo == "0":
#            continue
#    elif inputChoice == "4":
#        inputChoiceTwo = ui.menuApplicationsCustomer()
#        if inputChoiceTwo == "1":
#            manageFinancialsController.addApplication()
#        elif inputChoiceTwo == "2":
#            manageFinancialsController.updateApplication()
#        elif inputChoiceTwo == "0":
#            continue
#    elif inputChoice == "5":
#        inputChoiceTwo = ui.menuReceiptsCustomer()
#        if inputChoiceTwo == "1":
#            receiptID = input("Enter Customer ID: ")
#            for rec in manageFinancialsController.receiptData:
#                if rec.customerID == receiptID:
#                    print("Sales ID: " + rec.salesID)
#                    print("Customer ID: " + rec.customerID)
#                    print("Price: " + rec.price)
#                    print("Lease ID: " + rec.leaseID)
#        elif inputChoiceTwo == "0":
#            continue
#    elif inputChoice == "0":
#        break
#    else:
#        print("Invalid Choice")

# Employee Menus
#    inputChoice = ui.menuMainEmployee()
#    if inputChoice == "1":
#        inputChoiceTwo = ui.menuInventoryStaff()
#        if inputChoiceTwo == "1":
#            viewInventoryOBJ.viewInventory(manageInventoryController.inventoryData)
#        elif inputChoiceTwo == "2":
#            manageInventoryController.addInventory()
#        elif inputChoiceTwo == "3":
#            manageInventoryController.removeInventory()
#        elif inputChoiceTwo == "4":
#            manageInventoryController.updateInventory()
#        elif inputChoiceTwo == "0":
#            continue
#    elif inputChoice == "2":
#        inputChoiceTwo = ui.menuInquiriesStaff()
#        if inputChoiceTwo == "1":
#            for inquiry in manageInquiryController.inquiryData:
#                print("Customer ID: " + inquiry.customerID)
#                print("Vehicle ID: " + inquiry.vehicleID)
#                print("###############")
#        elif inputChoiceTwo == "0":
#            continue
#    elif inputChoice == "3":
#        inputChoiceTwo = ui.menuCustomerInfoStaff()
#        if inputChoiceTwo == "1":
#            manageCustomersController.addCustomer()
#        elif inputChoiceTwo == "2":
#            manageCustomersController.updateCustomer()
#        elif inputChoiceTwo == "3":
#            manageCustomersController.deleteCustomer()
#        elif inputChoiceTwo == "0":
#            continue
#    elif inputChoice == "4":
#        inputChoiceTwo = ui.menuEmployeeInfoStaff()
#        if inputChoiceTwo == "1":
#            manageEmployeesController.addEmployee()
#        elif inputChoiceTwo == "2":
#            manageEmployeesController.updateEmployee()
#        elif inputChoiceTwo == "3":
#            manageEmployeesController.deleteEmployee()
#        elif inputChoiceTwo == "0":
#            continue
#    elif inputChoice == "5":
#        inputChoiceTwo = ui.menuApplicationsStaff()
#        if inputChoiceTwo == "1":
#            manageFinancialsController.addApplication()
#        elif inputChoiceTwo == "2":
#            manageFinancialsController.deleteApplication()
#        elif inputChoiceTwo == "3":
#            appID = input("Enter Application ID to Approve: ")
#            approveDenyApplicationsOBJ.approveApplication(appID, manageFinancialsController.applicationData)
#        elif inputChoiceTwo == "4":
#            appID = input("Enter Application ID to Deny: ")
#            approveDenyApplicationsOBJ.denyApplication(appID, manageFinancialsController.applicationData)
#        elif inputChoiceTwo == "0":
#            continue
#    elif inputChoice == "6":
#        inputChoiceTwo = ui.menuSalesStaff()
#        if inputChoiceTwo == "1":
#            manageFinancialsController.addSale()
#        elif inputChoiceTwo == "2":
#            manageFinancialsController.deleteSale()
#        elif inputChoiceTwo == "3":
#            manageFinancialsController.updateSale()
#        elif inputChoiceTwo == "4":
#            manageFinancialsController.addLease()
#        elif inputChoiceTwo == "5":
#            manageFinancialsController.updateLease()
#        elif inputChoiceTwo == "6":
#            manageFinancialsController.deleteLease()
#        elif inputChoiceTwo == "7":
#            manageFinancialsController.addReceipt()
#        elif inputChoiceTwo == "8":
#            manageFinancialsController.updateReceipt()
#        elif inputChoiceTwo == "9":
#            manageFinancialsController.deleteReceipt()
#        elif inputChoiceTwo == "0":
#            continue
#    elif inputChoice == "0":
#        break
#    else:
#        print("Invalid Choice")


# Manager Menus
while (loggedIn and inputChoice != "0" and userType == "Manager"):
    inputChoice = ui.menuMainManager()
