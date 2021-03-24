from bs4 import BeautifulSoup
import csv
#aa.txt => html code "marketplace div"
myFile = open('aa')
soup = BeautifulSoup(myFile, features="html.parser")

file = open('stats.csv', 'w', newline='')
writer = csv.writer(file)

# write a header row
writer.writerow(['selection', 'eventdate', 'eventtime', 'stake', 'odds', 'return'])

# Beautifulsoup, tabs => div for each event
tabs = soup.find_all('div', class_="bet-summary-detail")

# get info for each event
for tabs in tabs:
    eventdate = tabs.find('div', class_="bet-summary-detail-placement-date-date").text
    eventtime = tabs.find('div', class_="bet-summary-detail-placement-date-time").text
    eventsel = tabs.find('div', class_="selection").text
    eventodds = tabs.find('div', class_="bet-summary-detail-odds").text
    eventreturn = tabs.find('span', class_="bet-summary-detail-amounts-return-value").text
    eventstake = tabs.find('div', class_="bet-summary-detail-amounts-multiples").text
#     ####STAKEformat
    eventstakeedit1 = eventstake.strip().split(" ", 0)
    eventstakeready = eventstake.strip().split(" Ft")[0]

    #### RETURNformat
    eventreturnready = eventreturn.strip().split(" ")[1]

    #####csv write

    writer.writerow([eventsel, eventdate, eventtime, eventstakeready, eventodds, eventreturnready])

    #### ODDSformat
    # ####SELformat
    # print('************************************************************')
    # print('date    ' + eventdate)
    # print('time    ' + eventtime)
    # print('sel    ' + eventsel)
    # print('odds    ' + eventodds)
    # print('return  ' + eventreturnready)
    # print('stake  ' + eventstakeready)
file.close()
