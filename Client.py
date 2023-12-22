current_user = {'user_id': ""}


def register_client():
    print("------------------------------------")
    print("           Registration page         ")
    print("welcome please enter your information")
    print("------------------------------------")
    name = input("Please enter your name: ")
    email = input("Please enter your email: ")
    user_id = input("Please enter your user ID: ")
    password = input("Please enter your password: ")

    client_info_list = [name, email, user_id, password]
    try:
        with open("client_users.txt", "r") as file:
            users = [line.strip().split('\t') for line in file.readlines()]
    except FileNotFoundError:
        users = []

    if any(existing_user[2] == user_id or existing_user[1] == email for existing_user in users):
        print("Error: User with the same user ID or email already exists.")
    else:
        users.append(client_info_list)

        with open("client_users.txt", "w") as file:
            for user_info in users:
                file.write('\t'.join(user_info) + '\n')

        print("Registration successful!")


def login_client():
    print("________________________________________________")
    print("| Welcome! Please enter your login information |")
    print("________________________________________________")
    user_id = input("User ID: ")
    password = input("Password: ")

    try:
        with open("client_users.txt", "r") as file:
            users = [line.strip().split('\t') for line in file.readlines()]
    except FileNotFoundError:
        users = []

    if any(existing_user[2] == user_id and existing_user[3] == password for existing_user in users):
        print("Login successful!")
        current_user['user_id'] = user_id
        return True
    else:
        print("Invalid user ID or password. Login failed.")
        return False


def client_menu():
    while True:
        print("______________________________________________________________________________________")
        print("Welcome ", current_user['user_id'], "!")
        choice = input(
            "press 1 if you want to add\npress 2 if you want to remove\npress3 if you want to view list of registered freelance\npress 4 if you want to accept or reject proposal sent by a freelancer\npress 5 to exit\n ______________________________________________________________________________________ \n")
        print("______________________________________________________________________________________")
        if choice == "1":
            add_job()
        elif choice == "2":
            remove_job(input("please enter job id to remove\n"))
        elif choice == "3":
            view_proposal()
        elif choice == "4":
            accept_or_reject_proposal()
        elif choice == "5":
            break
        else:
            print("invalid choice")


def add_job():
    print("Welcome! Client, please add a job:")

    job_id = input("Enter job ID: ")
    title = input("Enter job title: ")
    description = input("Enter job description: ")
    skills_required = input("Enter required skills (comma-separated): ").split(',')

    new_job = [job_id, title, description, skills_required, current_user['user_id']]

    try:
        with open("jobs.txt", 'r') as file:
            jobs = [line.strip().split(',') for line in file]
    except FileNotFoundError:
        jobs = []

    jobs.append(new_job)

    with open("jobs.txt", 'a') as file:
        for job in jobs:
            file.write(','.join(map(str, job)) + '\n')

    print("Job added successfully!")


def remove_job(job_id_to_remove):

    try:
        with open("jobs.txt", 'r') as file:
            jobs = [line.strip().split(',') for line in file]

        if jobs:
            index_to_remove = None
            for i, job in enumerate(jobs):
                if job[0] == job_id_to_remove:
                    index_to_remove = i
                    break

            if index_to_remove is not None:
                removed_job = jobs.pop(index_to_remove)
                print(f"Removed job with ID {job_id_to_remove}: {','.join(removed_job)}")
            else:
                print(f"No job found with ID {job_id_to_remove}")

            with open("jobs.txt", 'w') as file:
                for job in jobs:
                    file.write(','.join(map(str, job)) + '\n')

        else:
            print("No jobs found in the file.")

    except FileNotFoundError:
        print("File not found. No jobs to remove.")


def view_proposal():
    job_post_id = input("enter the job post you need to view their proposals\n")
    needed_proposal =""
    try:
        with open("proposals.txt", 'r') as file:
            proposals = [line.strip().split(',') for line in file]

        if proposals:
            for proposal in enumerate(proposals):
                if proposal[0] == job_post_id:
                    needed_proposal = proposal
                    print(needed_proposal)
            if needed_proposal == "":
                print("no matched job post with this id ", job_post_id)
    except FileNotFoundError:
        print("File not found. No jobs to remove.")


def accept_or_reject_proposal():
    job_post_id = input("Enter job post id for the proposal you want to edit:\n")
    freelancer_id = input("Enter freelancer id for the proposal you want to edit:\n")
    post_status = input("Enter accept in case you want to accept proposal or reject if not :\n")
    try:
        with open("proposals.txt", "r") as file:
            proposals = [line.strip().split(',') for line in file]
            if proposals:
                for proposal in proposals:
                    flag = False
                    if proposal[0] == job_post_id and proposal[1] == freelancer_id:
                        if proposal[-1] == "pending":
                            proposal[-1] = post_status
                            flag = True
                            print(proposal)
                        else:
                            print("this post was already updated before with status:", proposal[-1])
        if flag:
            with open('proposals.txt', 'w') as file:
                for proposal in proposals:
                    file.write(','.join(map(str, proposal)) + '\n')
            print("status updated successfully!")

    except FileNotFoundError:
        print("File not found")