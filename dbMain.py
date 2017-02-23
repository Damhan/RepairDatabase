import sqlite3

conn = sqlite3.connect("RepairDb.db")
c = conn.cursor()

def create_table():
    c.execute("CREATE TABLE IF NOT EXISTS phoneInventory(phoneId INTEGER, phoneBrand TEXT, phoneModel TEXT, buyPrice INTEGER, repairCost INTEGER, saleTarget INTEGER)")


def dynamic_data_entry():
    #Get the input and sort it into respective variables
    print("Enter values to be inserted:")
    inputline = input()
    items = inputline.split()
    phoneId = items[0]
    phoneBrand = items[1]
    phoneModel = items[2]
    buyPrice = items[3]
    repairCost = items[4]
    saleTarget = items[5]
    #insert input values into the table as a row
    c.execute("INSERT INTO phoneInventory (phoneId, phoneBrand , phoneModel , buyPrice, repairCost , saleTarget) VALUES(?,?,?,?,?,?)",
    (phoneId,phoneBrand,phoneModel,buyPrice,repairCost,saleTarget))

    conn.commit()

def get_table(t):
    c.execute("SELECT * FROM {} ".format(t))
    data = c.fetchall()
    for d in data:
        print(d)


def table_insertion():
    print("Press enter to begin inserting values.")
    print("Please enter values in the form 'phoneId(int) phoneBrand(str) phonemodel(str) buyPrice(int) repairCost(int) saleTarget(int)'")
    inputting = input()
    while inputting != "done":
        dynamic_data_entry()
        print("When you are done inputting values, please enter 'done', otherwise press enter")
        inputting = input()

def table_viewing():
    print("Enter the name of the table you would like to view")
    tableChoice = input()
    get_table(tableChoice)


def main():
    create_table()
    running = True

    while running:
        print("To insert values into a table press: 'i'")
        print("To view a table, press: 'v'")
        operationSelection = input()
        if operationSelection.lower() == "i":
            table_insertion()
        elif operationSelection.lower() =="v":
            table_viewing()
        print("Do you want to quit?: y/n")
        answer = input().lower()
        if answer == "n":
            running = True
        else:
            running = False
        

    c.close()
    conn.close()


if __name__ == "__main__":
    main()