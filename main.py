from generate_unique_random_numbers import generate_unique_random_numbers
from app_requests_queue import AppRequestsQueue
from palindrome_check import palindrome_check
from symmetrical_dividers_check import symmetrical_dividers_check

# Task 1
print("Task 1")
list = generate_unique_random_numbers(5)
app_requests = AppRequestsQueue()

for data in list:
    request = app_requests.generate_request(data)
    print(f"Generate request {request}")

while not app_requests.is_empty():
    request = app_requests.process_request()
    print(f"Process request {request}")

# Task 2
print("\nTask 2")
words = ["t", "test", "racecar",  "level", "deified",
         "Madam, in Eden, I'm Adam", "Step on no pets"]
for w in words:
    print(f"<{w}> Result: ", palindrome_check(w))


# Task 3
print("\nTask 3")
lines = ["( ){[ 1 ]( 1 + 3 )( ){ }}", "( 23 ( 2 - 3);", "( 11 }", "{(})", "(){}[]()"]
for line in lines:
    print(f"<{line}> Result: ", symmetrical_dividers_check(line))
