# Custom-Gas-Alert
Sends alerts when ETH gas prices go below a user-specified value

# What you will need:
1) Python 3+
2) AutoRemote(Lite) (for notifications, script still works without)
3) Tasker (required if using Autoremote)
4) Selenium (how to install: https://pythonspot.com/selenium-install/)
5) chromedriver*
6) Google Chrome*

*You can substitute Firefox and geckodriver for Google Chrome and chromedriver respectively.

# Getting Started
First, users should open Custom_Gas_Alert.py and add the path to chromedriver behind 'executable path='.
Chromedriver can be downloaded here: https://chromedriver.chromium.org/downloads.
If you are using a raspberry pi to run this script, please follow the instructions here: https://ivanderevianko.com/2020/01/selenium-chromedriver-for-raspberrypi.
You will also need Google Chrome to be installed.

After the path to chromedriver has been added you can close Custom_Gas_Alert.py.

# How to configure Settings
Users should now run user_settings.py.
On your first time type 'y' (case sensitive) to set initial settings. Any time you would like to change settings please run this script again.

1) You will need to type the name of the service you would like to track (type it exactly as it appears on gasnow.org, case sensative). For example: Polygon(Matic)
2) Choose if you want to follow the rapid or fast price (type in all lowercase).
3) You will type the price at which you would like to be alerted. The program will send you an alert anytime the price is less than or equal to this value. Type with no dollar sign and include two decimal places, even if they are both zero.
4) If you have an Autoremote URL type "y", otherwise type "n". Autoremote can be downloaded from the google play store here: https://play.google.com/store/apps/details?id=com.joaomgcd.autoremote&hl=en_US&gl=US (not affiliated). Autoremote allows users to set up a custom URL and then create derivative URLs that send different messages. When the URL is loaded in a browser the device associated with the URL gets a notification. Set this notification to say something along the lines of "It's Polygon Time!" (Note: if using the lite version of Autoremote you may only be allowed a two letter notification).
5) If you answered "y" to the Autoremote URL, you should paste your custom URL (including custom notification) here.
6) Once you've done this you may close out of user_settings.py.

# Autoremote
You can run the script without Autoremote, it will tell you if prices are below your threshold but it will not send a notification. Skip if you don't need notifications.

You will need to have Tasker installed (https://play.google.com/store/apps/details?id=net.dinglisch.android.taskerm&hl=en_US&gl=US). Tasker will allow Autoremote to communicate with your Android device. Once tasker is installed you will need to install Autoremote (link above) or Autoremote Lite (https://play.google.com/store/apps/details?id=com.joaomgcd.autoremote&hl=en_US&gl=US). 

Once both Tasker and Autoremote(Lite) are installed, open Autoremote and locate your URL. Copy and paste this URL into the browser of your choice. Select "Send Notification." Type the message you want to see in the notification in the box under "Message." Copy the longer URL in the blue box, this is what you will paste into the user_settings.py.

# Running the script
Once settings are set (you can verify by opening 'settings.txt') you may run Custom_Gas_Alerts.py as much as you like.

# Extras
I recommend setting this script to run once a day (or at any time interval of your choice) using Task Schedular (Windows) or crontab (Linux) so you can strategically move your coins into defi with as little paid in gas as possible!
