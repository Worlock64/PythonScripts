from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, Image
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
from reportlab.graphics.shapes import Drawing
from reportlab.graphics.charts.piecharts import Pie

fruit = {
    "elderberries":1,
    "figs":1,
    "apples":2,
    "durians":3,
    "bananas":5,
    "cherries":8,
    "grapes":13
}

report = SimpleDocTemplate("C:\\Users\\Shamus\\GoogleProjectOne\\report.pdf")
styles = getSampleStyleSheet()

#Generate table in report
table_data=[]
for k,v in fruit.items():
    table_data.append([k,v])

#Add styling to the table
table_style = [('GRID', (0,0), (-1,-1), 1, colors.black)]

#Build the piechart
report_pie = Pie(width=70, height=70)
report_pie.data = []
report_pie.labels=[]
for fruit_name in sorted(fruit):
    report_pie.data.append(fruit[fruit_name])
    report_pie.labels.append(fruit_name)
report_pie.sideLabels=True

#Building blocks for report
report_title = Paragraph("A Complete Inventory of My Fruit", styles["h1"])
report_table = Table(data=table_data, style=table_style, hAlign="LEFT")
report_chart = Drawing()
report_chart.add(report_pie)


report.build([report_title, report_table, report_chart])