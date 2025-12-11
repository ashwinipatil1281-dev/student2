import sys

# Default values
default_val1 = "Default1"
default_val2 = "Default2"

if len(sys.argv) == 3:
    val1 = sys.argv[1]
    val2 = sys.argv[2]
   
else:
    val1 = default_val1
    val2 = default_val2
   

print(f"Value1: {val1} ({source})")
print(f"Value2: {val2} ({source})")
