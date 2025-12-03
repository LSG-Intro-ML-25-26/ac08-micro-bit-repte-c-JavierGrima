def on_received_number(receivedNumber):
    global dado_oponente
    dado_oponente = randint(1, 6)
    basic.show_number(dado_oponente)
    basic.pause(1000)
    if receivedNumber > dado_oponente:
        basic.show_icon(IconNames.HAPPY)
    else:
        basic.show_icon(IconNames.SAD)
radio.on_received_number(on_received_number)

def on_button_pressed_a():
    global dado
    dado = randint(1, 6)
    basic.show_number(dado)
    radio.send_number(dado)
input.on_button_pressed(Button.A, on_button_pressed_a)

dado = 0
dado_oponente = 0
radio.set_group(1)