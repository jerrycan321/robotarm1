from tkinter import filedialog
from tkinter import *
from pyfirmata import Arduino, util
import time,json
import translate


st = 0
location = []

pins = {'Servo1' : 11,
        'Servo2' : 10,
        'Servo3' : 9,
        'Servo4' : 6,
        'Servo5' : 5,
        'Servo6' : 4 }

servo1_pos = 90
servo2_pos = 90
servo3_pos = 90
servo4_pos = 90
servo5_pos = 90
servo6_pos = 90


board = Arduino('/dev/ttyACM0')
servo1 = board.get_pin('d:11:s')
servo2 = board.get_pin('d:10:s')
servo3 = board.get_pin('d:9:s')
servo4 = board.get_pin('d:6:s')
servo5 = board.get_pin('d:5:s')
servo6 = board.get_pin('d:4:s')

def servo_one(value):
  global servo1_pos
  print("one - Value = %s" % value)
  servo1_pos=int(value)
  servo1.write(value)
  
def servo_two(value):
  global servo2_pos
  print("two - Value = %s" % value)
  servo2_pos = int(value)
  servo2.write(value)


def servo_three(value):
  global servo3_pos
  print("three - Value = %s" % value)
  servo3_pos = int(value)
  servo3.write(value)


def servo_four(value):
  global servo4_pos
  print("four - Value = %s" % value)
  servo4_pos = int(value)
  servo4.write(value)


def servo_five(value):
  global servo5_pos
  print("five - Value = %s" % value)
  servo5_pos = int(value)
  servo5.write(value)


def servo_six(value):
  global servo6_pos
  print("Six - Value = %s" % value)
  servo6_pos = int(value)
  servo6.write(value)


def save_pos():
   global st
   global location
   st = st + 1
   location.append([servo1_pos, servo2_pos, servo3_pos, servo4_pos, servo5_pos, servo6_pos])
   print("Save Pos")

def save_loc():
    global location
    global tk
    #with open("location1.json","w") as write_file:
    with open(filedialog.asksaveasfilename(initialdir = ".",
              title = "Select file",
              filetypes = (("json files","*.json"),("all file types","*.*"))),"w") as write_file:
        json.dump(location,write_file)

def load_loc():
    global location
    location = []
    with open(filedialog.askopenfilename(initialdir=".",
              title = "Select file",
              filetypes = (("json filess","*.json"),("all files","*.*"))),"r") as read_file:
       location = json.load(read_file)


def dump_pos():
    global location
    for step in location:
       print(step)

def runSequence():
    global location
    print("RUN Sequence")
    count=0
    for step in location:
       if count > 1:
          print("Start - %s" % str(location[count-1]))
          print("End   - %s" % str(location[count]))
          locmat = translate.translate(location[count-1],location[count])
          for servo_set in locmat:
             print("Moving to %s" % str(servo_set))
             servo1.write(str(servo_set[0]))
             servo2.write(str(servo_set[1]))
             servo3.write(str(servo_set[2]))
             servo4.write(str(servo_set[3]))
             servo5.write(str(servo_set[4]))
             servo6.write(str(servo_set[5]))
             time.sleep(0.1) 
       count = count + 1
    print("Sequence complete")


root = Tk()




saveButton = Button(root, text="Save Point", command=save_pos)
saveButton.place(x=0, y=0)
saveButton.pack()

dumpButton = Button(root, text="Dump points", command=dump_pos)
dumpButton.place(x=0, y=10)
dumpButton.pack()


runButton = Button(root, text="RUN", command=runSequence)
runButton.place(x=0, y=10)
runButton.pack()


runButton = Button(root, text="SAVE", command=save_loc)
runButton.place(x=0, y=10)
runButton.pack()


runButton = Button(root, text="LOAD", command=load_loc)
runButton.place(x=0, y=10)
runButton.pack()


scale1 = Scale(root,
        command = servo_one,
        from_ = 1,
        to = 175,
        orient = HORIZONTAL,
        length = 400,
        label = "Servo 1")

scale1.set(90)
scale1.pack()

scale2 = Scale(root,
        command = servo_two,
        from_ = 1,
        to = 175,
        orient = HORIZONTAL,
        length = 400,
        label = "Servo 2")

scale2.set(90)
scale2.pack()



scale3 = Scale(root,
        command = servo_three,
        from_ = 1,
        to = 175,
        orient = HORIZONTAL,
        length = 400,
        label = "Servo 3")

scale3.set(90)
scale3.pack()


scale4 = Scale(root,
        command = servo_four,
        from_ = 1,
        to = 175,
        orient = HORIZONTAL,
        length = 400,
        label = "Servo 4")

scale4.set(90)
scale4.pack()



scale5 = Scale(root,
        command = servo_five,
        from_ = 1,
        to = 175,
        orient = HORIZONTAL,
        length = 400,
        label = "Servo 5")

scale5.set(90)
scale5.pack()


scale6 = Scale(root,
        command = servo_six,
        from_ = 1,
        to = 175,
        orient = HORIZONTAL,
        length = 400,
        label = "Servo 6")

scale6.set(90)
scale6.pack()

root.mainloop()

