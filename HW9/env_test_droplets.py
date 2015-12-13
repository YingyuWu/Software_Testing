from remote_api import env,cd,run
from private import user, password

env.host_string = '107.170.18.199'
env.user = user
env.password = password

setup = "source .bash_profile;"

import unittest

class Test_000_Environment(unittest.TestCase):

    def test_000_login(self):
        "Server is present and we can log in."
        with cd("~/wendy_login"):
            result = run("whoami")
        self.assertTrue(env.user in result)

    def test_001_python3(self):
        "Python 3 is installed."
        with cd("~"):
            result = run("python3 --version")
        self.assertTrue("Python 3" in result)

    def test_002_pip3(self):
        "Pip3 is installed."
        with cd("~"):
            result = run("pip3 --version")
        self.assertTrue(result.startswith("pip"))
        
    def test_003_git(self):
        "git is installed."
        with cd("~"):
            result = run("git --version")
        self.assertTrue(result.startswith("git"))
        
    def test_004_django(self):
        "Django is installed."
        with cd("~"):
            result = run("pip3 list | grep Django")
        self.assertTrue(result.startswith("Django"))
    
    def test_005_app_installed(self):
        "Test that the application directory and software are present"
        with cd("~/wendy_workspace"):
            result = run("ls -l")
        self.assertTrue("application" in result)
        with cd("~/wendy_workspace/application"):
            result = run("ls -l")
        self.assertTrue("manage.py" in result)
        self.assertTrue("lists" in result)

    def test_006_selenium_installed(self):
        "Test Selenium webdriver is installed"
        with cd("~/wendy_workspace"):
            result = run("ls -l")
        with cd("~/wendy_workspace/application/functional_tests"):
            run("ls -l")
            result = run("python3.5 tests.py")
        print(result)

    def test_007_django(self):
        "Firefox is installed."
        with cd("~"):
            result = run("firefox -v")
        self.assertTrue("Firefox" in result)


    def test_008_function_test(self):
        "Function Test."
    with cd("~/wendy_workspace/application/"):
        result = run("python3.5 manage.py test functional_tests")
    print(result)
        
if __name__ == "__main__":
    unittest.main(verbosity=2)