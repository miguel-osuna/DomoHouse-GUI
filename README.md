# DomoHouse_GUI
The following project was developed as a final evaluation of the Project Engineering class. DomoHouse Consists on a Domotic Application to improve user comfort and safety.

A facial recognition system was implemented in order to automate different actions at home.

## **Components**
- Raspberry Pi 3b+
- 1080p Web Cam
- LCD Touch Screen HDMI 3.5'' Monitor Display
- Arduino Nano
- Bluetooth Module
- RFID Module
- Buzzer
- LEDs

## **Technology Stack**
- Raspbian
- Arduino
  - SPI Library
  - MFRC522 Library
- Python 3 Programming Language
  - OpenCV Library
  - Numpy Library
  - PySimpleGUI

## **Block Diagram**
<p align="center">
  <image src= captures/block_diagram.png width=640>
</p>

## **Project Description**
A graphical user interface was developed, as well as the image processing part with Python. As samples you have a database consisting of images.

Using the GUI the user has the opportunity to:
- Access the home
- Register a new user
- Delete a user
- Return to the main menu

With Arduino, the microcontroller was programmed for the conditioning of the different actuators (LEDs, Servos, Buzzers).

The Arduino code is run on the Microcontroller, and through a Bluetooth module it is connected to the Raspberry Pi 3b +, where the Python program runs.

## **GUI Design**

### Startup Layout
This login window simply displays the login window, which is used to access the system.

<p align="center">
  <image src= captures/inicio.png width=640>
</p>

### Login Layout
The login window has different elements that allow the user to confirm their identity in two different ways.

The first of these is the confirmation of identification through the user's face. For this, the user will previously have to create a small database of 10 images to have them as references.

The second of the forms of identification is through a unique identification card that the user must always carry.
This is only included as a way to strengthen the security system for the user.

<p align="center">
  <image src= captures/inicia_sesion.png width=640>
</p>

When the two security phases are verified, a window of type 'pop-up' will be displayed that will confirm access to the user through a message that includes his / her name, for example:

<p align="center">
  <image src= captures/popup_amo.png width=640>
</p>

### Menu Layout
The main menu is where all the magic happens, when we access it, we can realize we receive a warm greeting from the graphical user interface, this is displayed in the text window with “Welcome, my master, choose your option".

There are four buttons to be operated according to the user's decisions.

- The first of these is the On / Off button
- The second is the Add User button
- The third is the End Session button
- The fourth is the Delete User button

<p align="center">
  <image src= captures/menu.png width=640>
</p>

### Add Layout
In the tab to add a new user, we find several elements to generate the new record.

The first user's name is the first element

In total, there are 10 different samples per user. With these samples, the capture of the photo taken by the “Face ID” identifier can be compared. This way you have greater accuracy of the results.

<p align="center">
  <image src= captures/add.png width=640>
</p>

### Delete Layout
When we no longer want to have a user's record, we simply delete the images we have available in the folder.

In the same way, the initials of the name and surname are taken to look for the name of the image inside the folder, alternating only the number to find it.

<p align="center">
  <image src= captures/remove.PNG width=640>
</p>
