from src.utils import *


def calculate_cost(cost_per_day, days):
	print(cost_per_day, days)
	return round(days*cost_per_day, 2)


l_start_date = datetime.strptime("21-01-2024", "%d-%m-%Y")
l_end_date = datetime.strptime("20-02-2024", "%d-%m-%Y")
l_duration = get_days_between_dates(l_start_date, l_end_date)
l_cost = 64.38

w_start_date = datetime.strptime("20-01-2024", "%d-%m-%Y")
w_end_date = datetime.strptime("20-02-2024", "%d-%m-%Y")
w_duration = get_days_between_dates(w_start_date, w_end_date)
w_cost = 23.74


g_start_date = datetime.strptime("19-01-2024", "%d-%m-%Y")
g_end_date = datetime.strptime("19-02-2024", "%d-%m-%Y")
g_duration = get_days_between_dates(g_start_date, g_end_date)
g_cost = 25.30

# ------------------------------------------------- ELLEN -------------------------------------------------------------
ellen_days_out = 12
ellen_l_stay = l_duration - ellen_days_out
ellen_w_stay = w_duration - ellen_days_out
ellen_g_stay = g_duration - ellen_days_out
# ------------------------------------------------- CAROL -------------------------------------------------------------
carol_l_stay = l_duration
carol_w_stay = w_duration
carol_g_stay = g_duration
# ------------------------------------------------- RAISSA -------------------------------------------------------------
raissa_l_stay = l_duration
raissa_w_stay = w_duration
raissa_g_stay = g_duration
# ------------------------------------------------- TAISSA -------------------------------------------------------------
taissa_out_start = datetime.strptime("01-02-2024", "%d-%m-%Y")
taissa_out_end = datetime.strptime("13-02-2024", "%d-%m-%Y")
taissa_days_out = get_days_between_dates(taissa_out_start, taissa_out_end)

taissa_l_stay = l_duration - taissa_days_out
taissa_w_stay = l_duration - taissa_days_out
taissa_g_stay = l_duration - taissa_days_out

# ------------------------------------------------- RAFAEL -------------------------------------------------------------
rafael_l_stay = taissa_l_stay
rafael_w_stay = taissa_w_stay
rafael_g_stay = taissa_g_stay
# ------------------------------------------------- COSTS -------------------------------------------------------------
l_total_duration = carol_l_stay + ellen_l_stay + rafael_l_stay + raissa_l_stay + taissa_l_stay
l_cost_per_day = l_cost/l_total_duration
carol_l_cost = calculate_cost(l_cost_per_day, carol_l_stay)
ellen_l_cost = calculate_cost(l_cost_per_day, ellen_l_stay)
rafael_l_cost = calculate_cost(l_cost_per_day, rafael_l_stay)
raissa_l_cost = calculate_cost(l_cost_per_day, raissa_l_stay)
taissa_l_cost = calculate_cost(l_cost_per_day, taissa_l_stay)

w_total_duration = carol_w_stay + ellen_w_stay + rafael_w_stay + raissa_w_stay + taissa_w_stay
w_cost_per_day = w_cost/w_total_duration
carol_w_cost = calculate_cost(w_cost_per_day, carol_w_stay)
ellen_w_cost = calculate_cost(w_cost_per_day, ellen_w_stay)
rafael_w_cost = calculate_cost(w_cost_per_day, rafael_w_stay)
raissa_w_cost = calculate_cost(w_cost_per_day, raissa_w_stay)
taissa_w_cost = calculate_cost(w_cost_per_day, taissa_w_stay)

g_total_duration = carol_g_stay + ellen_g_stay + rafael_g_stay + raissa_g_stay + taissa_g_stay
g_cost_per_day = g_cost/g_total_duration
carol_g_cost = calculate_cost(g_cost_per_day, carol_g_stay)
ellen_g_cost = calculate_cost(g_cost_per_day, ellen_g_stay)
rafael_g_cost = calculate_cost(g_cost_per_day, rafael_g_stay)
raissa_g_cost = calculate_cost(g_cost_per_day, raissa_g_stay)
taissa_g_cost = calculate_cost(g_cost_per_day, taissa_g_stay)
print(taissa_g_stay)

# ------------------------------------------------- COLUMNS-------------------------------------------------------------
carol_l_col = f"({carol_l_stay}) {carol_l_cost}"
carol_w_col = f"({carol_w_stay}) {carol_w_cost}"
carol_g_col = f"({carol_g_stay}) {carol_g_cost}"
carol_tot_col = f"{round(carol_l_cost+carol_w_cost+carol_g_cost, 2)}"

ellen_l_col = f"({ellen_l_stay}) {ellen_l_cost}"
ellen_w_col = f"({ellen_w_stay}) {ellen_w_cost}"
ellen_g_col = f"({ellen_g_stay}) {ellen_g_cost}"
ellen_tot_col = f"{round(ellen_l_cost+ellen_w_cost+ellen_g_cost, 2)}"

rafael_l_col = f"({rafael_l_stay}) {rafael_l_cost}"
rafael_w_col = f"({rafael_w_stay}) {rafael_w_cost}"
rafael_g_col = f"({rafael_g_stay}) {rafael_g_cost}"
rafael_tot_col = f"{round(rafael_l_cost+rafael_w_cost+rafael_g_cost, 2)}"

raissa_l_col = f"({raissa_l_stay}) {raissa_l_cost}"
raissa_w_col = f"({raissa_w_stay}) {raissa_w_cost}"
raissa_g_col = f"({raissa_g_stay}) {raissa_g_cost}"
raissa_tot_col = f"{round(raissa_l_cost+raissa_w_cost+raissa_g_cost, 2)}"

taissa_l_col = f"({taissa_l_stay}) {taissa_l_cost}"
taissa_w_col = f"({taissa_w_stay}) {taissa_w_cost}"
taissa_g_col = f"({taissa_g_stay}) {taissa_g_cost}"
taissa_tot_col = f"{round(taissa_l_cost+taissa_w_cost+taissa_g_cost, 2)}"

# ------------------------------------------------- TOTAL COLUMN -------------------------------------------------------
total_l_days = ellen_l_stay + taissa_l_stay + rafael_l_stay + carol_l_stay + raissa_l_stay
total_w_days = ellen_w_stay + taissa_w_stay + rafael_w_stay + carol_w_stay + raissa_w_stay
total_g_days = ellen_g_stay + taissa_g_stay + rafael_g_stay + carol_g_stay + raissa_g_stay

total_l_col = f"{l_cost} | {round(sum([ellen_l_cost, carol_l_cost, raissa_l_cost, taissa_l_cost, rafael_l_cost]), 2)}"
total_w_col = f"{w_cost} | {round(sum([ellen_w_cost, carol_w_cost, raissa_w_cost, taissa_w_cost, rafael_w_cost]), 2)}"
total_g_col = f"{g_cost} | {round(sum([ellen_g_cost, carol_g_cost, raissa_g_cost, taissa_g_cost, rafael_g_cost]), 2)}"


header = ["", "Luz", "Água", "Gás", "Total"]
ellen_row = ["Ellen", ellen_l_col, ellen_w_col, ellen_g_col, ellen_tot_col]
rafael_row = ["Rafael", rafael_l_col, rafael_w_col, rafael_g_col, rafael_tot_col]
taissa_row = ["Taissa", taissa_l_col, taissa_w_col, taissa_g_col, taissa_tot_col]
raissa_row = ["Raissa", raissa_l_col, raissa_w_col, raissa_g_col, raissa_tot_col]
carol_row = ["Carol", carol_l_col, carol_w_col, carol_g_col, carol_tot_col]
total_row = ["Confirmação", total_l_col, total_w_col, total_g_col, "-"]

ROWS = [header, carol_row, ellen_row, rafael_row, raissa_row, taissa_row, total_row]


def print_table(rows):
	if not rows:
		print("No data to display")
		return
	# Determine the width of each column
	column_width = [max(len(str(row[i]))+2 for row in rows) for i in range(len(rows[0]))]
	
	# Print the table header
	print("┌" + "┬".join("─" * width for width in column_width) + "┐")
	print("│" + "│".join(f"{column: ^{column_width[i]}}" for i, column in enumerate(rows[0])) + "│")
	print("├" + "┼".join("─" * width for width in column_width) + "┤")
	
	# Print the table body
	for row in rows[1:-1]:
		print("│" + "│".join(f"{row[i]: ^{column_width[i]}}" for i in range(len(row))) + "│")
	print("├" + "┼".join("─" * width for width in column_width) + "┤")
	print("│" + "│".join(f"{rows[-1][i]: ^{column_width[i]}}" for i in range(len(rows[-1]))) + "│")
	
	# Print the table footer
	print("└" + "┴".join("─" * width for width in column_width) + "┘")


print_table(ROWS)

[['-', 'Luz', 'Total', 'Luz', 'Agua', 'Gas', 'Total'],
 ['Ellen', '(18) 10.17', '(19) 3.86', '(19) 4.11', '18.14'],
 ['Carol', '(30) 16.94', '(31) 6.29', '(31) 6.7', '29.93'],
 ['Raissa', '(30) 16.94', '(31) 6.29', '(31) 6.7', '29.93'],
 ['Taissa', '(18) 10.17', '(18) 3.65', '(18) 3.89', '17.71'],
 ['Rafael', '(18) 10.17', '(18) 3.65', '(18) 3.89', '17.71'],
 ['Confirmação', 64.39, 23.74, 25.290000000000003, '-']
 ]
