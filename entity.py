# Description: This file contains the entity classes for the database. These classes are used to store the data for the database.


# Employee Entity Class
# This class is used to store the employeeID, employeeName, commissions and saleID array of the user
# It has the following attributes: employeeID, employeeName, commissions, saleID and the following methods: getEmployeeID, setEmployeeID, getEmployeeName, setEmployeeName, getCommissions, setCommissions, getSaleID, setSaleID
# Contributors: Seth Tourish
# Date: 11/28/2024
class Employee:
    employeeID = 0 # employeeID of the employee
    employeeName = "" # employeeName of the employee
    commissions = 0.0 # commissions of the employee
    saleID = [] # saleIDs of the sales made by the employee

    def __init__(self, employeeID: str, employeeName: str, commissions: float, saleID: []): # Constructor
        self.employeeID = employeeID
        self.employeeName = employeeName
        self.commissions = commissions
        self.saleID = saleID

    def getEmployeeID(self) -> int: # Getter for employeeID
        return self.employeeID  # Return employeeID
    
    def setEmployeeID(self, employeeID: str): # Setter for employeeID
        self.employeeID = employeeID # Set employeeID

    def getEmployeeName(self) -> str: # Getter for employeeName
        return self.employeeName    # Return employeeName

    def setEmployeeName(self, employeeName: str): # Setter for employeeName
        self.employeeName = employeeName    # Set employeeName

    def getCommissions(self) -> float: # Getter for commissions
        return self.commissions    # Return commissions

    def setCommissions(self, commissions: float): # Setter for commissions
        self.commissions = commissions    # Set commissions
    
    def getSaleID(self) -> []: # Getter for saleID
        return self.saleID   # Return saleID

    def setSaleID(self, saleID: []): # Setter for saleID
        self.saleID = saleID  # Set saleID


# Customer Entity Class
# This class is used to store the customerID, address, customerName, applicationID and leaseID of the user
# It has the following attributes: customerID, address, customerName, applicationID, leaseID and the following methods: getCustomerID, setCustomerID, getAddress, setAddress, getCustomerName, setCustomerName, getApplicationID, setApplicationID, getLeaseID, setLeaseID
# Contributors: Seth Tourish
# Date: 11/28/2024
class Customer:
    customerID = 0  # customerID of the customer
    address = ""    # address of the customer
    customerName = ""   # customerName of the customer
    applicationID = 0   # applicationID of the customer's application
    leaseID = 0 # leaseID of the customer's lease

    def __init__(self, customerID: int, address: str, customerName: str, applicationID: int, leaseID: int): # Constructor
        self.customerID = customerID
        self.applicationID = applicationID
        self.address = address
        self.customerName = customerName
        self.leaseID = leaseID
    
    def getCustomerID(self) -> int: # Getter for customerID
        return self.customerID  # Return customerID

    def setCustomerID(self, customerID: int): # Setter for customerID
        self.customerID = customerID    # Set customerID

    def getAddress(self) -> str: # Getter for address
        return self.address    # Return address

    def setAddress(self, address: str): # Setter for address
        self.address = address    # Set address

    def getCustomerName(self) -> str: # Getter for customerName
        return self.customerName    # Return customerName

    def setCustomerName(self, customerName: str): # Setter for customerName
        self.customerName = customerName    # Set customerName
    
    def getApplicationID(self) -> int: # Getter for applicationID
        return self.applicationID    # Return applicationID
    
    def setApplicationID(self, applicationID: int): # Setter for applicationID
        self.applicationID = applicationID    # Set applicationID
    
    def getLeaseID(self) -> int: # Getter for leaseID
        return self.leaseID    # Return leaseID
    
    def setLeaseID(self, leaseID: int): # Setter for leaseID
        self.leaseID = leaseID    # Set leaseID

# Sales Entity Class
# This class is used to store the saleID, employeeID, customerID, leaseID, applicationID, commissions, receiptID and price of the user
# It has the following attributes: saleID, employeeID, customerID, leaseID, applicationID, commissions, receiptID, price and the following methods: getSaleID, setSaleID, getEmployeeID, setEmployeeID, getCustomerID, setCustomerID, getLeaseID, setLeaseID, getApplicationID, setApplicationID, getCommissions, setCommissions, getReceiptID, setReceiptID, getPrice, setPrice
# Contributors: Seth Tourish
# Date: 11/28/2024
class Sales:
    saleID = 0 # saleID of the sale
    employeeID = 0 # employeeID of the employee
    customerID = 0 # customerID of the customer
    leaseID = 0 # leaseID of the customer
    applicationID = 0 # applicationID of the customer
    commissions = 0.0 # commissions of the salesperson
    receiptID = 0 # receiptID of the sale
    price = 0.0 # price of the vehicle

    def __init__(self, saleID: int, employeeID: int, customerID: int, leaseID: int, applicationID: int, commissions: float, receiptID: int, price: float): # Constructor
        self.saleID = saleID
        self.employeeID = employeeID
        self.customerID = customerID
        self.leaseID = leaseID
        self.applicationID = applicationID
        self.commissions = commissions
        self.receiptID = receiptID
        self.price = price

    def getSaleID(self) -> int: # Getter for saleID
        return self.saleID  # Return saleID
    
    def setSaleID(self, saleID: int): # Setter for saleID
        self.saleID = saleID    # Set saleID

    def getEmployeeID(self) -> int: # Getter for employeeID
        return self.employeeID    # Return employeeID
    
    def setEmployeeID(self, employeeID: int): # Setter for employeeID
        self.employeeID = employeeID    # Set employeeID

    def getCustomerID(self) -> int: # Getter for customerID
        return self.customerID    # Return customerID

    def setCustomerID(self, customerID: int): # Setter for customerID
        self.customerID = customerID    # Set customerID

    def getLeaseID(self) -> int: # Getter for leaseID
        return self.leaseID    # Return leaseID

    def setLeaseID(self, leaseID: int): # Setter for leaseID
        self.leaseID = leaseID    # Set leaseID

    def getApplicationID(self) -> int: # Getter for applicationID
        return self.applicationID    # Return applicationID

    def setApplicationID(self, applicationID: int): # Setter for applicationID
        self.applicationID = applicationID    # Set applicationID

    def getCommissions(self) -> float: # Getter for commissions
        return self.commissions    # Return commissions

    def setCommissions(self, commissions: float): # Setter for commissions
        self.commissions = commissions    # Set commissions

    def getReceiptID(self) -> int: # Getter for receiptID
        return self.receiptID    # Return receiptID

    def setReceiptID(self, receiptID: int): # Setter for receiptID
        self.receiptID = receiptID    # Set receiptID

    def getPrice(self) -> float: # Getter for price
        return self.price    # Return price

    def setPrice(self, price: float): # Setter for price
        self.price = price    # Set price

# Application Entity Class
# This class is used to store the applicationID, customerID, saleID, creditScore, price, income and approveDeny of the user
# It has the following attributes: applicationID, customerID, saleID, creditScore, price, income, approveDeny and the following methods: getApplicationID, setApplicationID, getCustomerID, setCustomerID, getSaleID, setSaleID, getCreditScore, setCreditScore, getPrice, setPrice, getIncome, setIncome, getApproveDeny, setApproveDeny
# Contributors: Seth Tourish
# Date: 11/28/2024
class Application:
    applicationID = 0 # applicationID of the application
    customerID = 0 # customerID of the customer
    saleID = 0 # saleID of the application
    creditScore = 0 # creditScore of the customer
    price = 0.0 # price of the vehicle
    income = 0.0 # income of the customer
    approveDeny = '' # approveDeny status of the application (Char)

    def __init__(self, applicationID: int, customerID: int, saleID: int, creditScore: int, price: float, income: float, approveDeny: str): # Constructor
        self.applicationID = applicationID 
        self.customerID = customerID
        self.saleID = saleID
        self.creditScore = creditScore
        self.price = price
        self.income = income
        self.approveDeny = approveDeny
    
    def getApplicationID(self) -> int: # Getter for applicationID
        return self.applicationID   # Return applicationID

    def setApplicationID(self, applicationID: int): # Setter for applicationID
        self.applicationID = applicationID  # Set applicationID

    def getCustomerID(self) -> int: # Getter for customerID
        return self.customerID  # Return customerID

    def setCustomerID(self, customerID: int): # Setter for customerID
        self.customerID = customerID    # Set customerID

    def getSaleID(self) -> int: # Getter for saleID
        return self.saleID  # Return saleID

    def setSaleID(self, saleID: int): # Setter for saleID
        self.saleID = saleID    # Set saleID    

    def getCreditScore(self) -> int: # Getter for creditScore
        return self.creditScore    # Return creditScore

    def setCreditScore(self, creditScore: int): # Setter for creditScore
        self.creditScore = creditScore    # Set creditScore

    def getPrice(self) -> float: # Getter for price
        return self.price    # Return price

    def setPrice(self, price: float): # Setter for price
        self.price = price    # Set price
    
    def getIncome(self) -> float: # Getter for income
        return self.income    # Return income

    def setIncome(self, income: float): # Setter for income
        self.income = income    # Set income

    def getApproveDeny(self) -> str: # Getter for approveDeny
        return self.approveDeny    # Return approveDeny

    def setApproveDeny(self, approveDeny: str): # Setter for approveDeny
        self.approveDeny = approveDeny    # Set approveDen

# Lease Entity Class
# This class is used to store the leaseID, customerID, vehicleID, monthlyPayment, price and termLength of the user
# It has the following attributes: leaseID, customerID, vehicleID, monthlyPayment, price, termLength and the following methods: getLeaseID, setLeaseID, getCustomerID, setCustomerID, getVehicleID, setVehicleID, getMonthlyPayment, setMonthlyPayment, getPrice, setPrice, getTermLength, setTermLength
# Contributors: Seth Tourish
# Date: 11/28/2024
class Lease: 
    leaseID = 0 # leaseID of the lease
    customerID = 0 # customerID of the customer
    vehicleID = 0 # vehicleID of the vehicle
    monthlyPayment = 0.0 # monthlyPayment of the lease
    price = 0.0 # price of the vehicle
    termLength = 0 # termLength of the lease

    def __init__(self, leaseID: int, customerID: int, vehicleID: int, monthlyPayment: float, price: float, termLength: int): # Constructor
        self.leaseID = leaseID
        self.customerID = customerID
        self.vehicleID = vehicleID
        self.monthlyPayment = monthlyPayment
        self.price = price
        self.termLength = termLength

    def getLeaseID(self) -> int: # Getter for leaseID
        return self.leaseID    # Return leaseID

    def setLeaseID(self, leaseID: int): # Setter for leaseID
        self.leaseID = leaseID    # Set leaseID

    def getCustomerID(self) -> int: # Getter for customerID
        return self.customerID    # Return customerID

    def setCustomerID(self, customerID: int): # Setter for customerID
        self.customerID = customerID    # Set customerID

    def getVehicleID(self) -> int: # Getter for vehicleID
        return self.vehicleID    # Return vehicleID

    def setVehicleID(self, vehicleID: int): # Setter for vehicleID
        self.vehicleID = vehicleID    # Set vehicleID

    def getMonthlyPayment(self) -> float: # Getter for monthlyPayment
        return self.monthlyPayment    # Return monthlyPayment

    def setMonthlyPayment(self, monthlyPayment: float): # Setter for monthlyPayment
        self.monthlyPayment = monthlyPayment    # Set monthlyPayment

    def getPrice(self) -> float: # Getter for price
        return self.price    # Return price

    def setPrice(self, price: float): # Setter for price
        self.price = price    # Set price

    def getTermLength(self) -> int: # Getter for termLength
        return self.termLength    # Return termLength

    def setTermLength(self, termLength: int): # Setter for termLength
        self.termLength = termLength    # Set termLength

# Login Entity Class
# This class is used to store the loginID and password of the user
# It has the following attributes: loginID, password and the following methods: getLoginID, setLoginID, getPassword, setPassword
# Contributors: Seth Tourish, Amin Shawa, Sanabel Elkheir, Jerami Davis
# Date: 11/26/2024
class Login:
    loginID = ""    # loginID of the user
    password = ""   # password of the user

    def __init__(self, loginID: str, password: str):    # Constructor
        self.loginID = loginID  # Initialize
        self.password = password    # Initialize

    def getLoginID(self) -> str:    # Getter for loginID
        return self.loginID   # Return loginID

    def setLoginID(self, loginID: str):  # Setter for loginID
        self.loginID = loginID  # Set loginID

    def getPassword(self) -> str:   # Getter for password
        return self.password    # Return password

    def setPassword(self, password: str):   # Setter for password
        self.password = password    # Set password

# Receipt Entity Class
# This class is used to store the salesID, customerID, price and leaseID of the user
# It has the following attributes: salesID, customerID, price, leaseID and the following methods: getSalesID, setSalesID, getCustomerID, setCustomerID, getPrice, setPrice, getLeaseID, setLeaseID
# Contributors: Seth Tourish
# Date: 11/28/2024
class Receipt:
    salesID = 0 # salesID of the sale
    customerID = 0 # customerID of the customer
    price = 0.0 # price of the vehicle
    leaseID = 0 # leaseID of the lease

    def __init__(self, salesID: int, customerID: int, price: float, leaseID: int): # Constructor
        self.salesID = salesID
        self.customerID = customerID
        self.price = price
        self.leaseID = leaseID
    
    def getSalesID(self) -> int: # Getter for salesID
        return self.salesID # Return salesID

    def setSalesID(self, salesID: int): # Setter for salesID
        self.salesID = salesID  # Set salesID

    def getCustomerID(self) -> int: # Getter for customerID
        return self.customerID # Return customerID

    def setCustomerID(self, customerID: int): # Setter for customerID
        self.customerID = customerID    # Set customerID

    def getPrice(self) -> float: # Getter for price
        return self.price    # Return price

    def setPrice(self, price: float): # Setter for price
        self.price = price    # Set price

    def getLeaseID(self) -> int: # Getter for leaseID
        return self.leaseID    # Return leaseID

    def setLeaseID(self, leaseID: int): # Setter for leaseID
        self.leaseID = leaseID    # Set leaseID

# Financial Records Entity Class
# This class is used to store the budget, revenue and expenses of the company
# It has the following attributes: budget, revenue, expenses and the following methods: getBudget, setBudget, getRevenue, setRevenue, getExpenses, setExpenses
# Contributors: Seth Tourish
# Date: 11/28/2024
class FinancialRecord:
    budget = 0.0    # budget of the company
    revenue = 0.0   # revenue of the company
    expenses = 0.0  # expenses of the company

    def __init__(self, budget: float, revenue: float, expenses: float):    # Constructor
        self.budget = budget    # Initialize
        self.revenue = revenue  # Initialize
        self.expenses = expenses    # Initialize

    def getBudget(self) -> float:    # Getter for budget
        return self.budget  # Return budget

    def setBudget(self, budget: float):  # Setter for budget
        self.budget = budget    # Set budget

    def getRevenue(self) -> float:   # Getter for revenue
        return self.revenue # Return revenue

    def setRevenue(self, revenue: float):  # Setter for revenue
        self.revenue = revenue  # Set revenue

    def getExpenses(self) -> float:  # Getter for expenses
        return self.expenses    # Return expenses

    def setExpenses(self, expenses: float):    # Setter for expenses
        self.expenses = expenses    # Set expenses

# Inquiry Entity Class
# This class is used to store the customerID and vehicleID of the inquiry
# It has the following attributes: customerID, vehicleID and the following methods: getCustomerID, setCustomerID, getVehicleID, setVehicleID
# Contributors: Seth Tourish
# Date: 11/28/2024
class Inquiry:
    customerID = 0 # customerID of the customer
    vehicleID = 0 # vehicleID of the vehicle

    def __init__(self, customerID: int, vehicleID: int): # Constructor
        self.customerID = customerID
        self.vehicleID = vehicleID
    
    def getCustomerID(self) -> int: # Getter for customerID
        return self.customerID  # Return customerID

    def setCustomerID(self, customerID: int): # Setter for customerID
        self.customerID = customerID    # Set customerID

    def getVehicleID(self) -> int: # Getter for vehicleID
        return self.vehicleID    # Return vehicleID

    def setVehicleID(self, vehicleID: int): # Setter for vehicleID
        self.vehicleID = vehicleID    # Set vehicleID

# Inventory Entity Class
# This class is used to store the vehicleID, purchasePrice and salesPrice of the vehicle
# It has the following attributes: vehicleID, purchasePrice, salesPrice and the following methods: getVehicleID, setVehicleID, getPurchasePrice, setPurchasePrice, getSalesPrice, setSalesPrice
# Contributors: Seth Tourish
# Date: 11/28/2024
class Inventory:
    vehicleID = 0 # vehicleID of the vehicle
    purchasePrice = 0.0 # purchasePrice of the vehicle
    salesPrice = 0.0 # salePrice of the vehicle

    def __init__(self, vehicleID: int, purchasePrice: float, salesPrice: float): # Constructor
        self.vehicleID = vehicleID
        self.purchasePrice = purchasePrice
        self.salesPrice = salesPrice

    def getVehicleID(self) -> int: # Getter for vehicleID
        return self.vehicleID    # Return vehicleID
    
    def setVehicleID(self, vehicleID: int): # Setter for vehicleID
        self.vehicleID = vehicleID    # Set vehicleID

    def getPurchasePrice(self) -> float: # Getter for purchasePrice
        return self.purchasePrice    # Return purchasePrice

    def setPurchasePrice(self, purchasePrice: float): # Setter for purchasePrice
        self.purchasePrice = purchasePrice    # Set purchasePrice

    def getSalesPrice(self) -> float: # Getter for salesPrice
        return self.salesPrice    # Return salesPrice

    def setSalesPrice(self, salesPrice: float): # Setter for salesPrice
        self.salesPrice = salesPrice    # Set salesPrice

# Service Record Entity Class
# This class is used to store the serviceID, vehicleID and servicePrice of the service
# It has the following attributes: serviceID, vehicleID, servicePrice and the following methods: getServiceID, setServiceID, getVehicleID, setVehicleID, getServicePrice, setServicePrice
# Contributors: Seth Tourish
# Date: 11/28/2024
class ServiceRecord:
    serviceID = 0 # serviceID of the service
    vehicleID = 0 # vehicleID of the vehicle
    servicePrice = 0.0 # servicePrice of the service

    def __init__(self, serviceID: int, vehicleID: int, servicePrice: float): # Constructor
        self.serviceID = serviceID
        self.vehicleID = vehicleID
        self.servicePrice = servicePrice

    def getServiceID(self) -> int: # Getter for serviceID
        return self.serviceID    # Return serviceID

    def setServiceID(self, serviceID: int): # Setter for serviceID
        self.serviceID = serviceID    # Set serviceID

    def getVehicleID(self) -> int: # Getter for vehicleID
        return self.vehicleID    # Return vehicleID

    def setVehicleID(self, vehicleID: int): # Setter for vehicleID
        self.vehicleID = vehicleID    # Set vehicleID

    def getServicePrice(self) -> float: # Getter for servicePrice
        return self.servicePrice    # Return servicePrice
    
    def setServicePrice(self, servicePrice: float): # Setter for servicePrice
        self.servicePrice = servicePrice    # Set service
