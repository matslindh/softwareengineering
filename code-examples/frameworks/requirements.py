class Item:
    def __init__(self, price):
        pass

def price_with_25pp(price):
    """ Returns price with tax added """
    return price * 1.25

# Scenario: Tegne et brukerstyrt vindu og tekst til skjerm
window = userinterface.Window(title='Vindu', draggable=False)
screen.add_component(window, x=100, y=200)

text = userinterface.Text(text='Aphex Legendrs')
screen.add_component(text, x=50, y=20)
screen.render()






