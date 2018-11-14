from tkinter import *
from PIL import Image
from PIL import ImageTk
import videostream

# begin TitanCardScannerApp()
class TitanCardScannerApp():
    # the following method initializes the main app window and connects to the camera and displays the video feed
    def __init__(self):
        # create a main window called "TitanCard Scanner" with dimensions 500 x 410
        self.AppWindow = Tk()
        self.AppWindow.title("TitanCard Scanner")
        self.AppWindow.geometry('500x410')
        self.AppWindow.wm_protocol("WM_DELETE_WINDOW", self.__onCloseWindow__)

        # create a container in the main window for the video feed to be placed in
        self.VideoCanvas = Canvas(self.AppWindow, width=500, height=300, highlightthickness=0, relief='ridge')
        self.VideoCanvas.grid(row=1, column=1)

        # create a container to hold student information
        self.InfoCanvas = Canvas(self.AppWindow, width=20, height=5, highlightthickness=0, relief='ridge')
        self.InfoCanvas.grid(row=2, column=1)

        # create a container to hold name label and input field
        self.NameCanvas = Canvas(self.InfoCanvas, width=20, height=5, highlightthickness=0, relief='ridge')
        self.NameCanvas.grid(row=1, column=1)
        
        self.FirstNameLabel = Label(self.NameCanvas, text="Name")
        self.FirstNameLabel.grid(row=1, column=1)

        self.FirstNameEntryView = Entry(self.NameCanvas, width=20)
        self.FirstNameEntryView.grid(row=2, column=1)

        # create a container to hold id card label and input field
        self.TitanCardCanvas = Canvas(self.InfoCanvas, width=20, height=5, highlightthickness=0, relief='ridge')
        self.TitanCardCanvas.grid(row=1, column=2)
        
        self.TitanCardLabel = Label(self.TitanCardCanvas, text="CWID")
        self.TitanCardLabel.grid(row=1, column=1)

        self.TitanCardEntryView = Entry(self.TitanCardCanvas, width=10)
        self.TitanCardEntryView.grid(row=2, column=1)

        # create a container to hold email label and input field
        self.EmailCanvas = Canvas(self.InfoCanvas, width=20, height=5, highlightthickness=0, relief='ridge')
        self.EmailCanvas.grid(row=1, column=3)
        
        self.EmailLabel = Label(self.EmailCanvas, text="Email")
        self.EmailLabel.grid(row=1, column=1)

        self.EmailLabelEntryView = Entry(self.EmailCanvas, width=20)
        self.EmailLabelEntryView.grid(row=2, column=1)

        # create a container to hold buttons
        self.ButtonCanvas = Canvas(self.InfoCanvas, width=20, height=5, highlightthickness=0, relief='ridge')
        self.ButtonCanvas.grid(row=3, column=2)

        self.SignInButton = Button(self.ButtonCanvas, text='Sign In', command=self.__onSignInButtonClicked__)
        self.SignInButton.grid(row=1, column=1)

        self.ClearButton = Button(self.ButtonCanvas, text='Clear', command=self.__onClearButtonClicked__)
        self.ClearButton.grid(row=2, column=1)
        
        # create variables that captures the video stream object and camera frames and display video
        self.CameraFrame = None
        self.VideoStream = videostream.videostream(0)
        self.displayVideo()

        # start the application
        self.AppWindow.mainloop()
    
    # the following method displays the video obtained from the video stream object
    # it is called continuously every 15 milliseconds
    def displayVideo(self):
        ok, self.CameraFrame = self.VideoStream.getFrame()

        if ok:
            self.Image = ImageTk.PhotoImage(image=Image.fromarray(self.CameraFrame))
            self.VideoCanvas.create_image(250,150,image=self.Image,anchor='center')
        
        self.AppWindow.after(15, self.displayVideo)

    # the following method stops the video stream and closes the application
    def __onCloseWindow__(self):
        print("Closing Video... Done")
        self.VideoStream.release()
        print("Closing Window... Done")
        self.AppWindow.quit()

    # the following method specifies what happens after the sign in button is clicked
    def __onSignInButtonClicked__(self):
        print("Sign In button clicked")

    # the following method clears all of the input fields
    def __onClearButtonClicked__(self):
        self.FirstNameEntryView.delete(0,20)
        self.TitanCardEntryView.delete(0,10)
        self.EmailLabelEntryView.delete(0,20)
# end TitanCardScannerApp()

TitanCardScannerApp()
