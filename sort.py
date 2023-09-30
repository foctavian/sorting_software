import os 
import configparser
import shutil
from colorama import Fore, Back, Style

def move_files(path,target, names):
    for filename in os.listdir(path):
        f = os.path.join(path, filename)

        if os.path.isfile(f):
            for pre in names:
                if filename.startswith(pre+'_'):
                    new_target = os.path.join(target, pre,filename)
                    if not os.path.exists(new_target):
                        shutil.move(f,new_target)
                        print(Fore.GREEN+f"Moved {filename} to {target}")
                    else:
                        print(Fore.RED+f"{filename} already exists")


def init_dirs(target, names):
    for name in names:
        path = os.path.join(target, name)
        if not os.path.exists(path):
            os.mkdir(path)
            print(Fore.GREEN+Style.BRIGHT+f"Created {name} directory")
        else:
            print(Fore.RED+f"{name} directory already exists")

def main():
    config_file = configparser.ConfigParser()
    config_file.read("config.ini")
    config = config_file["config"]
    target = config["target_dir"]
    names = config["subjects"].splitlines()
    
    #init dirs
    init_dirs(target, names)
    move_files(config["dir_path"],target, names)

if __name__ == "__main__":
    main()