import datetime

dts = datetime.datetime.now()
dts = str(dts)
P = open("Automated Patchlog.txt", "at")
P.write("Automated logging requested at " + dts + "\n")
print("Added the following: Automated logging requested at " + dts)
