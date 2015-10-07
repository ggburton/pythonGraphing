import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt
from base_graphing import GetTicketStateCount

def Get_autopct(values):
    def my_autopct(pct):
        total = sum(values)
        val = int(pct*total/100.0)
        return '{p:.2f}%  ({v:d})'.format(p=pct, v=val)
    return my_autopct

closed_tickets, open_tickets = GetTicketStateCount()

labels = 'Closed Tickets', 'Open Tickets'
sizes = [closed_tickets, open_tickets]
colors = ['#f3f00e', '#16811b']

plt.pie(sizes, labels=labels, colors=colors, shadow=True, autopct=Get_autopct(sizes))
plt.axis('equal')
plt.savefig('pie.png')
plt.show()


"""
fig, ax = plt.subplots(1)

plt.plot(x_days, y_tickets_opened, '#f3f00e', linewidth=2)
plt.plot(x_days, y_tickets_closed, '#16811b', linewidth=2)
# ax.plot(x_days, y_tickets_closed)
fig.autofmt_xdate()
plt.legend(['Opened Tickets', 'Closed Tickets'], loc="upper left")
plt.show()

#plt.plot()
#plt.show()
"""