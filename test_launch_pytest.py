import sys
import time
import unittest

import launch
import launch_pytest
from launch.actions import ExecuteProcess
from launch_ros.actions import Node
from launch_testing.actions import ReadyToTest
import launch_testing.markers
import pytest


@launch_pytest.fixture
def generate_test_description():
    return launch.LaunchDescription(
        [
            Node(
                package="demo_nodes_cpp",
                executable="talker"),
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


@pytest.mark.launch(fixture=generate_test_description, shutdown=True)
def test_something():
    time.sleep(10.0)
    print('END TEST', file=sys.stderr)
