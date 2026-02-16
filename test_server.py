import sys
from server import execute_command_logic

def test_execution():
    print("Testing command execution...")
    try:
        # Test 1: Simple echo
        output = execute_command_logic("echo 'Hello World'")
        print(f"Output: {output}")
        if "Hello World" in output:
             print("SUCCESS: Command executed and output captured.")
        else:
             print("FAILURE: Output did not contain expected string.")
             sys.exit(1)
             
        # Test 2: Error case (non-existent directory)
        print("\nTesting error case...")
        error_output = execute_command_logic("ls /nonexistent_directory_12345")
        print(f"Error Output: {error_output}")
        if "Exit Code:" in error_output and "No such file or directory" in error_output:
            print("SUCCESS: Error correctly captured.")
        else:
            print("FAILURE: Error execution did not return expected error message.")
            sys.exit(1)

    except Exception as e:
        print(f"Test Failed with exception: {e}")
        sys.exit(1)

if __name__ == "__main__":
    test_execution()
