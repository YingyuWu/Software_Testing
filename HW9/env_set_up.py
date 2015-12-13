from remote_api import env,cd,run
from private import user, password

env.host_string = '107.170.18.199'
env.user = user
env.password = password

setup = "source .bash_profile;"

def setup_pip3():
    print("Installing pip3.")
    with cd("~"):
        result = run("sudo apt-get -y install python3-pip")
    with cd("~"):
        result = run("pip3 --version")
    print(result)
    print("pip3 is installed")
    assert(result.startswith("pip"))

def setup_git():
    print("Installing git.")
    with cd("~"):
        result = run("sudo apt-get -y install git")
    with cd("~"):
        result = run("git --version")
    print(result)
    print("git is installed")
    assert(result.startswith("git"))

def setup_django():
    print("Installing Django.")
    with cd("~"):
        result = run("sudo pip3 install django")
    with cd("~"):
        result = run("pip3 list | grep Django")
    print(result)
    print("Django installed")
    assert(result.startswith("Django"))

def setup_application():
    print("Installing application")
    with cd("~/wendy_workspace"):
        run("wget https://github.com/hjwp/book-example/archive/chapter_07.zip")
        result = run("sudo apt-get -y install unzip")
        run("unzip chapter_07.zip")
        run("mv book-example-chapter_07 application")
    with cd("~/wendy_workspace/application"):
        run("python3 manage.py migrate")
    print("Application installed")
        
def start_application():
    with cd("~/wendy_workspace/application"):
        result = run("python3 manage.py runserver 127.0.0.1:8000")
        print(result)
        #run(setup + "nohup ps -aux \&")
        pass

def setup_selenium():
    print("Installing Selenium.")
    with cd("~"):
        result = run("sudo pip3 install selenium")
    #with cd("~"):
        #result = run("pip3 list | grep Django")
    print(result)
    print("Selenium installed")
    #assert(result.startswith("Django"))

def setup_firefox():
    print("Installing Firefox.")
    with cd("~"):
        result = run("sudo apt-get -y install firefox")
    with cd("~"):
        result = run("firefox -v")
    assert("Firefox" in result)
    print(result)
    print("Firefox installed")


def setup_Xvfb():
    print("Installing pyvirtualdisplay.")
    with cd("~"):
        result = run("sudo apt-get -y install xvfb")
    with cd("~"):
        result = run("sudo pip3 install pyvirtualdisplay")
    print(result)
    print("pyvirtualdisplay installed")


    
if __name__ == "__main__":
    #setup_pip3()
    #setup_git()
    #setup_django()
    #setup_application()
    #setup_selenium()
    #setup_firefox()
    #function_test()
    setup_Xvfb()
    #start_application()