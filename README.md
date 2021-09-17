# gdb-runner

Tool to automate the execution of gdb with breapoint-based hooks

# Use

- Define a script file containing a `get_events` function that returns a dictionary with breapoints as keys and function as values
- Use `python run-gdb.py -f <scriptfile> -e <gdb executable you want to use>`.

Examples of script files in the directory [_tests_](https://github.com/psiquo/gdb-runner/tree/main/test).
