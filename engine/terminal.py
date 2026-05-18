import time
import sys

def slow_print(text, delay=0.03, color="\033[92m"):
    """Imprime texto como se fosse um terminal de IA antigo."""
    reset = "\033[0m"
    sys.stdout.write(color)
    sys.stdout.flush()
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write(reset + "\n")
    sys.stdout.flush()

def clear_screen():
    print("\033c", end="")

def prompt(text):
    sys.stdout.write("\n\033[92m[USUÁRIO] \033[0m")
    slow_print(text, delay=0.01, color="\033[93m")
    return input("\033[92m> \033[0m")
