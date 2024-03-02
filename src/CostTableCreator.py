from src.utils import calculate_cost, get_days_between_dates


class CostTableCreator:
	def __init__(self):
		self.bills_data = {}  # {bill_name: {person1: cost1, person2: cost2, ...}
		self.header = ["-"]
		self.bills_total_costs = {}
		self.rows = []
		
	def _clean_data(self):
		self.bills_data = {}  # {bill_name: {person1: cost1, person2: cost2, ...}
		self.header = ["-"]
		self.bills_total_costs = {}
		self.rows = []
	
	def _create_person_row(self, person, bills):
		columns, person_total_cost = [person.name], 0
		# Creating a column for each bill to pay
		for bill in bills:
			person_stay_days = self.bills_data[bill.name][person.name]['days']
			person_cost = self.bills_data[bill.name][person.name]['cost']
			person_bill_col = f"({person_stay_days}) {person_cost}"
			columns.append(person_bill_col)
			person_total_cost += person_cost
			
			self.bills_total_costs[bill.name] += person_cost
		
		# Creating the last column with the total amount to pay
		person_tot_col = f"{round(person_total_cost, 2)}"
		columns.append(person_tot_col)
		
		return columns
	
	def _create_total_cost_row(self, bills):
		total_cost_row = ["Somatório"]
		for bill in bills:
			total_cost = str(round(self.bills_total_costs[bill.name], 2))
			total_cost_row.append(total_cost)
		total_cost_row.append("-")
		
		return total_cost_row
	
	def _create_confirmation_rows(self, bills):
		total_cost_row, difference_row = ["Somatório"], ["Real-Soma"]
		total_difference = 0
		for bill in bills:
			total_cost = round(self.bills_total_costs[bill.name], 2)
			difference = round(bill.cost - total_cost, 2)
			total_difference += difference
			total_cost_row.append(str(total_cost))
			difference_row.append(str(difference))
		total_cost_row.append("-")
		difference_row.append(str(total_difference))
		
		self.rows.append(total_cost_row)
		self.rows.append(difference_row)
	
	def _create_rows(self, people, bills):
		self.rows.append(self.header)
		for person in people:
			self.rows.append(self._create_person_row(person, bills))
		self._create_confirmation_rows(bills)
	
	def _create_column_data(self, people, bill):
		bill_total_duration = sum([person.bills_data[bill.name] for person in people])
		bill_cost_per_day = bill.cost / bill_total_duration
		
		# {bill_name: {person1: cost1, person2: cost2, ...}
		for person in people:
			person_stay = person.bills_data[bill.name]
			cost = calculate_cost(bill_cost_per_day, person_stay)
			self.bills_data[bill.name][person.name] = {"days": person_stay, "cost": cost}
	
	def _extract_data(self, people, bills):
		self.bills_total_costs = {bill.name: 0 for bill in bills}  # initialize the total costs
		for bill in bills:
			self.header.append(bill.name)
			self.bills_data[bill.name] = {}
		self.header.append("Total")
		[self._create_column_data(people, bill) for bill in bills]
		
	def _print_table(self):
		# Determine the width of each column
		column_width = [max(len(str(row[i])) + 2 for row in self.rows) for i in range(len(self.rows[0]))]
		
		# Print the table header
		print("┌" + "┬".join("─" * width for width in column_width) + "┐")
		print("│" + "│".join(f"{column: ^{column_width[i]}}" for i, column in enumerate(self.rows[0])) + "│")
		print("├" + "┼".join("─" * width for width in column_width) + "┤")
		
		# Print the table body
		for row in self.rows[1:-2]:
			print("│" + "│".join(f"{row[i]: ^{column_width[i]}}" for i in range(len(row))) + "│")
			
		print("├" + "┼".join("─" * width for width in column_width) + "┤")
		print("│" + "│".join(f"{self.rows[-2][i]: ^{column_width[i]}}" for i in range(len(self.rows[-2]))) + "│")
		print("├" + "┼".join("─" * width for width in column_width) + "┤")
		print("│" + "│".join(f"{self.rows[-1][i]: ^{column_width[i]}}" for i in range(len(self.rows[-1]))) + "│")
		
		# Print the table footer
		print("└" + "┴".join("─" * width for width in column_width) + "┘")
		
	def calculate_costs(self, people, bills):
		self._clean_data()
		self._extract_data(people, bills)
		self._create_rows(people, bills)
		self._print_table()
