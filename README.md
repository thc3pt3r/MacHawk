# MacHawk - Fast CIR Traige for MacOs systems.

MacHawk is a command-line tool for performing incident response triage on MacOs systems.

## Usage

To run MacHawk, simply execute the `macHawk.sh` script with the desired options:

```bash
./macHawk.sh [options]
```
The available options are:

    -h, --help: Display help and available commands.
    -c, --complete: Run a complete collection of IR triage.
    -p, --partial: Run a partial collection of IR triage.
    -b, --banner: Print the program banner.
    -q, --quit: Exit the program.
´

## Operation

MacHawk is composed of several modules that collect specific system information:

- `general_hawk.sh`: General functions used by other modules.
- `log_hawk.sh`: Collect system logs.
- `network_hawk.sh`: Collect network information.
- `persistence_hawk.sh`: Search for persistence mechanisms.
- `process_hawk.sh`: Analyze running processes.
- `users_hawks.sh`: Collect user information.
- `system_hawk.sh`: Collect general system information.

The `macHawk.sh` script is responsible for running the different modules and generating an output directory with all the collected information.

## Requirements

To use MacHawk, you need the following:

- MacOs operating system
- Bash
- MacOs command-line utilities (lsof, netstat, etc.)
