from codexplore import emailProcess, printMsg

def main():
    emails = ['hieumenbox@gmail.com', 'hieu.nguyen211199@hcmut.edu.vn', 'minhhuongbql@yahoo.com.vn']
    for email in emails:
        username, email_domain = emailProcess(email)
        printMsg(username, email_domain)
if __name__ == "__main__":
    main()