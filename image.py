from reportlab.lib.pagesizes import A4
from reportlab.platypus import (
  SimpleDocTemplate, Image, Paragraph, Table, TableStyle, 
  Frame, Flowable
  )
from reportlab.platypus.figures import ImageFigure
from reportlab.platypus.flowables import ParagraphAndImage, Image, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER

filename = 'banner.png'
barGraph = 'pie.png'
lineGraph = '7day.png'


#create line flowable
class HRLine(Flowable):

    def __init__(self, width, height=0):
        Flowable.__init__(self)
        self.width = width
        self.height = height

    def draw(self):
        self.canv.line(0, self.height, self.width, self.height)



styles = getSampleStyleSheet()
# styles.add(ParagraphStyle(name='centered', alignment=TA_CENTER))

doc = SimpleDocTemplate("image.pdf",
                        pagesize=A4,
                        topMargin=-10)

divider = HRLine(420)

# ##################################################################
# Create Banner


# ##################################################################
headerSpacer = Spacer(210, 50)
ticketSummary = Paragraph('<para alignment="center"><b>Total Open Tickets<b/> <br/>      15 <br/> <hr/>' ,styles['Heading2'])


# ###################################################################
# Create Ticket Change Report
titleTicketChange = Paragraph('<para alignment="center"><b>MONTHLY OPEN/CLOSE REPORT<b/>', styles["Heading2"])
text1 = 'Total tickets = 178 <br/> Tickets closed = 163 <br/> Tickets open = 15 <br/> <br/> <br/> <br/> <br/>'
image = Image(barGraph, width=230, height=160)
paragraph = Paragraph(text1, styles['Normal'])
paraImage = ParagraphAndImage(paragraph, image, xpad=3, ypad=3, side='right')


# #####################################################################
# 7 Day line graph
title7day = Paragraph('<para alignment="center"><b>7 DAY CHANGE<b/>', styles['Heading2'])
text2 = Paragraph('Total new tickets = 33 <br/> Total closed = 30 <br/> Total change = +3 <br/> <br/> <br/> <br/> <br/>' , styles["Normal"])
image2 = Image(lineGraph, width=230, height=160)
paraimage2 = ParagraphAndImage(text2, image2, xpad=3, ypad=3, side='right')

# ####################################################################
# Combine parts to create report

parts = []
parts.append(Image(filename))
parts.append(headerSpacer)
parts.append(ticketSummary)
parts.append(divider)
parts.append(titleTicketChange)
parts.append(paraImage)
parts.append(headerSpacer)
parts.append(divider)
parts.append(title7day)
parts.append(paraimage2)
parts.append(divider)

doc.build(parts)
