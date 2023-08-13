import psutil
import os

processID = 1468
current_process = psutil.Process(processID)
children = current_process.children(recursive=True)
absolute_path = psutil.Process(10680).exe()


