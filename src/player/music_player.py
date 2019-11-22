from playsound import playsound
import npyscreen as npy

class Test(npy.NPSApp):
    def main(self):
        Form = npy.Form(name = "Test")
        Form.add(npy.MultiLine, values = [1, 2, 3, 4])

# playsound('audio.mp3')
