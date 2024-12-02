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
finalizePurchaseController = control.FinalizePurchase()

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
                ui.employeeMenuLoop(manageEmployeesController, manageFinancialsController, manageInventoryController, manageCustomersController, manageInquiryController, viewInventoryOBJ, generateFinancialReportOBJ, approveDenyApplicationsOBJ, calcEmployeeCommissionOBJ, viewApplicationResultsOBJ, finalizePurchaseController, loggedIn, userType)
            elif (loggedIn and (username[0] == 'M' or username[0] == 'm')): # if user is manager
                userType = "Manager"    # set userType to Manager
                ui.managerMenuLoop(manageEmployeesController, manageFinancialsController, manageInventoryController, manageCustomersController, manageInquiryController, viewInventoryOBJ, generateFinancialReportOBJ, approveDenyApplicationsOBJ, calcEmployeeCommissionOBJ, viewApplicationResultsOBJ, finalizePurchaseController, loggedIn, userType)
            elif (loggedIn and (username[0] == 'C' or username[0] == 'c')): # if user is customer
                userType = "Customer"   # set userType to Customer
                ui.customerMenuLoop(manageEmployeesController, manageFinancialsController, manageInventoryController, manageCustomersController, manageInquiryController, viewInventoryOBJ, generateFinancialReportOBJ, approveDenyApplicationsOBJ, calcEmployeeCommissionOBJ, viewApplicationResultsOBJ, finalizePurchaseController, loggedIn, userType)
        else:   # if login is unsuccessful
            print("Login Failed, Please Retry") # print login failed message
            continue    # continue loop
    elif inputChoice == "0":    # if user chooses to exit
        break   # break loop
    else:   # if user enters invalid choice
        print("Invalid Choice")   # print invalid choice message



# We gather here today
# To mourn the passing of the code
# That was once so great
# But now is no more
# It was a good code
# It was a great code
# It was the best code
# But now it is gone
# It was a code that was loved
# It was a code that was cherished
# It was a code that was admired
# But now it is no more
# So let us remember the code
# Let us remember the good times
# Let us remember the great times
# But let us also remember
# That all code must die
# And so we say goodbye
# To the code that was once so great
# And we move on
# To the code that will be even greater
# So let us remember the code
# And let us move on
# To the code that will be
# The best code of all
# Goodbye old code
# Hello new code
# Contributors: Copilot
# Date: 12/1/2024