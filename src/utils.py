from datetime import datetime


def get_days_between_dates(start_date: datetime, end_date: datetime):
	difference = end_date - start_date
	return difference.days


def is_date_inside_interval(date_to_check: datetime, start_date: datetime, end_date: datetime):
	return start_date <= date_to_check <= end_date


def get_overlap_between_date_intervals(start_date1: datetime, end_date1: datetime, start_date2: datetime, end_date2: datetime):
	latest_start = max(start_date1, start_date2)  # Find the latest of the two start dates
	earliest_end = min(end_date1, end_date2) 	  # Find the earliest of the two end dates
	
	# Calculate the difference in days if there is an overlap
	overlap_days = (earliest_end - latest_start).days + 1 if earliest_end > latest_start else 0
	
	return overlap_days


def get_total_days_of_stay(stay_data: dict, start_date: datetime, end_date: datetime):
	days_of_stay = get_days_between_dates(start_date, end_date)
	
	for interval in stay_data["intervals"]:
			days_of_stay -= get_overlap_between_date_intervals(start_date, end_date, interval[0], interval[1])
	
	for day in stay_data["days"]:
		days_of_stay -= 1 if is_date_inside_interval(day, start_date, end_date) else 0
	
	return days_of_stay


def get_date_from_input(label):
	while True:
		try:
			start_date_str = input(f"{label} no formato dd-mm-aaaa (ex: 01-02-2024): ")
			return datetime.strptime(start_date_str, "%d-%m-%Y")
		except ValueError:
			print("Erro: A data inserida deve estar no formato adequado!")


def get_bool_input(label):
	answer = input(f"{label} (sim ou nao): ")
	return "s" in answer

	
def get_float_input(label):
	while True:
		try:
			return float(input(label).strip())
		except ValueError:
			print("Erro: O valor deve ser um número válido!")
			

def get_int_input(label):
	while True:
		try:
			return int(input(label).strip())
		except ValueError:
			print("Erro: O valor deve ser um número inteiro válido!")
		
			
def calculate_cost(cost_per_day, days):
	return round(days*cost_per_day, 2)