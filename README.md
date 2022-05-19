# launch_shutdown_tests

## To run, execute : 
```
launch_test test_launch.py
```

## Result
To print what processes are still alive after the test, run : 
```
ps aux --forest | grep -B2 'test'
```

You should see the following 3 processes still active : 
```
\_ python3 test_print.py -shell-true-buffered
\_ python3 test_no_print.py -shell-true-buffered
\_ python3 -u test_no_print.py -shell-true-unbuffered
```
