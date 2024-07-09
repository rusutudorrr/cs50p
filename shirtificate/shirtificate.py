from fpdf import FPDF, XPos, YPos


class Shirtificate(FPDF):

    def header(self):
        self.set_font("Helvetica", "B", 50)
        self.cell(0, 10, "CS50 Shirtificate", new_x=XPos.LMARGIN, new_y=YPos.NEXT, align='C')

    def add_shirt(self, name):
        self.image("shirtificate.png", 10, 60, 190)
        self.set_text_color(255, 255, 255)  # white font
        self.set_font("Helvetica", "B", 20)
        self.set_y(120)  # Set the y coord
        shirt_text = f"{name} took CS50"
        self.cell(0, 10, shirt_text, new_x=XPos.LMARGIN, new_y=YPos.NEXT, align='C')



def main():

    shirtificate = Shirtificate()
    shirtificate.add_page()

    name = input("Enter your name: ")

    shirtificate.add_shirt(name)

    shirtificate.output('shirtificate.pdf')


if __name__ == "__main__":
    main()
