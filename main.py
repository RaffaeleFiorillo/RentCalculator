from src.App import App
from src.utils import get_bool_input

if __name__ == "__main__":
	if get_bool_input("Queres importar os dados gravados"):
		app = App.load()
	else:
		app = App()
	app.start()
