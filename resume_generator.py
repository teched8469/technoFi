import os

def generate_html_resume(name, designation, email, phone, linkedIn, skills, summary, working_period, working_designation, working_address, working_summary, study_period, education, education_address, output_file):
    html_content = f"""
    <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Resume - {name}</title>
</head>
<style>
    body{{
        display: flex;
    }}
    #core_details{{
        position: absolute;
        top: 0;
        left: 0;
        /* padding-left: 30px; */
        height: 100%;
        width: 25%;
        background-color: rgb(10, 4, 95);
        color: rgb(199, 4, 62);
        border-right: 5px solid rgb(247, 5, 65);
    }}
    #name_resumer{{
        padding-left: 30px;
        color: rgb(247, 5, 65);
        font-size: 50px;
    }}
    #designation_resumer{{
        padding-left: 30px;
        margin-top: -20px;
        font-size: 30px;
        color: white;
    }}
    #personal_information, #skill_heading{{
        padding-top: 10px;
        padding-bottom: 10px;
        padding-left: 30px;
        background-color: rgb(9, 4, 77);
        color: rgb(247, 5, 65);
        font-size: 25px;
    }}
    #core_details p{{
        padding-left: 30px;
        color: white;
    }}
    #email , #phone_number, #account{{
        margin-bottom: -10px;
        color: rgb(247, 5, 65);
        padding-left: 30px;
        
    }}
    #core_details ul{{
        margin-top: -10px;
        margin-bottom: -10px;
        list-style: none;
        color: white;
        padding-top: 10px;
        margin-left: -10px;
    }}
    #core_details li{{
        color: white;
        padding-top: 10px;
        margin-left: -10px;
    }}
    #experience_details{{
        position: absolute;
        top: 0;
        right: 0;
        height: 100%;
        width: 74.4%;

        /* background-color: black; */
    }}
    #intro{{
        display: flex;
        justify-content: center;
        align-items: center;
        padding-left: 20px;
        padding-right: 20px;
        padding-bottom: 30px;
        margin-left: 20px;
        margin-right: 20px;
        border-bottom: 2px solid rgba(46, 46, 46, 0.432);
        border-radius: 30px;
    }}
    #work_det{{
        display: flex;
        flex-direction: row;
        height: 150px;
    }}
    #years_worked{{
        display: flex;
        align-items: center;
        justify-content: center;
        width: 15%;
        height: 95%;
        background-color: rgb(15, 0, 100);
        color: white;
        border-radius: 10px;
        border: 2px solid rgb(247, 5, 65);
        margin-left: 10px;
        margin-right: 10px;
    }}
    #years_worked_0{{
        display: flex;
        align-items: center;
        justify-content: center;
        width: 15%;
        height: 80%;
        background-color: rgb(15, 0, 100);
        color: white;
        border-radius: 10px;
        border: 2px solid rgb(247, 5, 65);
        margin-left: 10px;
        margin-right: 10px;
    }}
    #working_area{{
        width: 80%;
        height: 100%;
    }}
    #work_heading{{
        margin-left: 30px;
        color: #25003d;
        font-size: 30px;
    }}
    #work_designation{{
        font-size: 25px;
        margin-bottom: -10px;
    }}
    #place_address{{
        color: rgb(49, 49, 49);
        margin-bottom: -10px;
    }}
</style>
<body>
    <div id="core_details">
        <div id="intro_section">
            <h1 id="name_resumer">{name}</h1>
            <h3 id="designation_resumer">{designation}</h3>
        </div>
        <div id="contact_section">
            <h3 id="personal_information">Personal Info</h1>
            <div id="details">
                <h4 id="email">Email</h4>
                <p>{email}</p>
                <h4 id="phone_number">Phone</h4>
                <p>{phone}</p>
                <h4 id="account">LinkedIn</h4>
                <p>{linkedIn}</p>
            </div>
        </div>
        <div id="skills">
            <h3 id="skill_heading">Skills</h3>
            <ul>
                {"".join([f"<li>{skill}</li>" for skill in skills])}
            </ul>
        </div>
    </div>
    <div id="experience_details">
        <div id="self_introduction">
            <p id="intro">{summary}</p>
        </div>
        <div id="work_experience">
            <h2 id="work_heading">Work History</h2>
            <div id="work_det">
                <div id="years_worked">{working_period}</div>
                <div id="working_area">
                    <h3 id="work_designation">{working_designation}</h3>
                    <h4 id="place_address">{working_address}</h4>
                    <p id="about">{working_summary}</p>
                </div>
            </div>
        </div>
        <div id="work_experience">
            <h2 id="work_heading">Education</h2>
            <div id="work_det">
                <div id="years_worked_0">{study_period}</div>
                <div id="working_area">
                    <h3 id="work_designation">{education}</h3>
                    <h4 id="place_address">{education_address}</h4>
                </div>
            </div>
        </div>
    </div>
</body>
</html>
    """

    with open(output_file, 'w') as file:
        file.write(html_content)

def main():
    # User inputs for the resume
    name = input("Enter your name: ")
    designation = input("Enter your current designation: ")
    email = input("Enter your email: ")
    phone = input("Enter your phone: ")
    linkedIn = input("Enter your linkedIn Account: ")

    print("Enter your skills (one entry per line). Type 'done' when finished:")
    skill = []
    while True:
        entry = input()
        if entry.lower() == 'done':
            break
        skill.append(entry)
        
    # introduction section
    summary = input("Enter a brief summary about yourself: ")

    # working experience section 
    working_period = input("Enter your working period: ")
    working_designation = input("Enter your working designation in this period: ")
    working_address = input("Enter address of your working area: ")
    working_summary = input("Give brief about your working experience: ")

    # education section 
    study_period = input("Enter your education period: ")
    education = input("Enter your institute name: ")
    education_address = input("Enter address of your institute: ")

    
    # Define output file name
    output_file = "resume.html"
    
    # Generate the resume
    generate_html_resume(name, designation, email, phone, linkedIn, skill, summary, working_period, working_designation, working_address, working_summary, study_period, education, education_address, output_file)
    
    print(f"Resume has been generated and saved to {output_file}")

if __name__ == "__main__":
    main()
