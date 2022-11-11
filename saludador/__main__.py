import sys
from termcolor import colored

def main(args=None):
    print("Hola, mundo python, [", colored('paquetes distribuibles', 'yellow'), "]")	
    if args is None:
        args = sys.argv[1:]
    
    if len(args) > 0:
        print(" -> argumentos por revisar!")


if __name__ == "__main__":
    exit(main())
