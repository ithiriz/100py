#import slowloris.py 
import subprocess
i = input('Enter the website name: ' )
j = input("Enter the port NUmber: ")
subprocess.call(["python3","slowloris.py",(i),("-s"),(j)],python3=True) 
