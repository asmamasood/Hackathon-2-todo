import subprocess
import sys
import pytest

def run_cli(*args):
    result = subprocess.run(
        [sys.executable, "-m", "todo"] + list(args),
        capture_output=True,
        text=True,
        cwd="src"
    )
    return result

def test_cli_add_and_list():
    # Since we can't easily reset the singleton between subprocess calls,
    # we just check if it works. Note: multiple tests might interfere if run in parallel.
    run_cli("add", "CLI Task", "-d", "CLI Description")
    result = run_cli("list")
    assert "CLI Task" in result.stdout
    assert "CLI Description" in result.stdout

def test_cli_done():
    run_cli("add", "Task for Done")
    # Assuming it got an ID, let's list to find it
    list_res = run_cli("list")
    # Find ID of "Task for Done"
    for line in list_res.stdout.splitlines():
        if "Task for Done" in line:
            task_id = line.split()[0]
            run_cli("done", task_id)
            list_res_after = run_cli("list")
            assert "✔" in list_res_after.stdout
            break

def test_cli_rm():
    run_cli("add", "Task for RM")
    list_res = run_cli("list")
    for line in list_res.stdout.splitlines():
        if "Task for RM" in line:
            task_id = line.split()[0]
            run_cli("rm", task_id)
            list_res_after = run_cli("list")
            assert "Task for RM" not in list_res_after.stdout
            break
