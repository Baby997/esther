def process_student_record(student_dict):
      
    try:
        # Validate that all required fields are present
        required_fields = ['name', 'score', 'attendance']

        if 'name' not in student_dict:
            raise KeyError("Missing required field: 'name'")
        if 'score' not in student_dict:
            raise KeyError("Missing required field: 'score'")
        if 'attendance' not in student_dict:
            raise KeyError("Missing required field: 'attendance'")
        
        # Convert and validate the score
        try:
            score = int(student_dict['score'])
        except ValueError:
            raise ValueError(f"Score must be convertible to integer, got: {student_dict['score']}")
        
        if not (0 <= score <= 100):
            raise ValueError(f"Score must be between 0 and 100, got: {score}")
        
        # Convert and validate the attendance
        try:
            attendance = float(student_dict['attendance'])
        except ValueError:
            raise ValueError(f"Attendance must be convertible to float, got: {student_dict['attendance']}")
        
        if not (0 <= attendance <= 100):
            raise ValueError(f"Attendance must be between 0 and 100, got: {attendance}")
        
        # Calculate the final grade using the given formula
        final_grade = score * 0.7 + attendance * 0.3
        
        return {
            'name': student_dict['name'],
            'score': score,
            'attendance': attendance,
            'final_grade': round(final_grade, 2)
        }
    
    except (KeyError, ValueError) as e:
        # Re-raise the exception to propagate the error
        raise e
    
    finally:
        # This block runs regardless of whether an error occurred
        print("Processing completed for record")


def process_class_records(student_list):
    """
    Processes multiple student records and tracks successes and failures.
    
    Args:
        student_list: List of student record dictionaries
    
    Returns:
        Summary dictionary with processing statistics
    """
    successful_records = []
    failed_records = []
    errors = []
    
    for idx, student in enumerate(student_list):
        try:
            # Attempt to process each student record
            processed = process_student_record(student)
            successful_records.append(processed)
        except (KeyError, ValueError) as e:
            # Handle any errors during processing
            error_msg = f"Record {idx} ({student.get('name', 'Unknown')}): {str(e)}"
            failed_records.append(student)
            errors.append(error_msg)
    
    # Return a summary of the processing results
    return {
        'total_records': len(student_list),
        'successful_records': len(successful_records),
        'failed_records': len(failed_records),
        'successful_students': successful_records,
        'errors': errors
    }


def calculate_class_average(grades):
    """
    Calculates the average of a list of grades with error handling.
    
    Args:
        grades: List of numeric grades
    
    Returns:
        Average grade or None if an error occurs
    """
    try:
        # Check if the list is empty
        if len(grades) == 0:
            raise ZeroDivisionError("Cannot calculate average of empty list")
        
        # Calculate the average
        average = sum(grades) / len(grades)
    
    except ZeroDivisionError as e:
        # Handle empty list error
        print(f"Error: {e}")
        return None
    
    except TypeError as e:
        # Handle non-numeric values in the list
        print(f"Error: Non-numeric value in grades list - {e}")
        return None
    
    else:
        # This block runs only if no exceptions occurred
        print("Calculation successful")
        return round(average, 2)
    
    finally:
        # This block always runs
        print("Average calculation completed")


def grade_with_division(total_score, num_assignments):
    """
    Calculates average score per assignment with nested error handling.
    
    Args:
        total_score: Total score across all assignments
        num_assignments: Number of assignments
    
    Returns:
        Average score per assignment
    """
    try:
        # Validate that total_score is not negative
        if total_score < 0:
            raise ValueError("Total score cannot be negative")
        
        try:
            # Attempt to calculate the average
            average = total_score / num_assignments
        
        except ZeroDivisionError:
            # Handle division by zero
            print("Error: Cannot divide by zero - no assignments provided")
            return None
        
        except TypeError:
            # Handle invalid data types
            print("Error: Invalid data types for calculation")
            return None
        
        else:
            # This block runs only if the calculation was successful
            print("Division calculation successful")
            return round(average, 2)
    
    finally:
        # This block always runs
        print("Division calculation completed")


# Test Cases
if __name__ == "__main__":
    test_students = [
        {'name': 'Alice Johnson', 'score': '85', 'attendance': '90'},
        {'name': 'Bob Smith', 'score': 'ninety', 'attendance': '88'},
        {'name': 'Carol White', 'score': '150', 'attendance': '95'},
        {'score': '75', 'attendance': '80'},  # Missing name
        {'name': 'Dave Brown', 'score': '78', 'attendance': '92.5'},
        {'name': 'Eve Davis', 'score': '92', 'attendance': '-10'}  # Invalid attendance
    ]
    
    print("=" * 60)
    print("BATCH PROCESSING TEST")
    print("=" * 60)
    
    summary = process_class_records(test_students)
    
    print("\n" + "=" * 60)
    print("PROCESSING SUMMARY")
    print("=" * 60)
    print(f"Total Records: {summary['total_records']}")
    print(f"Successful: {summary['successful_records']}")
    print(f"Failed: {summary['failed_records']}")
    
    print("\nSuccessful Records:")
    for student in summary['successful_students']:
        print(f"  {student['name']}: Final Grade = {student['final_grade']}")
    
    print("\nErrors Encountered:")
    for error in summary['errors']:
        print(f"  {error}")
    
    # Extract final grades from successful students
    final_grades = [student['final_grade'] for student in summary['successful_students']]
    
    # Calculate class average
    print("\n" + "=" * 60)
    print("CLASS AVERAGE CALCULATION")
    print("=" * 60)
    average = calculate_class_average(final_grades)
    
    if average is not None:
        print(f"Class Average: {average}")
    else:
        print("Class average could not be calculated.") 