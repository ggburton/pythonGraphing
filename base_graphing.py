import csv
import os
from time import strptime
from datetime import datetime

REPORT_MONTHLY = os.path.join(os.getcwd() + os.sep, 
                           'reports', 'report_count_open_closed.csv')
REPORT_WEEKLY = os.path.join(os.getcwd() + os.sep,
                             'reports', 'report_ticket_delta.csv')


def GetTicketStateCount():
    input_file = csv.DictReader(open(REPORT_MONTHLY))
    for row in input_file:
        if row['status'] == 'closed':
            closed_tickets = int(row['count(status)'])
        if row['status'] == 'open':
            open_tickets = int(row['count(status)'])
    return closed_tickets, open_tickets


def Get7DayLineGraph():
    tickets = []
    open_tickets = 0
    closed_tickets = 0
    input_file = csv.DictReader(open(REPORT_WEEKLY))
    for row in input_file:
        created_at = datetime.strptime(row['date(created_at)'],
                                       "%Y-%m-%d").date()
        print(created_at)
        if row['date(closed_at)'] == "":
            closed_at = None
        else:
            closed_at = datetime.strptime(row['date(closed_at)'],
                                          "%Y-%m-%d").date()
        if row['status'] == 'open':
            open_tickets += 1
        else:
            closed_tickets += 1
        new_ticket = (created_at, closed_at, row['status'])
        tickets.append(new_ticket)

    print(len(tickets))
    created_days = []
    closed_days = []
    for ticket in tickets:
        created_days.append(ticket[0])
        if ticket[1] != None:
            closed_days.append(ticket[1])

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

    return x_days, y_tickets_opened, y_tickets_closed
