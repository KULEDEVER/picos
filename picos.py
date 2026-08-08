import gc
import os
from machine import Pin
def morse_code():
    import time
    from machine import Pin
    spacing = 0.125
    led=Pin("LED", Pin.OUT)
    MORSE = {
        "1": ".----",
        "2": "..---",
        "3": "...--",
        "4": "....-",
        "5": ".....",
        "6": "-....",
        "7": "--...",
        "8": "---..",
        "9": "----.",
        "0": "-----",
        "a": ".-",
        "b": "-...",
        "c": "-.-.",
        "d": "-..",
        "e": ".",
        "f": "..-.",
        "g": "--.",
        "h": "....",
        "i": "..",
        "j": ".---",
        "k": "-.-",
        "l": ".-..",
        "m": "--",
        "n": "-.",
        "o": "---",
        "p": ".--.",
        "q": "--.-",
        "r": ".-.",
        "s": "...",
        "t": "-",
        "u": "..-",
        "v": "...-",
        "w": ".--",
        "x": "-..-",
        "y": "-.--",
        "z": "--..",
        ".": ".-.-.-",
        ",": "--..--",
        "?": "..--..",
        "'": ".----.",
        "!": "-.-.--",
        "/": "-..-.",
        "(": "-.--.",
        ")": "-.--.-",
        "&": ".-...",
        ":": "---...",
        ";": "-.-.-.",
        "=": "-...-",
        "+": ".-.-.",
        "-": "-....-",
        "_": "..--.-",
        '"': ".-..-.",
        "$": "...-..-",
        "@": ".--.-.",
    }
    def dit():
        led.value(1)
        time.sleep(spacing)
        led.value(0)
        time.sleep(spacing)
    def dah():
        led.value(1)
        time.sleep(spacing*3)
        led.value(0)
        time.sleep(spacing*1)
    def pause():
        time.sleep(spacing*2)
    def space():
        time.sleep(spacing*7)
    runmorse=True
    try:
        while runmorse:
            code = input("> ").lower()
            pause()
            for char in code:
                if char == " ":
                    space()
                    continue
                number=MORSE.get(char)
                if not number:
                    continue
                for part in number:
                    if part == ".":
                        dit()
                    elif part == "-":
                        dah()
                pause()
    except:
        runmorse=False
def thanks():
    print("Thank you for using my shell, follow me on github for new side projects and updates at:")
    print("https://github.com/KULEDEVER")
    print("Also, feel free to join my discord for news on side projects at:")
    print("https://discord.gg/65Af5h7rZ")
banner=[
    "Welcome to PICOS v1.0 -- KULEDEVER",
    "Type 'help' to see all available commands",
]
help_banner=[
    "ls: show a list of files and folders in the current directory",
    "mkdir: make a directory",
    "rmdir: remove a directory",
    "clear: clear the screen",
    "cd: change the direrctory",
    "mem: show ram related informtion",
    "morse: a small morse code translator, enter a sentence, word, number or special char and the led blinks in morse code",
    "led on: turn on the onboard led",
    "led off: turn off the oboard led",
    "exit: leave the shell",
    "help: show this list of commands",
    "touch: make a file",
    "cat: view the contents of a specified file",
    "add: add text to a file",
    "erase: delete a file",
]
def print_multi(array):
    for line in array:
        print(line)
print_multi(banner)
run=True
try:
    while run:
        gc.collect()
        directory = os.listdir()
        currentdir = os.getcwd()
        if currentdir == "/":
            command = input("PICOS> ")
        else:
            command=input(f"PICOS{currentdir}> ")
        if command == "ls":
            for dire in directory:
                mode = os.stat(dire)[0]
                if mode == 16384:
                    filetyp = "Folder"
                elif mode == 32768:
                    filetyp = "File"
                print(f"{dire} - {filetyp}")
        elif command == "mkdir":
            newdir=input("DIRECTORY NAME> ")
            os.mkdir(newdir)
        elif command == "rmdir":
            remdir=input("DIRECTORY NAME> ")
            try:
                dirs = os.listdir(remdir)
                if len(dirs) == 0:
                    os.rmdir(remdir)
                else:
                    print("Directory is not empty")
            except:
                print("Specified directory does not exist")
        elif command == "clear":
            print("\x1b[2J\x1b[H", end="")
        elif command == "cd":
            changedir=input("DIRECTORY NAME> ")
            try:
                os.chdir(changedir)
            except:
                pass
        elif command == "mem":
            freemem = gc.mem_free() / 1024
            allocmem = gc.mem_alloc() / 1024
            allmemrough=freemem+allocmem
            print(f"Free: {freemem:.2f}KB")
            print(f"Allocated: {allocmem:.2f}KB")
            print(f"Total: ~{allmemrough:.2f}KB")
        elif command == "morse":
            morse_code()
        elif command == "led on":
            Pin("LED", Pin.OUT).value(1)
        elif command == "led off":
            Pin("LED", Pin.OUT).value(0)
        elif command == "help":
            print_multi(help_banner)
        elif command == "exit":
            thanks()
            run = False
        elif command == "touch":
            filenam = input("FILE NAME> ")
            if "picos.py" in filenam or "main.py" in filenam:
                print(f"Cannot change {filenam}, as it is protected and existent")
            else:
                with open(filenam, "w") as f:
                    pass
        elif command == "cat":
            filenam2 = input("FILE NAME> ")
            with open(filenam2, "r") as f:
                print(f.read())
        elif command == "add":
            filenam3 = input("FILE NAME> ")
            if "picos.py" in filenam3 or "main.py" in filenam3:
                print(f"Cannot change {filenam3}, as it is protected")
            else:
                text2write = input("TEXT TO WRITE> ")
                with open(filenam3, "a") as f:
                    f.write(text2write)
        elif command == "erase":
            filenam4 = input("FILE NAME> ")
            if "picos.py" in filenam4 or "main.py" in filenam4:
                print("Cannot erase current shell/bootloader, if you wish to remove PICOS, open another shell or use the REPL")
            else:
                os.remove(filenam4)
except KeyboardInterrupt:
    thanks()
    print("")
    run=False