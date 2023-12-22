current_user = {'user_id': ""}


def register_freelancer():
    print("------------------------------------")
    print("           Registration page         ")
    print("welcome please enter your information")
    print("------------------------------------")
    name = input("Please enter your name: ")
    number = input("Please enter your phone number: ")
    email = input("Please enter your email: ")
    national = input("Please enter your national ID: ")
    user_id = input("Please enter your user ID: ")
    password = input("Please enter your password: ")

    user_info_list = [name, number, email, national, user_id, password]

    try:
        with open("freelancer_users.txt", "r") as file:
            users = [line.strip().split('\t') for line in file.readlines()]
    except FileNotFoundError:
        users = []

    # Check if there are existing users with the same user_id or email
    if any(existing_user[4] == user_id or existing_user[2] == email or existing_user[1] == number for existing_user in
           users):
        print("Error: User with the same user ID or email or number already exists.")
    else:
        users.append(user_info_list)

        with open("freelancer_users.txt", "w") as file:
            for user_info in users:
                file.write('\t'.join(user_info) + '\n')

        print("Registration successful!")


def login_freelancer():
    print("________________________________________________")
    print("| Welcome! Please enter your login information |")
    print("________________________________________________")
    user_id = input("User ID: ")
    password = input("Password: ")

    try:
        with open("freelancer_users.txt", "r") as file:
            users = [line.strip().split('\t') for line in file.readlines()]
    except FileNotFoundError:
        users = []

    # Check if there is a user with the provided user_id and password
    if any(existing_user[4] == user_id and existing_user[5] == password for existing_user in users):
        current_user['user_id'] = user_id
        return True
    else:
        print("Invalid user ID or password. Login failed.")
        return False


def freelancer_menu():
    while True:
        print("______________________________________________________________________________________")
        print("Welcome ", current_user['user_id'], "!")
        x = (input(
            f"welcome you can choose from the following options\n1) Press 1 if you want to see all job posts list\n2) Press 2 to search in jobs posts by Title\n3) press 3 to send a proposal\n4) press 4 to check if your proposal has been accepted or not\n5) press 5 to exit this page\n ______________________________________________________________________________________ \n"))
        print("______________________________________________________________________________________")
        if x == "1":
            view_all_job_posts()
        elif x == "2":
            search_job_titles()
        elif x == "3":
            send_proposal()
        elif x == "4":
            check_proposal_status()
        elif x == "5":
            break
        else:
            print("invalid choice please choose again\n ")


def view_all_job_posts():
    try:
        with open("jobs.txt",'r') as job_file:
            jobs = [line.strip().split(',') for line in job_file]

            if jobs:
               for job in jobs:
                   print(job)
    except FileNotFoundError:
        print("File not found.")


def send_proposal():
    job_id = input("please enter the job id for the the post you want to send proposal to \n")
    skills_you_have = input("Enter skills you have (comma-separated): ").split(',')
    proposal_initial_status = "pending"

    # Create a list for the new job
    proposal = [job_id, current_user['user_id'], skills_you_have,proposal_initial_status]

    try:
        with open("proposals.txt", 'r') as file:
            proposals = [line.strip().split(',') for line in file]
    except FileNotFoundError:
        proposals = []
    proposals.append(proposal)

    # Write the updated list of jobs back to the file
    with open("proposals.txt", 'a') as file:
        for proposal in proposals:
            file.write(','.join(map(str, proposal)) + '\n')

    print("Proposal sent successfully!")


def search_job_titles():
    job_title = input("Enter job title you want to search with ")
    needed_job = ""
    try:
        with open("jobs.txt", 'r') as file:
            jobs = [line.strip().split(',') for line in file]

        if jobs:
            for job in enumerate(jobs):
                if job_title in job[1]:
                    needed_job = job
                    print(needed_job)
            if needed_job == "":
                print("no matched job post with title ", job_title)
    except FileNotFoundError:
        print("File not found. No jobs to remove.")


def check_proposal_status():
    job_post_id = input("Enter job post ID you want to check about:")
    try:
        with open("proposals.txt","r") as file:
            proposals = [line.strip().split(',') for line in file]
        if proposals:
            for proposal in proposals:
                if job_post_id == proposal[0] and current_user['user_id'] == proposal[1]:
                    if proposal[-1] == "pending":
                        print("your proposal is still pending")
                    elif proposal[-1] == "accept":
                        print(" congratulations! your offer has been accepted ^-^ ")
                    else:
                        print("sorry your offer has been rejected")
    except FileNotFoundError:
        print("File not found")
