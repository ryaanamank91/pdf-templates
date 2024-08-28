import pandas as pd
from fpdf import FPDF  # library to create pdf from python

# to create the pdf object
pdf = FPDF(orientation="P", unit="mm", format="A4")

# create the dataframe
df = pd.read_csv('topics_day24.csv')

# create pages in pdf
for index, row in df.iterrows():
    pdf.add_page()  # adds a new page

    # creates the content of the page
    pdf.set_font(family="Times", style="B", size=24)  # sets the font of the page
    pdf.set_text_color(100, 100, 100)  # to set the text color
    pdf.cell(w=0, h=12, txt=row["Topic"], align="L", ln=1)  # sets the config of page and the content
    pdf.line(x1=10, y1=21, x2=200, y2=21)  # To add an underline below the topics

# output the pdf file on the disk
pdf.output("output.pdf")


