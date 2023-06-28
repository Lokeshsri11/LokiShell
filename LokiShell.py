import Levenshtein

valid_commands = ["help", "hello", "init", "clone", "add", "commit", "push", "pull", "merge", "checkout", "branch", "status", "log", "reset", "remote", "config", "diff", "stash", "tag", "fetch", "rebase", "cherry-pick", "revert", "show", "rm", "mv", "grep", "am", "bisect", "reflog", "submodule", "config", "describe", "diff", "shortlog", "ignore", "clean", "remote", "fsck", "blame", "instaweb", "mv", "rename"]

def autocorrect_command(command):
    min_distance = float('inf')
    corrected_command = None
    for valid_command in valid_commands:
        distance = Levenshtein.distance(command, valid_command)
        if distance < min_distance:
            min_distance = distance
            corrected_command = valid_command
    return corrected_command

def run_shell():
    while True:
        user_input = input(">> ")
        command = user_input.strip()

        if command in valid_commands:
            print(f"Executing command: {command}")
        else:
            corrected_command = autocorrect_command(command)
            if corrected_command:
                print(f"Command not found. Did you mean: {corrected_command}?")
                confirm = input("Press 'y' to execute the suggested command: ")
                if confirm.lower() == 'y':
                    print(f"Executing command: {corrected_command}")
                else:
                    print("Command not executed.")
            else:
                print("Command not found.")

        if command == "quit":
            break

run_shell()
