'''
SINGLE RESPONSABILITY PRINCIPLE

Note que nessa classe, temos várias ações e responsabilidades. O que torna a manutenção, usabilidade e até a performance ruins.

Seguindo o conceito do Princípio da Responsabilidade única, organize essa classe e, se necessário, crie outras 
classes com suas devidas responsabilidades.

'''


class APIconnector:
    def conect_api(self):
        pass


class TaskManager:
    def create_task(self):
        pass

    def update_task(self):
        pass

    def remove_task(self):
        pass

class NotificationService:
    def send_notification(self):
        pass

class ReportGeneretor:
    def generate_report(self):
        pass

class ReportSender:
    def send_report(self):
        pass