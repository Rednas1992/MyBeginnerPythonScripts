from datetime import datetime

def write_to_file(filename, text):
    try:
        current_time = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        log_entry = f"{current_time}: {text}\n"

        with open(filename, 'a') as file:
            file.write(log_entry)

        print("Success")
    except Exception as e:
        print("No success:", str(e))

# Example usage
filename = "log1.txt"
text = "dit is een test zodat ik dit later kan gebruiken om log files weg te schrijven"

write_to_file(filename, text)
