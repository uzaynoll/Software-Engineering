info_employee = dict()
info_customer = dict()
detail_transaction = list()
log_transaction = list ()

def ReadFile(name: str):
    file= open(name, "r").readlines()
    return file

def Employee_Dictionary(filedata: list):
    for data in filedata:
        data= data.strip().split()
        if data[0] == "e":
            empid = data[1]
            info_employee[empid] = data[2]

def Customer_Dictionary(filedata: list):
    for data in filedata:
        data= data.strip().split()
        if data[0] == "c":
            cusid = data[1]
            info_customer[cusid] = dict()
            info_customer[cusid]["CusName"] = data[2]
            info_customer[cusid]["balance"] = float(data[3])

def Transaction_Dictionary(filedata: list):
    for data in filedata:
        data= data.strip().split()
        if data[0] == "t":
            data_transaction = dict()
            data_transaction["cusID"] = data[1]
            data_transaction["empID"] = data[2]
            data_transaction["transacType"] = data[3]
            data_transaction["amount"] = float(data[4])
            detail_transaction.append(data_transaction)

def Deposit(transaction: dict):
    customerName = info_customer[transaction["cusID"]]["CusName"]
    employeeName = info_employee[transaction["empID"]]
    info_customer[transaction["cusID"]]["balance"] += transaction["amount"]
    log_transaction.append(f"{customerName} {employeeName} +${transaction['amount']:.2f} $ {info_customer[transaction['cusID']]['balance']:.2f}\n")

def Withdraw(transaction: dict):
    customerName = info_customer[transaction["cusID"]]["CusName"]
    employeeName = info_employee[transaction["empID"]]
    info_customer[transaction["cusID"]]["balance"] -= transaction["amount"]
    log_transaction.append(f"{customerName} {employeeName} -${transaction['amount']:.2f} $ {info_customer[transaction['cusID']]['balance']:.2f}\n")

def Transaction():
    log_transaction.append("123456789012345678901234567890123456789012345678901234567890\n")
    for transaction in detail_transaction:
        if transaction["transacType"] == "d":
            Deposit(transaction)
        else:
            Withdraw(transaction)

def TransactionLog(filename: str):
    with open(filename, "w") as fhandler:
        fhandler.writelines(log_transaction)
        print("Transaction log successfully maintained !!!")

def TestResult(testData: list):
    for i in range(len(log_transaction)):
        if testData[i].strip() == log_transaction[i].strip():
            print(f"{i + 1}th data is verified.")
        else:
            print(f"{i + 1}th data is verified.")

filedata = ReadFile("file.txt")

Employee_Dictionary(filedata)
Customer_Dictionary(filedata)
Transaction_Dictionary(filedata)

Transaction()
testdata = ReadFile("CorrectOutput.txt")
TestResult(testdata)
TransactionLog("transactionLog.txt")