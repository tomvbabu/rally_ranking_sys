import openpyxl


class Racer:
    def __init__(self, comp_no, name, category, time):
        self.millisec = None
        self.comp_no = comp_no
        self.name = name
        self.category = category
        self.time = time

    def to_milli(self):
        minutes, sec, msec = map(int, self.time.split('.'))
        self.millisec = (minutes*60*1000) + (sec*1000) + msec
        return self.millisec

    def show_time(self):
        milli = self.millisec
        minutes = milli // (60*1000)
        milli %= (60*1000)
        seconds = milli // 1000
        milli %= 1000

        return f"{minutes}m {seconds}s {milli}ms"


wb = openpyxl.load_workbook('race_data.xlsx')
ws = wb.active

no_rows = ws.max_row - 1
no_cols = ws.max_column

print(str(no_rows) + " " + str(ws.max_column))

# for j in range(2, no_rows + 1):
#     values = [ws.cell(row=j, column=i).value for i in range(1, no_cols + 1)]
#     print(values)
my_list = list()
for cell in ws.iter_rows(min_row=2, max_row=no_rows+1, min_col=1, max_col=no_cols):
    my_list.append(cell)

racer_list = list()

for comp_no, name, category, time in my_list:
    racer_list.append(Racer(comp_no.value, name.value, category.value, time.value))

for racer in racer_list:
    print(racer.name, racer.to_milli())

print("\n\n")
racer_sort_list = sorted(racer_list,key=lambda racer:racer.to_milli())

for racer in racer_sort_list:
    print(racer.name, racer.to_milli(),racer.time,racer.show_time())

