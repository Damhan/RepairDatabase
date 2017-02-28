import sqlite3
import datetime as d

conn = sqlite3.connect("RepairDb.db")
c = conn.cursor()

#Creates an inventory table if one does not exist
def create_table():
	c.execute("CREATE TABLE IF NOT EXISTS phoneInventory(phoneId INTEGER, phoneBrand TEXT, phoneModel TEXT, buyPrice INTEGER, repairCost INTEGER, saleTarget INTEGER)")
	c.execute("CREATE TABLE IF NOT EXISTS phoneHistory(phoneId INTEGER, date TEXT,buyP INTEGER,repairP INTEGER,sellP INTEGER,profit INTEGER)")


def dynamic_data_entry():
    #Get the input and sort it into respective variables (DOESNT MAKE A CHECK FOR INVALID VALUES!!)
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

#Handles inserting values into tables (ONLY HANDLES INSERTION INTO phoneInventory!!) 
def inventory_insertion():
    print("Press enter to begin inserting values.")
    print("Please enter values in the form 'phoneId(int) phoneBrand(str) phonemodel(str) buyPrice(int) repairCost(int) saleTarget(int)'")
    inputting = input()
    while inputting != "done":
        dynamic_data_entry()
        print("When you are done inputting values, please enter 'done', otherwise press enter")
        inputting = input()

#handles deleting values from phoneInventory (DOESNT HANDLE OTHER TABLES!!)
def inventory_deletion():
	print("Do you need to see the table first? y/n")
	answer = input()
	if answer.lower() =="y":
		get_table("phoneInventory")
	print("Enter the id you wish to delete:")
	idPick = input()
	c.execute("SELECT * FROM phoneInventory WHERE phoneId= ?",(idPick,))
	phoneInfo = c.fetchall()
	c.execute("DELETE FROM phoneInventory WHERE phoneId = ?",(idPick,))
	conn.commit()
	phone_history_insertion(phoneInfo)

#Takes info from phoneInventory on deletion and inserts it into the phoneHistory table
def phone_history_insertion(phoneInfo):
	#set up the variables to pass
	phoneInfo = phoneInfo[0]
	phoneId = phoneInfo[0]
	date = d.date.today()
	buyP = phoneInfo[3]
	repairP = phoneInfo[4]
	sellP = phoneInfo[5]
	profit = (sellP-buyP) - repairP
	#insert the values into a new row
	c.execute("INSERT INTO phoneHistory (phoneId, date,buyP,repairP,sellP,profit)  VALUES (?,?,?,?,?,?)",
	(phoneId,date,buyP,repairP,sellP,profit))
	print("Adding to history...")
	conn.commit()
	print("Added!")


#Handles viewing tables
def table_viewing():
    print("Enter the name of the table you would like to view")
    tableChoice = input()
    get_table(tableChoice)

#returns everything in a table and prints it
def get_table(t):
    c.execute("SELECT * FROM {} ".format(t))
    data = c.fetchall()
    for d in data:
        print(d)


#main functions
def main():
    create_table()
    running = True

    while running:
        print("To insert values into a table press: 'i'")
        print("To view a table, press: 'v'")
        print("To delete a row from the inventory press 'd'")
        operationSelection = input()
        if operationSelection.lower() == "i":
            inventory_insertion()
        elif operationSelection.lower() =="v":
            table_viewing()
        elif operationSelection.lower() =="d":
            inventory_deletion()
        #check if we are done or do we want to access another function
        print("Do you want to quit?: y/n")
        answer = input().lower()
        if answer == "n":
            running = True
        else:
            running = False
        
    #close our cursor & connection
    c.close()
    conn.close()


if __name__ == "__main__":
    main()
