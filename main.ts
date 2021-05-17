basic.showIcon(IconNames.EigthNote)
pins.setAudioPin(AnalogPin.P12)
music.setVolume(200)
music.setBuiltInSpeakerEnabled(false)
basic.forever(function () {
    if (!(input.buttonIsPressed(Button.B)) && input.pinIsPressed(TouchPin.P2) && (!(input.pinIsPressed(TouchPin.P1)) && !(input.pinIsPressed(TouchPin.P0)))) {
        music.ringTone(262)
    } else if (!(input.buttonIsPressed(Button.B)) && input.pinIsPressed(TouchPin.P2) && (input.pinIsPressed(TouchPin.P1) && !(input.pinIsPressed(TouchPin.P0)))) {
        music.ringTone(277)
    } else if (!(input.buttonIsPressed(Button.B)) && input.pinIsPressed(TouchPin.P2) && (input.pinIsPressed(TouchPin.P1) && input.pinIsPressed(TouchPin.P0))) {
        music.ringTone(294)
    } else if (!(input.buttonIsPressed(Button.B)) && input.pinIsPressed(TouchPin.P2) && (!(input.pinIsPressed(TouchPin.P1)) && input.pinIsPressed(TouchPin.P0))) {
        music.ringTone(311)
    } else if (!(input.buttonIsPressed(Button.B)) && !(input.pinIsPressed(TouchPin.P2)) && (input.pinIsPressed(TouchPin.P1) && input.pinIsPressed(TouchPin.P0))) {
        music.ringTone(330)
    } else if (!(input.buttonIsPressed(Button.B)) && !(input.pinIsPressed(TouchPin.P2)) && (!(input.pinIsPressed(TouchPin.P1)) && input.pinIsPressed(TouchPin.P0))) {
        music.ringTone(349)
    } else if (input.buttonIsPressed(Button.B) && input.pinIsPressed(TouchPin.P2) && (!(input.pinIsPressed(TouchPin.P1)) && !(input.pinIsPressed(TouchPin.P0)))) {
        music.ringTone(370)
    } else if (input.buttonIsPressed(Button.B) && input.pinIsPressed(TouchPin.P2) && (input.pinIsPressed(TouchPin.P1) && !(input.pinIsPressed(TouchPin.P0)))) {
        music.ringTone(392)
    } else if (input.buttonIsPressed(Button.B) && input.pinIsPressed(TouchPin.P2) && (input.pinIsPressed(TouchPin.P1) && input.pinIsPressed(TouchPin.P0))) {
        music.ringTone(415)
    } else if (input.buttonIsPressed(Button.B) && input.pinIsPressed(TouchPin.P2) && (!(input.pinIsPressed(TouchPin.P1)) && input.pinIsPressed(TouchPin.P0))) {
        music.ringTone(440)
    } else if (input.buttonIsPressed(Button.B) && !(input.pinIsPressed(TouchPin.P2)) && (input.pinIsPressed(TouchPin.P1) && input.pinIsPressed(TouchPin.P0))) {
        music.ringTone(466)
    } else if (input.buttonIsPressed(Button.B) && !(input.pinIsPressed(TouchPin.P2)) && (!(input.pinIsPressed(TouchPin.P1)) && input.pinIsPressed(TouchPin.P0))) {
        music.ringTone(494)
    } else {
        music.stopAllSounds()
    }
})
