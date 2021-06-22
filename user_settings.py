import os

# set path to settings
curr_dir = os.getcwd()
path = curr_dir + "\\settings.txt"

# change settings prompt
clear_settings = input("Would you like to change your settings? 'y' or 'n'\n")

if clear_settings == "y":
    f = open(path, "r+")
    f.seek(0)
    f.truncate()
    print("Settings cleared!")
elif clear_settings == "n":
    print("Goodbye.")
    exit()

# user inputs settings
defi_service = input("Type the defi service you would like to track.\n(Type it exactly as it appears on GasNow)\n")
tx_speed = input("How Fast would you like your transaction to be?\n(Type: 'rapid' or 'fast'.)\n")
tx_price = input("At which gas price would you like to be alerted?\n(Type a number in the format 0.00)\n")
alert_y_n = input("Do you have an AutoRemote URL?\n(Type 'y' or 'n')\n")

if alert_y_n == "y":
    alert_url = input("Paste your AutoRemote URL here:\n")
elif alert_y_n == "n":
    alert_url = r'N/A'
else:
    print("Illegal input.") 

print(defi_service, file=open(path, "a"))
print(tx_speed, file=open(path, "a"))
print(tx_price, file=open(path, "a"))
print(alert_url, file=open(path, "a"))
