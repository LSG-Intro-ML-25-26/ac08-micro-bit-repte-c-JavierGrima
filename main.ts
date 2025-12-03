radio.onReceivedNumber(function (receivedNumber) {
    dado_oponente = randint(1, 6)
    basic.showNumber(dado_oponente)
    basic.pause(1000)
    if (receivedNumber > dado_oponente) {
        basic.showIcon(IconNames.Happy)
    } else {
        basic.showIcon(IconNames.Sad)
    }
})
input.onButtonPressed(Button.A, function () {
    dado = randint(1, 6)
    basic.showNumber(dado)
    radio.sendNumber(dado)
})
let dado = 0
let dado_oponente = 0
radio.setGroup(1)
