

def main():
    try:
        configuration = open('C:\Users\Usr\Documents\RESPALDO 2022\Innovacion Virtual 2022\CursoPythonEntregables\Modulo 10\Config.txt')
    except FileNotFoundError:
        print("Couldn't find the config.txt file!")


    

if __name__ == '__main__':
    main()        