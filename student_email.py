
import csv, smtplib, ssl

message = """Subject: Your position to move to the next module

Hi {student}, we would like to show you how you perfomance is and ensure you that you will be moving to the
next module. 
Below is your grades from your IPs and attendance:
IP1: {ip1}
IP2: {ip2}
IP3: {ip3}
IP4: {ip4}
Attendance: {attendance}
First recommendation: {firstrecommendation}
Reason(first recommendation):{reason1}
Final recommendation:{finalrecommendation}
Reason(final recommendation): {finalrecommendation}
 """
from_address = "nancytoniw@gmail.com"
password = input("Type your password and press enter: ")

context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(from_address, password)
    with open("students_info.csv") as file:
        reader = csv.reader(file)
        next(reader)
        for student,email,ip1,ip2,ip3,ip4,attendance,firstrecommendation,reason1,finalrecommendation,reasonf in reader: 
            print(f"Sending email to {student}")
            server.sendmail(
                from_address,
                email,
                message.format(student=student,email=email,ip1=ip1,ip2=ip2,ip3=ip3,ip4=ip4,attendance=attendance,firstrecommendation=firstrecommendation,reason1=reason1,finalrecommendation=finalrecommendation,reasonf=reasonf),
               
            )