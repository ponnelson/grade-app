
import streamlit as st

st.write("Student Grade Manager")   

# --------------------------------
# INITIALIZE STUDENT LIST
# --------------------------------

if "students" not in st.session_state:
    st.session_state.students = []


# --------------------------------
# GRADE CALCULATION
# --------------------------------

def calculate_grade(mark):

    if mark >= 90:
        return "A"
    elif mark >= 80:
        return "B"
    elif mark >= 70:
        return "C"
    elif mark >= 60:
        return "D"
    else:
        return "F"





# --------------------------------
# ADD STUDENT FORM
# --------------------------------

with st.form("student_form", clear_on_submit=True):

    col1, col2, col3 = st.columns([2, 1, 1])

    with col1:
        name = st.text_input(
            "Name",
            placeholder="Enter student name"
        )

    with col2:
        mark = st.number_input(
            "Mark",
            min_value=0,
            max_value=100,
            value=0,
            step=1
        )

    with col3:
        st.write("")
        st.write("")
        add_student = st.form_submit_button(
            "Add",
            use_container_width=True
        )

    if add_student:

        if not name.strip():
            st.error("Please enter student name.")

        else:

            student = {
                "Name": name.strip(),
                "Mark": mark,
                "Grade": calculate_grade(mark)
            }

            st.session_state.students.append(student)

            st.success(
                f"{name} added successfully!"
            )



# --------------------------------
# STUDENT RESULTS
# --------------------------------

st.write("Student Results")

students = st.session_state.students

if students:

    # Table headings

    col1, col2, col3 = st.columns([2, 1, 1])

    col1.markdown("**Name**")
    col2.markdown("**Mark**")
    col3.markdown("**Grade**")

     # Display student records

    for student in students:

        col1, col2, col3 = st.columns([2, 1, 1])

        col1.write(student["Name"])
        col2.write(student["Mark"])
        col3.write(student["Grade"])


   
    # --------------------------------
    # CLASS STATISTICS
    # --------------------------------

    marks = [
        student["Mark"]
        for student in students
    ]

    average = sum(marks) / len(marks)

    highest = max(marks)

    lowest = min(marks)

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Average",
        f"{average:.1f}"
    )

    col2.metric(
        "Highest",
        highest
    )

    col3.metric(
        "Lowest",
        lowest
    )


    # --------------------------------
    # CLEAR ALL STUDENTS
    # --------------------------------

    st.divider()

    if st.button("Clear All Students"):

        st.session_state.students = []

        st.rerun()

else:

    st.info("No students added yet.")


