#
#
#
#

import ui
from numpy import random

# picks a random number
number_to_guess = random.randint(1, 10)
print(number_to_guess)

def check_button_touch_up_inside(sender):
    
    #input
    number_entered = int(view ['number_textfield'].text)

    #process
    if number_entered == number_to_guess:
        view['response_label'].text = "CORRECT"
    else:
        view['response_label'].text = "WRONG"




view = ui.load_view()
view.present('sheet')
