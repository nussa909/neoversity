import pathlib
import sys


def parse_log_line(line: str) -> dict:
    parsed_log = {}
    try:
        words = line.split()

        if len(words) > 3:
            parsed_log["date"] = words[0]    
            parsed_log["time"] = words[1] 
            parsed_log["level"] = words[2] if words[2] in ["INFO", "ERROR", "DEBUG", "WARNING"] else None
            parsed_log["message"] = " ".join(words[3:])

    except Exception as err:
        print("Error:{err}")

    return parsed_log


def load_logs(file_path: str) -> list:
    log_list = []
    try:
        with open(file_path, "r",encoding="utf-8") as file:
            for line in file.readlines():
                log_list.append(parse_log_line(line))
    except FileNotFoundError:
        print("Error: cannot open file!")
    
    return log_list


def filter_logs_by_level(logs: list, level: str) -> list:
    filtered_list = [log for log in logs if log["level"] == level]

    return filtered_list


def count_logs_by_level(logs: list) -> dict:
    logs_by_level_count_dct = {}
    for log_level in ["INFO", "ERROR", "DEBUG", "WARNING"]:
        logs_by_level_count_dct[log_level] = len(filter_logs_by_level(logs,log_level))

    return logs_by_level_count_dct
 

def display_log_counts(counts: dict):
    log_level_header = "Debug level"
    count_header = "Quantity"

    print(f"{log_level_header:^20}|{count_header:^20}")
    print("-" * 40)
    for log_level, count in counts.items():
        print(f"{log_level:^20}|{count:^20}")


def main():
    if len(sys.argv) < 2:
        print("Error: not enough parameters")
        return 
    
    file_path = pathlib.Path(sys.argv[1])
    if not file_path.exists():
        print("Error: Path does not exist")
        return
    
    loaded_logs = load_logs(file_path)
    display_log_counts(count_logs_by_level(loaded_logs))

    if len(sys.argv) > 2:
        if sys.argv[2].lower() in ["info", "error", "debug", "warning"]:
            debug_level = sys.argv[2].upper()
            print(f"\nLog details for debug level \"{debug_level}\":")
            for log in filter_logs_by_level(loaded_logs, debug_level):
                print(f"{log['date']} {log['time']} - {log['message']}")
        else:
            print(f"\nError: unknown debug level {sys.argv[2]}")


if __name__ == "__main__":
    main()

