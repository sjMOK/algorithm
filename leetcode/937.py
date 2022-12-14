def reorder_log_files(logs):
    letter_logs = []
    digit_logs = []

    for log in logs:
        content = ''.join(log.split()[1:])

        if content.isdigit():
            digit_logs.append(log)
        else:
            letter_logs.append(log)

    letter_logs.sort(key = lambda s:(s.split()[1:], s.split()[0]))

    return letter_logs + digit_logs
