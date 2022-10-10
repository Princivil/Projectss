import re

# Define is_valid_time below:
def is_valid_time(input):
    time = re.compile(r'^\d\d?:\d\d')
    match = time.search(input)
    if match:
        return True
    return False

is_valid_time("10:45")       
is_valid_time("1:23")        
is_valid_time("10.45")       
is_valid_time("1999")        
is_valid_time("145:23")