from src.utils import get_date_from_input, get_total_days_of_stay, get_int_input, get_bool_input


class Person:
	def __init__(self):
		self.name: str = input("Insira o nome da Pessoa: ").strip()
		self.out_data = {"intervals": [], "days": []}  # intervals of dates where the person stayed at home
		self._get_out_intervals()
		self.bills_data: {str: int} = {}
	
	def __str__(self):
		return f"Pessoa {self.name} | \n{self._get_bills_description()}"
	
	def _get_bills_description(self) -> str:
		descriptions = []
		for bill_name in self.bills_data:
			bill_description = f"   -> {bill_name}: Dias Faturados: {self.bills_data[bill_name]})\n"
			descriptions.append(bill_description)
		
		return "".join(descriptions)
	
	def update_stay_days(self, bills):
		self._get_out_intervals()
		[self.add_bill(bill) for bill in bills]
	
	def _get_out_intervals(self):
		print(f"Vais introduzir os dias em que {self.name} saiu de casa. Podes introduzir valores no formato:\n"
		      f"\tIntervalo (data inicio e data fim): Um intervalo de dias entre duas datas em que a pessoa saiu de casa\n"
		      f"\tDia (data do dia): Um dia específico em que a pessoa saiu de casa")
		while True:
			print("Opções: \n\t1-> Inserir um intervalo; \n\t2->Inserir um dia; \n\t3->Terminar a operação")
			option = get_int_input("Escolhe a tua opção: ")
			match option:
				case 1:
					start_date = get_date_from_input("Insira a Data de Inicio do Intervalo")
					end_date = get_date_from_input("Insira a Data de Fim do Intervalo")
					self.out_data["intervals"].append((start_date, end_date))
				case 2:
					self.out_data["days"].append(get_date_from_input("Insira a data do Dia"))
				case 3:
					return None
			print("----------------------------------------------------------------------------------------------------")
			
	# a bill has the format {"total_days": int}
	def add_bill(self, bill):
		tot_days = get_total_days_of_stay(self.out_data, bill.start_date, bill.end_date)
		print(f"Para a fatura {bill.name} à {self.name} serão faturados um total de {tot_days} dias.")
		if get_bool_input("Queres fazer um ajuste para este valor (adicionar ou subtrair dias)"):
			tot_days += get_int_input(f"Insira o número de dias a serem adicionados (coloque um menos para subtrair): ")
		self.bills_data[bill.name] = tot_days
	