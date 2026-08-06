# CS 1101: Programming Fundamentals - Unit 7 Assignment
# Scenario: University Workshop Feedback Manager

# ==========================================
# Question 1: String Manipulation
# ==========================================
raw_feedback = " THE SPEAKER WAS GREAT but THE ROOM WAS COLD "

# Step a: Clean leading/trailing spaces and lowercase
cleaned_step_a = raw_feedback.strip().lower()

# Step b: Replace "speaker" with "presenter" and remove extra internal spaces
replaced_text = cleaned_step_a.replace("speaker", "presenter")
cleaned_step_b = " ".join(replaced_text.split())

# Step c: Title case and format output
final_cleaned_feedback = cleaned_step_b.title()
print(f"Cleaned Feedback (Formatted): {final_cleaned_feedback}\n")

# ==========================================
# Question 2: File I/O Operations
# ==========================================
feedback_list = [
    final_cleaned_feedback,
    "The Presentation Was Informative And Engaging.",
    "The Session Started On Time And Was Well Organized."
]

# Step a: Write feedback list to feedback.txt
with open("feedback.txt", "w") as file:
    for item in feedback_list:
        file.write(item + "\n")

# Step b: Read and print all lines
print("--- Current Feedback List ---")
with open("feedback.txt", "r") as file:
    for line in file:
        print(line.strip())

# Step c: Append additional feedback and print updated list
additional_feedback = "The Visual Slides Were Exceptional And Clear."
with open("feedback.txt", "a") as file:
    file.write(additional_feedback + "\n")

print("\n--- Updated Feedback List ---")
with open("feedback.txt", "r") as file:
    for line in file:
        print(line.strip())

# ==========================================
# Question 3: Structured Exception Handling
# ==========================================
print("\n--- Safely Reading Feedback File ---")
filename = "feedback.txt"

try:
    with open(filename, "r") as file:
        contents = file.readlines()
        for line in contents:
            print(line.strip())
except FileNotFoundError:
    print("File not found. Please create feedback.txt first.")
except PermissionError:
    print("Permission denied. Close the file and try again.")
finally:
    print("Operation completed.")

# ==========================================
# Question 4: Analysis & Summary Report
# ==========================================
target_word = "great"
total_feedback_count = 0
great_mention_count = 0

# Step a: Count total feedback and mentions of "great"
with open("feedback.txt", "r") as file:
    for line in file:
        total_feedback_count += 1
        if target_word in line.lower():
            great_mention_count += 1

# Step b: Write summary to summary.txt
with open("summary.txt", "w") as summary_file:
    summary_file.write("=== Workshop Feedback Summary ===\n")
    summary_file.write(f"Total Feedback: {total_feedback_count}\n")
    summary_file.write(f"Mentions of 'Great': {great_mention_count}\n")

# Step c: Console output using f-strings
print("\n=== Console Output Summary ===")
print("=== Workshop Feedback Summary ===")
print(f"Total Feedback: {total_feedback_count}")
print(f"Mentions of 'Great': {great_mention_count}")
