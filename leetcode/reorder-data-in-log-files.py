class Solution:
    def reorderLogFiles(self, logs: list[str]) -> list[str]:
        letter_logs = []
        digit_logs = []
        for log in logs:
            temp = log.split(" ")
            if(temp[1].isalpha()):
                letter_logs.append(log)
            else:
                digit_logs.append(log)
        letter_logs = sorted(letter_logs, key=lambda w:(w.split(" ")[1:],w.split(" ")[0]))
        logs = letter_logs + digit_logs
        return logs