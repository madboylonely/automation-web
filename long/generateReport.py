# importing the required packages
import pyautogui
import cv2
import numpy as np
import time
import pygetwindow as gw
import core.GlobalConstants as GlobalConstants

g_stopScreenRecordFlag = False


def generateReport(name):
    # Creating the HTML file
    file_html = open(name + ".html", "w")

    # Adding the input data to the HTML file
    file_html.write('''<html>
    <head>
        <title>''' + GlobalConstants.g_reportRawData[0].desc + '''</title>
    <style>
        h1 {text-align: center}
        table, th, td {border: solid 1px black;}
        table {width:100%}
        .pass {background: green; text-align: center}
        .fail {background: red; text-align: center}
    </style>
    </head> 
        <body>
            <h1>''' + GlobalConstants.g_reportRawData[0].desc + '''</h1>   
            
            <table>
                <tr>
                    <th>Description</th>    	
                    <th>Result</th>
                </tr>
                '''
                + str(handleRawReportData()) + 
                '''</table></body></html>''')

    # Saving the data into the HTML file
    file_html.close()

    # Reset global raw data
    GlobalConstants.g_reportRawData = []


def handleRawReportData():
    result = ''''''
    for obj in GlobalConstants.g_reportRawData:
        if obj.desc == GlobalConstants.g_reportRawData[0].desc:
            continue
        else:
            if obj.status:
                result += '''<tr><td>''' + obj.desc + '''</td><td class="pass">PASS</td></tr>'''
            else:
                result +='''<tr><td>''' + obj.desc + '''</td><td class="fail">FAIL</td></tr>'''
    
    return result


def startRecordScreen(name):
    # Specify resolution
    resolution = (1920, 1080)

    # Specify video codec
    codec = cv2.VideoWriter_fourcc(*"XVID")

    # Specify name of Output file
    filename = name + ".avi"

    # Specify frames rate. We can choose any
    # value and experiment with it
    fps = 60.0

    # Creating a VideoWriter object
    out = cv2.VideoWriter(filename, codec, fps, resolution)

    # Create an Empty window
    cv2.namedWindow("Live", cv2.WINDOW_NORMAL)

    # Resize this window
    cv2.resizeWindow("Live", 480, 270)

    while True:
        # Take screenshot using PyAutoGUI
        img = pyautogui.screenshot()

        # Convert the screenshot to a numpy array
        frame = np.array(img)

        # Convert it from BGR(Blue, Green, Red) to
        # RGB(Red, Green, Blue)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Write it to the output file
        out.write(frame)

        # Optional: Display the recording screen
        cv2.imshow('Live', frame)

        # Stop recording when we press 'q'
        if cv2.waitKey(1) == ord('q'):
            break

    # Release the Video writer
    out.release()

    # Destroy all windows
    cv2.destroyAllWindows()


def stopRecordScreen(timeStopRecord):
    time.sleep(timeStopRecord)
    recordWindow = gw.getWindowsWithTitle('Live')[0]
    try:
        recordWindow.activate()
    except:
        recordWindow.minimize() 
        recordWindow.maximize() 

    print(gw.getActiveWindow())
    time.sleep(5)
    pyautogui.press('q')
    # notepadWindow = gw.getWindowsWithTitle('Untitled')[0]
    # notepadWindow.activate()
