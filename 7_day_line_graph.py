import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from base_graphing import Get7DayLineGraph

x_days, y_tickets_opened, y_tickets_closed = Get7DayLineGraph()

fig, ax = plt.subplots(1)

plt.plot(x_days, y_tickets_opened, '#f3f00e', linewidth=2)
plt.plot(x_days, y_tickets_closed, '#16811b', linewidth=2)
# ax.plot(x_days, y_tickets_closed)
fig.autofmt_xdate()
plt.legend(['Opened Tickets', 'Closed Tickets'], loc="upper left")
plt.savefig('7Day.png')
# plt.show()
