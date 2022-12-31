# import matplotlib.pyplot as plt
# import numpy as np

# x = np.linspace(0, 20, 100)  # Create a list of evenly-spaced numbers over the range
# plt.plot(x, np.sin(x))       # Plot the sine of each x point
# plt.show()                   # Display the plot

# from threading import Thread
# import threading
# from generateReport import *
import pygetwindow as gw

# generateReport("TC1")
# try:
#     t1 = threading.Thread(target=startRecordScreen, args=("report",)) #startRecordScreen("report", 500)
#     t2 = threading.Thread(target=stopRecordScreen, args=(3,))
#     t1.start()
#     t2.start()
#     t1.join()
#     t2.join()
# except:
#  	print("Error")

print(gw.getActiveWindow())
# notepadWindow = gw.getWindowsWithTitle('Untitled')[0]
# notepadWindow.activate()