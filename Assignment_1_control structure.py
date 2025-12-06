# TASK

# . Create a student grade processor that: 
# . Uses a list of student scores (mix of valid and invalid data)
#  • Uses if-else to classify each score as "Pass" (≥60) or "Fail" (<60) 
# • Skips any negative scores with continue 
# • Prints results for each valid score 
# • Counts total passing and failing students



student_records = [
    {"name": "Alice", "score": 85},
    {"name": "Bob", "score": 150},
    {"name": "Carol", "score": 78},
    {"name": "Dave", "score": -15},
    {"name": "Esther", "score": 92},
    {"name": "John",  "score": 35}, 
]
# print("=== FOR LOOP: Processing all records ===")

# for student in student_records:
#     if student["score"] == "valid":
#         print(f"Processing {student['name']}: Score {student['score']}")
#     else:
#         print(f"Skipping invalid user: {student['name']}")

count_pass = 0
count_fail = 0

print()
for student in student_records:

    if student["score"] < 0:
        continue
    if student["score"] < 60:
        print(f"Name: {student["name"]} | Score: {student["score"]} | Status: Fail")
        count_fail += 1
    else:
        print(f"Name: {student["name"]} | Score: {student["score"]} | Status: Pass")
        count_pass += 1
print(f"total passing student:{count_pass}")
print(f"total failing student:{count_fail}")