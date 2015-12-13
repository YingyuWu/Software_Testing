#
# remote_api.py
#
# Contains calls to allow command execution on remote (and local) machines,
# using the paramiko library to create an SSH connection.
#
# Greg DeLozier, 11/17/2016
# gdelozie@kent.edu
# 

import paramiko

from contextlib import contextmanager

# ---- Environment ----
class Environment(object):
    host_string = ""
    host_port = 22    
    user = ""
    password = None
    working_directory = list()

env = Environment()

@contextmanager
def cd(path):
    env.working_directory.append(path)
    yield
    env.working_directory.pop()
    
def run(command):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(env.host_string, env.host_port, 
                username = env.user,
                password = env.password)
    results = None
    try:
        if env.working_directory:
            command = "cd {} && {}".format(
                " && cd ".join(env.working_directory), command)
        stdin, stdout, stderr = ssh.exec_command(command)
        stdout = [line.decode('utf-8').strip() 
                    for line in stdout.read().splitlines()]
        stderr = ["ERROR:" + line.decode('utf-8').strip() 
                    for line in stderr.read().splitlines()]
        if stderr:
            stdout = stdout + "------" + stderr
        result = "\n".join(stdout)
    finally:
        ssh.close()
        return result

# ---- Tests ----

import unittest
import private

class Test_Remote_API(unittest.TestCase):

    def test_env(self):
        env.host_string = "107.170.18.199"
        env.host_port = 22
        env.user = "root"
        env.password = "wyu6328248"
        self.assertEqual(env.host_string,"107.170.18.199")
        self.assertEqual(env.user,"root")
        self.assertEqual(env.password,"wyu6328248")
        self.assertTrue(type(env.working_directory) is list)
        self.assertEqual(len(env.working_directory),0)

    def test_cd(self):
        self.assertTrue(type(env.working_directory) is list)
        self.assertEqual(len(env.working_directory),0)
        with cd("~"):
            self.assertEqual(len(env.working_directory),1)
            self.assertTrue("~" in env.working_directory)
            with cd("foobar"):
                self.assertEqual(len(env.working_directory),2)
                self.assertTrue("foobar" in env.working_directory)
            self.assertEqual(len(env.working_directory),1)
            self.assertTrue("~" in env.working_directory)
        self.assertEqual(len(env.working_directory),0)
     
    def test_run(self):
        env.host_string = "107.170.18.199"
        env.user = private.user
        env.password = private.password
        results = run("ls")
        self.assertTrue(type(results) is str)
        self.assertTrue("sites" in results.split("\n"))               

if __name__ == "__main__":
    unittest.main()