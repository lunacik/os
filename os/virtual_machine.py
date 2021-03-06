
class VirtualMachine():
    def __init__(self, proc, page, rm_memory):
        self.PAGE = page
        self.DS = 0 + page
        self.CS = 64 + page
        self.SS = 160 + page
        self.IP = self.CS
        self.SP = self.SS
        self.memory = rm_memory


    def exec_commands(self, vm_gui):
        while(self.exec_command(vm_gui) != True):
            pass


    def exec_command(self, vm_gui):
        DR = str(self.memory[self.IP])
        self.IP += 1
        try:
            if (DR[:2] == 'DS'):
                self.SP += 1
                self.memory[self.SP] = self.memory[self.DS + int(DR[2:])]
            elif (DR[:2] == 'SD'):
                self.memory[self.DS + int(DR[2:])] = self.memory[self.SP] 
                self.SP -= 1
            elif (DR == 'ADD'):
                self.memory[self.SP - 1] = int(self.memory[self.SP - 1]) + int(self.memory[self.SP])
                self.SP -= 1
            elif (DR == 'SUB'):
                self.memory[self.SP - 1] = int(self.memory[self.SP - 1]) - int(self.memory[self.SP])
                self.SP -= 1
            elif (DR == 'MUL'):
                self.memory[self.SP - 1] = int(self.memory[self.SP - 1]) * int(self.memory[self.SP])
                self.SP -= 1
            elif (DR == 'DIV'):
                self.memory[self.SP - 1] = int(int(self.memory[self.SP - 1]) / int(self.memory[self.SP]))
            elif (DR == 'DIV'):
                self.memory[self.SP - 1] = int(int(self.memory[self.SP - 1]) / int(self.memory[self.SP]))
                self.SP -= 1
            elif(DR == 'ECHO'):
                vm_gui.outputBox.insertPlainText(str(self.memory[self.SP]))
                self.SP -= 1 
            elif(DR == 'AND'):
                self.memory[self.SP - 1] = int(self.memory[self.SP - 1]) & int(self.memory[self.SP])
                self.SP -= 1
            elif(DR == 'OR'):
                self.memory[self.SP - 1] = int(self.memory[self.SP - 1]) | int(self.memory[self.SP])
                self.SP -= 1
            elif(DR == 'READ'):
                vm_gui.read_msg_box()
            elif(DR == 'CMP'):
                if (int(self.memory[self.SP - 1]) == int(self.memory[self.SP])):
                    self.memory[self.SP - 1] = 1
                elif (int(self.memory[self.SP - 1]) > int(self.memory[self.SP])):
                    self.memory[self.SP - 1] = 0
                else:
                    self.memory[self.SP - 1] = 2
                self.SP -= 1
            elif(DR == 'NEG'):
                self.memory[self.SP] = int(-self.memory[self.SP])
            elif(DR == 'NOT'):
                if(int(self.memory[self.SP]) == 0):
                    self.memory[self.SP] = 1
                else:
                    self.memory[self.SP] = 0
            elif(DR[:2] == 'JP'):
                self.IP = self.CS + int(DR[2:])
            elif(DR[:2] == 'JE'):
                if(self.memory[self.SP] == 1):
                    self.IP = self.CS + int(DR[2:])
                self.SP -= 1
            elif(DR[:2] == 'JL'):
                if(self.memory[self.SP] == 0):
                    self.IP = self.CS + int(DR[2:])
                self.SP -= 1
            elif(DR[:2] == 'JG'):
                if(self.memory[self.SP] == 2):
                    self.IP = self.CS + int(DR[2:])
                self.SP -= 1
            elif(DR == "HALT"):
                return True
            else:
                vm_gui.msg_box_exception("Error: invalid command")
             
        except ZeroDivisionError:
            vm_gui.msg_box_exception("Error: division by zero")

        except Exception:
            vm_gui.msg_box_exception("Error: unknown error")

