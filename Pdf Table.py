from fpdf import FPDF


class PDF(FPDF):
    def header(self):
        self.add_font("meiryo", "",fname='meiryo.ttf', uni=True)
        self.set_font("meiryo", "", 14)
        self.cell(0, 10, "Sonkeigo & Kenjougo Verb List", ln=True, align="C")
        self.ln(5)

    def table(self, header, rows):
        self.set_font("Meiryo", "", 10)
        col_widths = [38, 50, 65, 38]
        for i in range(len(header)):
            self.cell(col_widths[i], 8, header[i], border=1, align='C')
        self.ln()
        for row in rows:
            for i in range(len(row)):
                self.cell(col_widths[i], 8, row[i], border=1)
            self.ln()

# Re-create the table content to avoid encoding issues
header = ['Base Verb (普通形)', 'Sonkeigo (尊敬語)', 'Kenjougo (謙譲語)', 'Meaning']
rows = [
    ['行く・来る', 'いらっしゃる / おいでになる', '参ります（まいります）', 'to go / come'],
    ['いる', 'いらっしゃる / おいでになる', 'おります', 'to be (animate)'],
    ['言う', 'おっしゃる', '申します / 申し上げます', 'to say'],
    ['する', 'なさる', 'いたします', 'to do'],
    ['食べる・飲む', '召し上がる（めしあがる）', '頂きます（いただきます）', 'to eat / drink'],
    ['見る', 'ご覧になる（ごらんになる）', '拝見します（はいけんします）', 'to see'],
    ['聞く', 'お聞きになる', '伺います（うかがいます）', 'to hear / ask'],
    ['会う', 'お会いになる', 'お目にかかります', 'to meet'],
    ['知っている', 'ご存じです（ごぞんじです）', '存じております / 存じ上げております', 'to know'],
    ['あげる', '—', '差し上げます（さしあげます）', 'to give (to others)'],
    ['もらう', '—', '頂きます（いただきます）', 'to receive'],
    ['訪ねる', '—', '伺います（うかがいます）', 'to visit'],
    ['尋ねる', '—', '伺います（うかがいます）', 'to inquire / ask'],
    ['思う', 'お思いになる', '存じます（ぞんじます）', 'to think'],
    ['伝える', '—', 'お伝えします', 'to convey / tell']
]

# Generate and save the PDF
pdf = PDF()
pdf.add_page()
pdf.table(header, rows)

file_path = "C:/Users/viony/Sonkeigo/Sonkeigo_Kenjougo_Verbs_Fixed.pdf"
pdf.output(file_path)

file_path
