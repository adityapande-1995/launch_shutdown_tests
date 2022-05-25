import sys
import time
import unittest

import launch
from launch.actions import ExecuteProcess
from launch_testing.actions import ReadyToTest
import launch_testing.markers
import pytest


@pytest.mark.launch_test
def generate_test_description():
    return launch.LaunchDescription(
        [
            # This process will get killed
            # Includes a print statement with sleep.
            ExecuteProcess(
                cmd=['python3','test_print.py', '-shell-false-buffered'],
                shell=False,
                output='both',
            ),
            # !!! --- This shell=True + buffererd python3 process won't get killed --- !!!!!
            # Includes a print statement with sleep.
            ExecuteProcess(
                cmd=['python3','test_print.py', '-shell-true-buffered'],
                shell=True,
                output='both',
            ),
            # This process will get killed
            # Includes a print statement with sleep.
            ExecuteProcess(
                cmd=['python3', '-u','test_print.py', '-shell-false-unbuffered'],
                shell=False,
                output='both',
            ),
            # This process will get killed
            # Includes a print statement with sleep.
            ExecuteProcess(
                cmd=['python3', '-u','test_print.py', '-shell-true-unbuffered'],
                shell=True,
                output='both',
            ),

            ## Following processes do not print anything.
            ExecuteProcess(
                cmd=['python3','test_no_print.py', '-shell-false-buffered'],
                shell=False,
                output='both',
            ),
            # !!!! ---- This process does not get killed ----- !!!!
            ExecuteProcess(
                cmd=['python3','test_no_print.py', '-shell-true-buffered'],
                shell=True,
                output='both',
            ),
            ExecuteProcess(
                cmd=['python3', '-u','test_no_print.py', '-shell-false-unbuffered'],
                shell=False,
                output='both',
            ),
            # !!!! ---- This process does not get killed ----- !!!!
            ExecuteProcess(
                cmd=['python3', '-u','test_no_print.py', '-shell-true-unbuffered'],
                shell=True,
                output='both',
            ),

            # Checking C++ processes, both of these will get killed
            ExecuteProcess(
                cmd=['./test_cpp_process/myprinter', '-shell-true'],
                shell=True,
                output='both',
            ),
            ExecuteProcess(
                cmd=['./test_cpp_process/myprinter', '-shell-false'],
                shell=False,
                output='both',
            ),

            ReadyToTest(),
        ])


class MyTestFixture(unittest.TestCase):

    def test_something(self):
        time.sleep(10.0)
        print('END TEST', file=sys.stderr)
