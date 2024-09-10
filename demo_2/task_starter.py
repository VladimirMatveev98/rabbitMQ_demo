import os

commands = ["python new_task.py First message.",
            "python new_task.py Second message..",
            "python new_task.py Third message...",
            "python new_task.py Fourth message....",
            "python new_task.py Fifth message....."]

for command in commands:
    os.system(command)
