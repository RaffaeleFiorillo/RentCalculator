from src.utils import get_int_input
from src.Person import Person
from src.Bill import Bill
from src.CostTableCreator import CostTableCreator
import os
import pickle


class App:
	SAVE_FILE_NAME = "assets/save_data.pickle"
	
	def __init__(self):
		self.people: [Person] = []
		self.bills: [Bill] = []
		self.table_creator = CostTableCreator()
	
	def _save(self):
		with open(self.SAVE_FILE_NAME, 'wb') as f:
			pickle.dump(self, f)
		print(f"Dados Gravados com Sucesso!")
		
	@staticmethod
	def load():
		try:
			with open(App.SAVE_FILE_NAME, 'rb') as f:
				return pickle.load(f)
		except FileNotFoundError:
			print("Save file not found.")
			return None
		except Exception as e:
			print(f"Error loading save file: {e}")
			return None
	
	# ----------------------------------------- People Options ---------------------------------------------------------
	def _add_person(self):
		os.system("cls")
		print("------------------------------------------- Adicionar Pessoa -------------------------------------------\n")
		person = Person()
		self.people.append(person)
		[person.add_bill(bill) for bill in self.bills]
		print(f"Pessoa Criada com sucesso! \n\t{person}")
	
	def _remove_person(self):
		os.system("cls")
		print("-------------------------------------------- Remover Pessoa --------------------------------------------\n")
		people_names = [person.name for person in self.people]
		print("Pessoas Existentes: " + ", ".join(people_names))
		person_name = input("Insira o nome da Pessoa que deseja remover: ").strip()
		
		if person_name in people_names:
			self.people = [person for person in self.people if person.name != person_name]
			print("Pessoa Removida com sucesso!")
		else:
			print("Erro: Pessoa não encontrada! Tem certeza que inseriu o nome corretamente?")
	
	def _display_all_persons(self):
		os.system("cls")
		print("------------------------------------------- Mostrar Pessoas --------------------------------------------\n")
		[print(person) for person in self.people]
		
	# -----------------------------------------  Bills Options ---------------------------------------------------------
	def _add_bill(self):
		os.system("cls")
		print("------------------------------------------- Adicionar Fatura -------------------------------------------\n")
		bill = Bill()
		self.bills.append(bill)
		print(f"Fatura Criada com sucesso! \n\t{bill}")
		if self.people:
			print("------------------------------------------- Atualizar Pessoas -------------------------------------------\n")
			[person.add_bill(bill) for person in self.people]
		
	def _remove_bill(self):
		os.system("cls")
		print("-------------------------------------------- Remover Fatura --------------------------------------------\n")
		bills_names = [bill.name for bill in self.bills]
		print("Faturas Existentes: " + ", ".join(bills_names))
		bill_name = input("Insira o nome da Fatura que deseja remover: ").strip()
		
		if bill_name in bills_names:
			self.bills = [bill for bill in self.bills if bill.name != bill_name]
			print("Fatura Removida com sucesso!")
		else:
			print("Erro: Fatura não encontrada! Tem certeza que inseriu o nome corretamente?")
			
	def _display_all_bills(self):
		os.system("cls")
		print("------------------------------------------- Mostrar Faturas --------------------------------------------\n")
		[print(bill) for bill in self.bills]
	
	# ----------------------------------------- Costs Option --------------------------------------------------------------
	def _calculate_costs(self):
		os.system("cls")
		print("------------------------------------------- Tabela de Custos -------------------------------------------\n")
		self.table_creator.calculate_costs(self.people, self.bills)
	
	# ----------------------------------------- Main Menu --------------------------------------------------------------
	@staticmethod
	def _display_menu():
		print("------------------------------------------------- MENU -------------------------------------------------\n"
		      "\t1 -> [Adicionar Pessoa]: Adicionar uma das pessoas que vai dividir as despesas.\n"
		      "\t2 -> [ Remover Pessoa ]: Remover uma pessoa entre às que vão dividir as despesas.\n"
		      "\t3 -> [Mostrar Pessoas]: Adicionar uma Fatura para que o seu custo por pessoa seja calculado.\n"
		      "\t4 -> [Adicionar Fatura]: Adicionar uma Fatura para que o seu custo por pessoa seja calculado.\n"
		      "\t5 -> [ Remover Fatura ]: Remover uma Fatura para que o seu custo seja excluído dos calculos.\n"
		      "\t6 -> [Mostrar Faturas]: Adicionar uma Fatura para que o seu custo por pessoa seja calculado.\n"
		      "\t7 -> [Calcular Despesas]: Mostra uma tabela detalhando os custos de cada Pessoa para cada Fatura.\n"
		      "\t8 -> [   Gravar Dados  ]: Caso a Aplicação fechar, será possível retomar do ponto em que gravase.\n"
		      "\t9 -> [      Sair      ]: Terminar a execução do programa. ATENÇÃO: Qualquer dado inserido vai ser perdido.\n"
		      )
	
	def start(self):
		options_functions = {1: self._add_person, 2: self._remove_person, 3: self._display_all_persons,
		                     4: self._add_bill, 5: self._remove_bill, 6: self._display_all_bills,
		                     7: self._calculate_costs, 8: self._save, 9: exit}
		
		while True:
			os.system("cls")  # clear the content of what was done in the previous option
			self._display_menu()
			option = get_int_input("Insira o número da operação que queres efetuar: ")
			options_functions[option]()
			input("\n(Pressione qualquer botão para voltar ao Menu)")
