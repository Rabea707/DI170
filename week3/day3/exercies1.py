#Try to create a countdown to your birthday !

#For example : "My birthday is in 45 days, and 10:29:46"
import datetime
string_date = "10/09/2020"

dt = datetime.strptime(string_date, "%d/%m/%Y")