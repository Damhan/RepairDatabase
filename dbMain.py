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


create_table()
print("Press enter to begin inserting values.")
print("Please enter values in the form 'phoneId(int) phoneBrand(str) phonemodel(str) buyPrice(int) repairCost(int) saleTarget(int)'")
inputting = input()
while inputting != "done":
    dynamic_data_entry()
    print("When you are done inputting values, please enter 'done', otherwise press enter")
    inputting = input()

c.close()
conn.close()
