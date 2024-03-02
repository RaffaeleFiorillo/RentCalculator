from src.utils import get_date_from_input, get_days_between_dates
from datetime import datetime


class Bill:
	def __init__(self):
		self.name: str = input("Insira o nome da Fatura: ").strip()
		self.start_date: datetime = get_date_from_input("Insira a data de Inicio da Fatura")
		self.end_date: datetime = get_date_from_input("Insira a data de Fim da Fatura")
		self.duration: int = get_days_between_dates(self.start_date, self.end_date)
		self.cost: float = float(input("Insira o valor a pagar para esta fatura: "))
	
	def __str__(self):
		return f"Fatura {self.name}: Custo: {self.cost}| Total Dias: {self.duration} | "\
		       f"Data inicio: {self.start_date} | Data Fim: {self.end_date} | "
