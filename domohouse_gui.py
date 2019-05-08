import sys
import cv2
import time
import os

if sys.version_info[0] >= 3:
    import PySimpleGUI as sg
else:
    import PySimpleGUI27 as sg

# Declaracion de variables importantes
sg.ChangeLookAndFeel('BlueMono')
image_logo = 'C:/Users/Miguel Osuna/OneDrive/Documentos/Trabajos/Universidad/8vo Semestre/Ingeniería de Proyectos de Electrónica/DomoHouse_GUI/images/id.png'

# Importar cascade para deteccion de rostros
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Definicion de otras variables
faceConfirmed = False
tagConfirmed = False
menuDisplayed = False
cntr = 0
name = ''
photoNum = 1

# Definiendo los layouts de la GUI
layout_inicio = [[sg.Image(filename=image_logo, size=(80, 80)),
                  sg.Text('DOMOHOUSE', size=(20, 1), font=('Roboto', 30), justification='center', text_color="white",
                          pad=(10, 10), auto_size_text=True)],
                 [sg.Text('_' * 100, pad=(5, 5), text_color="white", auto_size_text=True)],
                 [sg.Text(' ' * 200, pad=(5, 5), text_color="white", auto_size_text=True)],

                 [sg.T(' ' * 20),
                  sg.Button('Iniciar sesión', size=(16, 2), pad=(5, 5), font=('Roboto', 20),
                            button_color=('#4c85e0', '#FFFFFF'), auto_size_button=True, key='Login')],
                 ]

layout_login = [[sg.Image(filename=image_logo, size=(80, 80)),
                 sg.Text('DOMOHOUSE', size=(20, 1), font=('Roboto', 30), justification='center', text_color="white",
                         pad=(10, 10), auto_size_text=True)],
                [sg.Text('_' * 100, pad=(5, 5), text_color="white", auto_size_text=True)],

                [sg.Text('Por favor, verifique su identificación', size=(40, 1), font=('Roboto', 16),
                         justification='center', text_color="white", pad=(10, 10), auto_size_text=True, key='OUTPUT')],
                [sg.Text('Presione el botón', size=(18, 1), font=('Roboto', 16), justification='center',
                         text_color="white", background_color="gray", pad=(10, 10), auto_size_text=True,
                         key='FaceConfirmed'), sg.T(' ' * 10),
                 sg.Button('Face ID', size=(10, 1), pad=(5, 5), font=('Roboto', 16),
                           button_color=('#4c85e0', '#FFFFFF'), auto_size_button=True, key='FaceID')],
                [sg.Text('Presione el botón', size=(18, 1), font=('Roboto', 16), justification='center',
                         text_color="white", background_color="gray", pad=(10, 10), auto_size_text=True,
                         key='TagConfirmed'), sg.T(' ' * 10),
                 sg.Button('Tag ID', size=(10, 1), pad=(5, 5), font=('Roboto', 16), button_color=('#4c85e0', '#FFFFFF'),
                           auto_size_button=True, key='TagID')],
                [sg.T(' ' * 35),
                 sg.Button('Salir', size=(10, 2), pad=(5, 5), font=('Roboto', 12), button_color=('#4c85e0', '#FFFFFF'),
                           auto_size_button=True, key='Salir')]
                ]

layout_menu = [[sg.Image(filename=image_logo, size=(80, 80)),
                sg.Text('DOMOHOUSE', size=(20, 1), font=('Roboto', 30), justification='center', text_color="white",
                        pad=(10, 10), auto_size_text=True)],
               [sg.Text('_' * 100, pad=(5, 5), text_color="white", auto_size_text=True)],

               [sg.Text('Bienvenido, mi amo, elija su opcion', size=(40, 1), font=('Roboto', 16),
                        justification='center', text_color="white", background_color="gray", pad=(10, 10),
                        auto_size_text=True, key='Bienvenida')],
               [sg.T(' ' * 15),
                sg.Button('On/Off', size=(10, 2), pad=(5, 5), font=('Roboto', 12), button_color=('#4c85e0', '#FFFFFF'),
                          auto_size_button=True, key='OnOff'),
                sg.T(' ' * 15), sg.Button('Agregar Usuario', size=(10, 2), pad=(5, 5), font=('Roboto', 12),
                                          button_color=('#4c85e0', '#FFFFFF'), auto_size_button=True, key='Agregar')],
               [sg.T(' ' * 15), sg.Button('Finalizar Sesión', size=(10, 2), pad=(5, 5), font=('Roboto', 12),
                                          button_color=('#4c85e0', '#FFFFFF'), auto_size_button=True, key='Finalizar'),
                sg.T(' ' * 15), sg.Button('Eliminar Usuario', size=(10, 2), pad=(5, 5), font=('Roboto', 12),
                                          button_color=('#4c85e0', '#FFFFFF'), auto_size_button=True,
                                          key='EliminarUsuario')]
               ]

layout_agregar = [[sg.Image(filename=image_logo, size=(80, 80)),
                   sg.Text('DOMOHOUSE', size=(20, 1), font=('Roboto', 30), justification='center', text_color="white",
                           pad=(10, 10), auto_size_text=True)],
                  [sg.Text('_' * 100, pad=(5, 5), text_color="white", auto_size_text=True)],

                  [sg.Text('Nombre:', size=(10, 1), font=('Roboto', 16), justification='right', text_color="white",
                           pad=(10, 10), auto_size_text=True),
                   sg.InputText('Fulano', size=(30, 2), font=('Roboto', 16), text_color="black",
                                background_color="white", pad=(10, 10), key='photoFirstName')],
                  [sg.Text('Aprellido:', size=(10, 1), font=('Roboto', 16), justification='right', text_color="white",
                           pad=(10, 10), auto_size_text=True),
                   sg.InputText('Mengano', size=(30, 2), font=('Roboto', 16), text_color="black",
                                background_color="white", pad=(10, 10), key='photoLastName')],
                  [sg.Button('Tomar Foto', size=(10, 1), pad=(5, 5), font=('Roboto', 12),
                             button_color=('#4c85e0', '#FFFFFF'), auto_size_button=True, key='TomarFoto'),
                   sg.Text('Foto #' + str(photoNum) + ' de 10', size=(16, 1), font=('Roboto', 16),
                           justification='center', text_color="white", background_color="gray", pad=(10, 10),
                           auto_size_text=True, key='Fotos'),
                   sg.Button('Regresar', size=(14, 1), pad=(5, 5), font=('Roboto', 12),
                             button_color=('#4c85e0', '#FFFFFF'), auto_size_button=True, key='Regresar')]
                  ]

layout_eliminar = [[sg.Image(filename=image_logo, size=(80, 80)),
                    sg.Text('DOMOHOUSE', size=(20, 1), font=('Roboto', 30), justification='center', text_color="white",
                            pad=(10, 10), auto_size_text=True)],
                   [sg.Text('_' * 100, pad=(5, 5), text_color="white", auto_size_text=True)],

                   [sg.Text('Nombre:', size=(10, 1), font=('Roboto', 16), justification='right', text_color="white",
                            pad=(10, 10), auto_size_text=True),
                    sg.InputText('Fulano', size=(30, 2), font=('Roboto', 16), text_color="black",
                                 background_color="white", pad=(10, 10), key='photoFirstName')],
                   [sg.Text('Aprellido:', size=(10, 1), font=('Roboto', 16), justification='right', text_color="white",
                            pad=(10, 10), auto_size_text=True),
                    sg.InputText('Mengano', size=(30, 2), font=('Roboto', 16), text_color="black",
                                 background_color="white", pad=(10, 10), key='photoLastName')],
                   [sg.Text(' ' * 20), sg.Button('Eliminar', size=(10, 1), pad=(10, 10), font=('Roboto', 12),
                                                 button_color=('#4c85e0', '#FFFFFF'), auto_size_button=True,
                                                 key='Eliminar'),
                    sg.Button('Regresar', size=(14, 1), pad=(10, 10), font=('Roboto', 12),
                              button_color=('#4c85e0', '#FFFFFF'), auto_size_button=True, key='Regresar')]
                   ]

def takeSnapshotAndSave(firstName, lastName, number):
    # access the webcam (every webcam has a number, the default is 0)
    cap = cv2.VideoCapture(0)
    capture = 1

    while capture <= number:
        # Capture frame-by-frame
        ret, frame = cap.read()

        # to detect faces in video
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)

        for (x,y,w,h) in faces:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
            roi_gray = gray[y:y+h, x:x+w]
            roi_color = frame[y:y+h, x:x+w]

        # if you want to convert it to gray uncomment and display gray not fame
        #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        crop_img = frame[y: y + h, x: x + w]  # Crop from x, y, w, h -> 100, 200, 300, 400
        name = firstName[0] + lastName[0] + str(capture)
        cv2.imwrite("./images/" + name + ".jpg", crop_img)
        time.sleep(1)
        capture += 1

    # When everything done, release the capture
    # cap.release()
    # cv2.destroyAllWindows()
    return None

# Ventana de inicializacion
window = sg.Window('Welcome to DomoHouse', size=(480, 320), no_titlebar=True).Layout(layout_inicio)

# main loop program
while True:
    # reads and updates the window
    # timeout is a delay
    event, values = window.Read(timeout=0)

    # Boton para desplegar la ventana de inicio de sesion
    if event == 'Login':
        window.Close()
        window = sg.Window('DomoHouse: Your App', size=(480, 320), no_titlebar=True).Layout(layout_login)

        '''
        if faceConfirmed == False or tagConfirmed == False:
            window.FindElement('TagConfirmed').Update('Presione el botón')
            window.FindElement('FaceConfirmed').Update('Presione el botón')
        '''

    # Boton para confirmar FaceID del usuario
    if event == 'FaceID':
        # Desplegar ventana de Popup
        if sg.PopupYesNo('¿Desea tomar la foto?', text_color="white", font=('Roboto', 20),
                         button_color=('#4c85e0', '#FFFFFF'), keep_on_top=True, no_titlebar=True) == 'Yes':
            # Confirmar Face ID

            # Agregar algoritmo de comparacion
            # Crear una funcion de comparacion

            # El nombre sera cambiado por el programa de reconocimiento facial, de acuerdo a la base de datos
            name = 'Miguel'
            window.FindElement('FaceConfirmed').Update('Face ID verificado')
            faceConfirmed = True

    # Boton para confirmar TagID del usuario
    if event == 'TagID':
        # Desplegar ventana de Popup
        if sg.PopupYesNo('¿Desea escanear la tarjeta?', text_color="white", font=('Roboto', 20),
                         button_color=('#4c85e0', '#FFFFFF'), keep_on_top=True, no_titlebar=True) == 'Yes':
            # Confirmar Tag ID

            # Agregar algoritmo de comparacion
            # Crear una funcion de comparacion

            window.FindElement('TagConfirmed').Update('Tag ID verificado')
            tagConfirmed = True

    # Boton para regresar a la ventana de inicio
    if event == 'Salir':
        tagConfirmed = False
        faceConfirmed = False
        window.Close()
        window = sg.Window('Welcome to DomoHouse', size=(480, 320), no_titlebar=True).Layout(layout_inicio)

    # Si el ususario ya confirmo su ID, accede al sistema
    if faceConfirmed is True and tagConfirmed is True and menuDisplayed is False:
        window.Close()
        window = sg.Window('DomoHouse: Your App', size=(480, 320), no_titlebar=True).Layout(layout_menu)
        sg.Popup('Bienvenido, amo ' + name, text_color="white", font=('Roboto', 20),
                 button_color=('#4c85e0', '#FFFFFF'), keep_on_top=True, no_titlebar=True)
        menuDisplayed = True

    if event == 'OnOff':
        # Manda al MCU el primer caracter del nombre del usuario
        print(name[0])
        cntr += 1

        # Para "Off", el valor del contador es par, y para "On", el valor del contador es impar
        # Por default, el sistema inicia apagado, es decir, el contador igual a 0
        if cntr % 2 == 0:
            sg.Popup('Sistema apagado', text_color="white", font=('Roboto', 20), button_color=('#4c85e0', '#FFFFFF'),
                     keep_on_top=True, no_titlebar=True)

        if cntr % 2 != 0:
            sg.Popup('Sistema encendido', text_color="white", font=('Roboto', 20), button_color=('#4c85e0', '#FFFFFF'),
                     keep_on_top=True, no_titlebar=True)

    if event == 'Finalizar':
        # Devuelve el valor de las variables a su estado original
        tagConfirmed = False
        faceConfirmed = False
        menuDisplayed = False
        name = 'Somebody'
        photoNum = 1
        window.Close()
        window = sg.Window('Welcome to DomoHouse', size=(480, 320), no_titlebar=True).Layout(layout_inicio)

        # Para asegurar de apagar el equipo por completo, se apaga al momento de finalizar la sesion
        if cntr % 2 != 0:
            # Se manda la primera incinial del usuario
            print(name[0])
            cnt = 0
            print(cnt)

    if event == 'Agregar':
        window.Close()
        window = sg.Window('DomoHouse: Your App', size=(480, 320), no_titlebar=True).Layout(layout_agregar)

    # Cada que se presione el boton de "Tomar Foto",
    # se capturara una imagen del rostro del usuario, para asi poder almacenarla
    if event == 'TomarFoto':
        '''
        Cuando se capture la imagen, se almacenara mediante el uso de las iniciales del nombre y apellido del usuario,
        junto con el numero de foto

        Ej: Nombre: Miguel
            Apellido: Osuna
            PhotoNumber: 1

            MO1.jpeg
            .
            .
            .
            MO10.jpeg 
        '''
        if photoNum < 10 and sg.PopupYesNo('¿Quiere tomar la foto?', text_color="white", font=('Roboto', 20),
                                           button_color=('#4c85e0', '#FFFFFF'), keep_on_top=True,
                                           no_titlebar=True) == 'Yes':
            # Codigo para tomar la foto y almacenarla
            # Se obtiene el nombre y el apellido de las entradas de texto,
            # y despues se utiliza solamente la primer letra de cada uno
            firstName = window.FindElement('photoFirstName').Get()
            lastName = window.FindElement('photoLastName').Get()

            sg.PopupQuickMessage("Espere mientras se toman las fotos", text_color="black", font=('Roboto', 20),
                          button_color=('#4c85e0', '#FFFFFF'), keep_on_top=True, no_titlebar=True)

            takeSnapshotAndSave(firstName, lastName, 10)
            window.FindElement('Fotos').Update('Progreso: #10 de 10')
            photoNum = 10

        if photoNum >= 10:
            sg.Popup('Ya se tomaron todas las fotos, gracias', text_color="white", font=('Roboto', 20),
                     button_color=('#4c85e0', '#FFFFFF'), keep_on_top=True, no_titlebar=True)

    # Boton para regresar al menu de opciones
    if event == 'Regresar':
        window.Close()
        window = sg.Window('DomoHouse: Your App', size=(480, 320), no_titlebar=True).Layout(layout_menu)

    # Boton para eliminar el usuario de acuerdo a los archivos guardados
    if event == 'EliminarUsuario':
        window.Close()
        window = sg.Window('DomoHouse: Your App', size=(480, 320), no_titlebar=True).Layout(layout_eliminar)

    if event == 'Eliminar':
        firstName = window.FindElement('photoFirstName').Get()
        lastName = window.FindElement('photoLastName').Get()

        if sg.PopupYesNo('¿Seguro que quiere eliminar las fotos?', text_color="white", font=('Roboto', 20),
                         button_color=('#4c85e0', '#FFFFFF'), keep_on_top=True, no_titlebar=True) == 'Yes':
            # Agregar algoritmo para borrar archivos de una carpeta
            for num in range(1, 11):
                if os.path.exists("images" + '/' + firstName[0] + lastName[0] + str(num) + ".jpg"):
                    os.remove("images" + '/' + firstName[0] + lastName[0] + str(num) + ".jpg")
                else:
                    sg.PopupQuickMessage("Usuario no existente", text_color="black", font=('Roboto', 20),
                                         button_color=('#4c85e0', '#FFFFFF'), keep_on_top=True, no_titlebar=True)
            time.sleep(3)
            sg.Popup('Imágenes eliminadas', text_color="white", font=('Roboto', 20),
                     button_color=('#4c85e0', '#FFFFFF'), keep_on_top=True, no_titlebar=True)

# window.Close()
