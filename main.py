def on_forever():
    if not (input.button_is_pressed(Button.B)) and input.pin_is_pressed(TouchPin.P2) and (not (input.pin_is_pressed(TouchPin.P1)) and not (input.pin_is_pressed(TouchPin.P0))):
        pins.analog_write_pin(AnalogPin.P12, 511)
        pins.analog_set_period(AnalogPin.P12, 3610)
    elif not (input.button_is_pressed(Button.B)) and input.pin_is_pressed(TouchPin.P2) and (input.pin_is_pressed(TouchPin.P1) and not (input.pin_is_pressed(TouchPin.P0))):
        pins.analog_write_pin(AnalogPin.P12, 511)
        pins.analog_set_period(AnalogPin.P12, 3412)
    elif not (input.button_is_pressed(Button.B)) and input.pin_is_pressed(TouchPin.P2) and (input.pin_is_pressed(TouchPin.P1) and input.pin_is_pressed(TouchPin.P0)):
        pins.analog_write_pin(AnalogPin.P12, 511)
        pins.analog_set_period(AnalogPin.P12, 3215)
    elif not (input.button_is_pressed(Button.B)) and input.pin_is_pressed(TouchPin.P2) and (not (input.pin_is_pressed(TouchPin.P1)) and input.pin_is_pressed(TouchPin.P0)):
        pins.analog_write_pin(AnalogPin.P12, 511)
        pins.analog_set_period(AnalogPin.P12, 3040)
    elif not (input.button_is_pressed(Button.B)) and not (input.pin_is_pressed(TouchPin.P2)) and (input.pin_is_pressed(TouchPin.P1) and input.pin_is_pressed(TouchPin.P0)):
        pins.analog_write_pin(AnalogPin.P12, 511)
        pins.analog_set_period(AnalogPin.P12, 2915)
    elif not (input.button_is_pressed(Button.B)) and not (input.pin_is_pressed(TouchPin.P2)) and (not (input.pin_is_pressed(TouchPin.P1)) and input.pin_is_pressed(TouchPin.P0)):
        pins.analog_write_pin(AnalogPin.P12, 511)
        pins.analog_set_period(AnalogPin.P12, 2703)
    elif input.button_is_pressed(Button.B) and input.pin_is_pressed(TouchPin.P2) and (not (input.pin_is_pressed(TouchPin.P1)) and not (input.pin_is_pressed(TouchPin.P0))):
        pins.analog_write_pin(AnalogPin.P12, 511)
        pins.analog_set_period(AnalogPin.P12, 2551)
    elif input.button_is_pressed(Button.B) and input.pin_is_pressed(TouchPin.P2) and (input.pin_is_pressed(TouchPin.P1) and not (input.pin_is_pressed(TouchPin.P0))):
        pins.analog_write_pin(AnalogPin.P12, 511)
        pins.analog_set_period(AnalogPin.P12, 2410)
    elif input.button_is_pressed(Button.B) and input.pin_is_pressed(TouchPin.P2) and (input.pin_is_pressed(TouchPin.P1) and input.pin_is_pressed(TouchPin.P0)):
        pins.analog_write_pin(AnalogPin.P12, 511)
        pins.analog_set_period(AnalogPin.P12, 2273)
    elif input.button_is_pressed(Button.B) and input.pin_is_pressed(TouchPin.P2) and (not (input.pin_is_pressed(TouchPin.P1)) and input.pin_is_pressed(TouchPin.P0)):
        pins.analog_write_pin(AnalogPin.P12, 511)
        pins.analog_set_period(AnalogPin.P12, 2146)
    elif input.button_is_pressed(Button.B) and not (input.pin_is_pressed(TouchPin.P2)) and (input.pin_is_pressed(TouchPin.P1) and input.pin_is_pressed(TouchPin.P0)):
        pins.analog_write_pin(AnalogPin.P12, 511)
        pins.analog_set_period(AnalogPin.P12, 2028)
    elif input.button_is_pressed(Button.B) and not (input.pin_is_pressed(TouchPin.P2)) and (not (input.pin_is_pressed(TouchPin.P1)) and input.pin_is_pressed(TouchPin.P0)):
        pins.analog_write_pin(AnalogPin.P12, 511)
        pins.analog_set_period(AnalogPin.P12, 1912)
    else:
        pins.analog_write_pin(AnalogPin.P12, 511)
        pins.analog_set_period(AnalogPin.P12, 0)
basic.forever(on_forever)
