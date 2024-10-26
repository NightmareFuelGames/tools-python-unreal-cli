# import subprocess
# from rich.console import Console
#
# # Initialize a rich console
# console = Console()
#
# # This is a bit of future proofing in case I start to need to wrap it
# run = subprocess.run
#
#
# def popen_with_format(fmt, args, shell=False):
#     """Execute a command with the given formatter."""
#     # Print the command that will be executed
#     console.print(f"[bold green]Executing:[/bold green] {' '.join(args)}")
#
#     with subprocess.Popen(
#             args,
#             stdout=subprocess.PIPE,
#             stderr=subprocess.STDOUT,
#             text=True,
#             shell=shell,
#     ) as process:
#         from rich.text import Text
#         try:
#             # Displaying output with color-coded lines
#             while process.poll() is None:
#                 line = process.stdout.readline()
#                 if line:
#                     # Handling different log levels for better readability
#                     #
#                     # if "LogClass: Warning: " in line:
#                     #     console.print(Text(line.strip(), style="bold yellow"))
#                     # if "COMPLETED" in line:
#                     #     console.print(Text(line.strip(), style="bold green"))
#                     # elif "[D][LogInit" in line:
#                     #     console.log(Text(line.strip(), style="bold cyan"))
#                     # elif "[L][Running" in line:
#                     #     console.log(Text(line.strip(), style="bold yellow"))
#                     # elif "[D][LogConfig" in line:
#                     #     console.log(Text(line.strip(), style="bold magenta"))
#                     # elif "[D][LogOutputDevice" in line:
#                     #     console.log(Text(line.strip(), style="bold blue"))
#                     # else:
#                     #     # General log output
#                     #     console.print(Text(line.strip(), style="dim"))
#
#                     fmt.match_regex(line)  # Apply any regex-based matching for your fmt object
#
#             # Return process exit code
#             return process.poll() + fmt.returncode()
#         except KeyboardInterrupt:
#             console.print("[red]Stopping due to user interrupt[/red]")
#             process.kill()
#             return -1


import subprocess

# This is a bit of future proofing in case I start to need to wrap it
run = subprocess.run


def popen_with_format(fmt, args, shell=False):
    """Execute a command with the given formatter."""

    print(" ".join(args))

    with subprocess.Popen(
        args,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        # This is needed because without lines might not be recognized as such
        text=True,
        shell=shell,
    ) as process:
        try:
            while process.poll() is None:
                # sys.stdout.flush()

                line = process.stdout.readline()

                if len(line) > 0:
                    fmt.match_regex(line)

            return process.poll() + fmt.returncode()
        except KeyboardInterrupt:
            print("Stopping due to user interrupt")
            process.kill()

        return -1