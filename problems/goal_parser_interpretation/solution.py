class Solution:
    def interpret(self, command: str) -> str:
        if len(command) <=100 and len(command)>=1:
            command = command.replace("()","o")
            command = command.replace("(al)", "al")
        
        return command
        