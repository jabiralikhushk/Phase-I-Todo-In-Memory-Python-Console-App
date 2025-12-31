import subprocess  
import sys  
  
def run_todo_command(args):  
    "Helper function to run todo app commands."  
    cmd = [sys.executable, "todo_app.py"] + args  
    result = subprocess.run(cmd, capture_output=True, text=True, cwd=".")  
    return result.stdout.strip(), result.stderr.strip(), result.returncode 
  
print("Testing Todo Application Features")  
print("="*40)  
  
# Test 1: Add a task  
print("n1. Testing ADD feature:")  
stdout, stderr, code = run_todo_command(["add", "Buy groceries"])  
print(f"   Command: add 'Buy groceries'")  
print(f"   Output: {stdout}")  
print(f"   Return code: {code}") 
