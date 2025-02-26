'''
OPEN CLOSED PRINCIPLE

Imagine que uma clínica veterinária tem seu sistema próprio para aprovação de exames. No primeiro momento, ela tem um método para
verificar exame de sangue. Em outro ela adiciona exame por raio-x. Notamos no código que, conforme a clínica adiciona exames,
deverão adicionar uma validação para o exame. O que aumentaria a complexidade do código e a manutenção do mesmo.

A solução deste caso pode ser feita com o princípio aberto-fechado (Open Closed Principle). 
Utilizando do conceito do OCP, crie uma interface e classes que implementam a mesma para que, caso a clínica necessite de um novo
tipo de exame, uma nova classe seja adicionada, implementando métodos de uma interface padrão para exames.

'''


from abc import ABC, abstractmethod

class Exam(ABC):
    @abstractmethod
    def approve(self):
        pass

class BloodTest(Exam):
    def approve(self):
        print("Exame sanguíneo aprovado")


class XrayTest(Exam):
    def approve(self):
        print("Exame de Raio-X aprovado")

class ExamApprover:
    def approve_exam(self,exam: Exam):
        exam.approve()


blod_teest = BloodTest()
xray_test = XrayTest()


approver = ExamApprover()

approver.approve_exam(blod_teest)
approver.approve_exam(xray_test)






