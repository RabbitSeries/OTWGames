def findAuth(level: int):
    psw = next((psw for psw in open("passwords").read().splitlines()
               if psw.startswith("Level 18")), None)
    return psw.split(":")[1].strip() if psw else None
