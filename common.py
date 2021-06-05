"""Common file for functions that will be used across the project"""

import os

PROJECT_NAME = "League Tier List"

def request_command(cmd):
    print(f"{PROJECT_NAME} would like to execute command: {cmd}\n(Y/N)")
    if(input().lower().startswith('y')):
        os.system(cmd)
    else:
        print("Skipping Command.")

    return


def install_dependencies(verbose=False):
    if verbose:
        print("-- INSTALLING DEPENDENCIES --")

    from sys import platform
    if platform in ["linux", "linux2", "darwin"]:
        request_command('sudo -S apt install python3-pip')
        request_command('sudo -S apt install unzip && sudo apt install curl')

    with open('dependencies.txt') as dep_file:
        for line in dep_file:
            print(f'pip install {line}')
            os.system(f'pip install {line}')

    init_file = open(".init_flag.txt", "w+")
    init_file.write("File to flag first startup of python project.")
    init_file.close()

    return


def sys_echo(cmd):
    # Execute command and print it to console

    print(cmd)
    os.system(cmd)


def update_chrome_driver():
    from sys import platform

    if platform in ["linux", "linux2"]:
        print("Updating for linux...")
        """os.system('curl -o chromedriver.zip https://chromedriver.storage.googleapis.com/91.0.4472.19/chromedriver_linux64.zip  && \\ '
                  'mv chromedriver.zip drivers && cd drivers && \\'
                  'unzip chromedriver.zip && mv chromedriver chromedriver.exe && cd ..')
        """
        sys_echo('curl -o chromedriver.zip https://chromedriver.storage.googleapis.com/91.0.4472.19/chromedriver_linux64.zip')
        sys_echo('unzip chromedriver.zip')
        sys_echo('mv chromedriver drivers/chromedriver.exe')
        sys_echo('rm chromedriver.zip')

    return
