from pynput import keyboard

from mqtt import setup_mqtt, mqtt_message_constructor
from mqtt import baseTopic

buffer = ''


def on_press(key):
    global buffer

    try:
        if key == keyboard.Key.enter:
            if buffer:
                print(f"\n[Scanned] → {buffer}")
                mqtt_con.publish(
                    baseTopic, mqtt_message_constructor(buffer), qos=0)
                buffer = ''
        elif hasattr(key, 'char'):
            buffer += key.char
        elif key == keyboard.Key.space:
            buffer += ' '
    except Exception as e:
        print(f"Error: {e}")


def on_release(key):
    if key == keyboard.Key.esc:
        print("\n[Exiting]")
        return False


# Start listener
def main():
    global mqtt_con
    mqtt_con = setup_mqtt()
    mqtt_con.loop_start()

    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        print("Waiting for scanner input... (Press ESC to quit)")
        listener.join()


if __name__ == "__main__":
    main()
