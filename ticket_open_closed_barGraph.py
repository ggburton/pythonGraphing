import matplotlib.pyplot as plt
import csv
import os
from time import strptime

REPORT_FILE = os.path.join(os.getcwd()+ os.sep, 'reports', 'report_ticket_delta.csv')
open_tickets = 0
closed_tickets = 0


def Get_autopct(values):
    def my_autopct(pct):
        total = sum(values)
        val = int(pct*total/100.0)
        return '{p:.2f}%  ({v:d})'.format(p=pct, v=val)
    return my_autopct

tickets = []
input_file = csv.DictReader(open(REPORT_FILE))
for row in input_file:
    created_at = strptime(row['date(created_at)'], "%Y-%m-%d")
    if row['date(closed_at)'] == "":
        closed_at = None
    else:
        closed_at = strptime(row['date(closed_at)'], "%Y-%m-%d")
    if row['status'] == 'open':
        open_tickets += 1
    else:
        closed_tickets += 1
    new_ticket = (created_at, closed_at, row['status'])
    tickets.append(new_ticket)

created_days = []
closed_days = []
for ticket in tickets:
    created_days.append(ticket[0].tm_yday)
    if ticket[1] != None:
        closed_days.append(ticket[1].tm_yday)


unique_created_days = set(created_days)
unique_closed_days = set(closed_days)


x_days = []
y_tickets_opened = []
y_tickets_closed = []
for day in sorted(unique_created_days):
    count_created = created_days.count(day)
    count_closed = closed_days.count(day)
    x_days.append(day)
    y_tickets_opened.append(count_created)
    y_tickets_closed.append(count_closed)


for day in sorted(unique_closed_days):
    count = closed_days.count(day)


labels = 'Closed Tickets', 'Open Tickets'
sizes = [closed_tickets, open_tickets]
colors = ['lightskyblue', 'lightcoral']

# plt.pie(sizes, labels=labels, colors=colors, shadow=True, autopct=Get_autopct(sizes))
# plt.axis('equal')
# plt.savefig('test.png')

plt.plot(x_days, y_tickets_opened)
plt.plot(x_days, y_tickets_closed)
plt.legend(['Opened Tickets', 'Closed Tickets'], loc="upper left")
plt.show()

#plt.plot()
#plt.show()
