globalVar = 66

if True:
    localVar = 77
    print(f"Global variable is {globalVar}")
    print(f"Local variable is {localVar}")
try:
    print(f"Outside the block: local_var = {local_var}")  
except NameError as e:
    print("NameError:", e)
print(f"Global variable outside if block {globalVar}")