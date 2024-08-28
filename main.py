import pandas as pd
from fpdf import FPDF  # library to create pdf from python

# to create the pdf object
pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0)

# create the dataframe
df = pd.read_csv('topics_day24.csv')

# create pages in pdf
for index, row in df.iterrows():
    pdf.add_page()  # adds a new page

    # creates the content of the page
    pdf.set_font(family="Times", style="B", size=24)  # sets the font of the page
    pdf.set_text_color(100, 100, 100)  # to set the text color
    pdf.cell(w=0, h=12, txt=row["Topic"], align="L", ln=1)  # sets the config of page and the content
    # to add horizontal lines in the page
    for y in range(20, 275, 10):
        pdf.line(10, y, 200, y)

    pdf.ln(265)  # to add the break line

    # set the footer for the master page
    pdf.set_font(family="Times", style="I", size=10)  # sets the font of the footer
    pdf.set_text_color(100, 100, 100)  # to set the text color
    pdf.cell(w=0, h=10, txt=row["Topic"], align="R", )  # sets the config of footer and the content

    # to iterate inside the loop of the page and add more pages for the same topic
    for i in range(row["Pages"] - 1):
        pdf.add_page()

        pdf.ln(265)  # to add the break line

        # set the footer for the other pages
        pdf.set_font(family="Times", style="I", size=8)  # sets the font of the footer
        pdf.set_text_color(180, 180, 180)  # to set the text color
        pdf.cell(w=0, h=10, txt=row["Topic"], align="R", )  # sets the config of footer and the content

        # to add horizontal lines in the page
        for y in range(20, 275, 10):
            pdf.line(10, y, 200, y)

# output the pdf file on the disk
pdf.output("output.pdf")


