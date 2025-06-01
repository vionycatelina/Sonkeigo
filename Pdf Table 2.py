from fpdf import FPDF

class PDF(FPDF):
    def __init__(self):
        super().__init__()
        self.set_auto_page_break(auto=True, margin=15)
        self.add_page()
        self.add_font("meiryo", "",fname='meiryo.ttf', uni=True)
        self.set_font("meiryo", "", 14)

    def add_wrapped_table(self, header, data, col_widths, line_height=8):
        # Print header
        self.set_font("meiryo", size=10)
        self._print_row(header, col_widths, line_height)
        self.set_font("meiryo", size=10)

        # Print data rows
        for row in data:
            self._print_row(row, col_widths, line_height)

    def _print_row(self, row, col_widths, line_height):
        # Calculate the height of the row
        max_lines = 0
        for i, cell in enumerate(row):
            lines = self.multi_cell(col_widths[i], line_height, cell, border=0, align='L', split_only=True)
            max_lines = max(max_lines, len(lines))
        row_height = max_lines * line_height

        x_start = self.get_x()
        y_start = self.get_y()

        for i, cell in enumerate(row):
            x = x_start + sum(col_widths[:i])
            self.set_xy(x, y_start)
            self.multi_cell(col_widths[i], line_height, cell, border=1, align='L')
            self.set_xy(x + col_widths[i], y_start)

        self.set_y(y_start + row_height)

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

col_widths = [40, 50, 60, 40]

# Generate PDF again
pdf = PDF()
pdf.add_wrapped_table(header, rows, col_widths)
pdf_path = "keigo_table_wrapped.pdf"
pdf.output(pdf_path)
pdf_path
