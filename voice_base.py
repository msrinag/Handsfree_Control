import speech_recognition as sr
import  pyautogui as p
# Initialize the recognizer
r = sr.Recognizer()

# Function to convert text to
# speech


# Loop infinitely for user to
# speak

while 1:

    # Exception handling to handle
    # exceptions at the runtime
    try:

        # use the microphone as source for input.
        with sr.Microphone() as source2:

            # wait for a second to let the recognizer
            # adjust the energy threshold based on
            # the surrounding noise level
            r.adjust_for_ambient_noise(source2, duration=0.2)

            # listens for the user's input
            audio2 = r.listen(source2)

            # Using ggogle to recognize audio
            MyText = r.recognize_google(audio2)
            MyText = MyText.lower()

            print("Did you say " + MyText)
            if MyText=='take screenshot':
                img = p.screenshot()
                img.save('test1.png')

            elif (MyText.find('type')!= -1):
                p.write(MyText[MyText.find('type')+5:])
            elif (MyText.find('right click')):
                p.click(button='left')
            elif (MyText.find('left click')):
                p.click(button='right')

    except sr.RequestError as e:
        print("not a command")

    except sr.UnknownValueError:
        print("not a command")
#kar lohellorcbipl

#RC B TYPE RCB