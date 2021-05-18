#!/usr/bin/env python3
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph, Spacer, Table, Image
from reportlab.lib.styles import getSampleStyleSheet
import cars
from reportlab.lib import colors
from reportlab.graphics.shapes import Drawing
from reportlab.graphics.charts.piecharts import Pie


def generate(filename, title, additional_info, table_data):
    """"generate function automate generation of pdf report from a give data
    it include Pie graphic report using Pie module"""
    styles = getSampleStyleSheet()
    report = SimpleDocTemplate(filename)
    report_title = Paragraph(title, styles["h1"])
    report_info = Paragraph(additional_info, styles["BodyText"])
    table_style = [('GRID', (0, 0), (-1, -1), 1, colors.black),
                   ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                   ('ALIGN', (0, 0), (-1, -1), 'CENTER')]
    report_table = Table(data=table_data, style=table_style, hAlign="LEFT")
    empty_line = Spacer(1, 20)

    # Generate Pie
    report_pie = Pie(width=3 * inch, height=3 * inch)
    report_pie.data = []
    report_pie.labels = []
    # this function retrive car and sales number from car data
    # Sort the list of cars in the PDF by total sales.
    # Create a pie chart for the total sales of each car made.
    car_sales = cars.car_total_sales("car_sales.json")
    for car_name in sorted(car_sales):
        report_pie.data.append(car_sales[car_name])
        report_pie.labels.append(car_name)
    report_chart = Drawing()
    report_chart.add(report_pie)

    report.build([report_title, empty_line, report_info, empty_line, report_table, report_chart])
