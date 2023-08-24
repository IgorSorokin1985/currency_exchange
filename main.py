from src.mvc import Model, View, Controller

model = Model()
view = View()
controller = Controller(model, view)

controller.get_currency_usd()
