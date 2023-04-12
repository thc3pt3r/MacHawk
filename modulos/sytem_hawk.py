import subprocess, os, datetime, shutil



def hunt_for_all():
    create_output_dir()
    mad_path()
    etc_listing()
    hosts_content()
    copy_launchagents()
    copy_launchdaemons()


def create_output_dir():
    try:
        os.mkdir("system_hawk")
    except FileExistsError:
        print("the directory already exist")
    except Exception as e:
        print(f"There was an error creating the Directory: {e}")
def sysdiagnose_hawk():
    directory_name = "System_hawk"
    try:
        os.mkdir(directory_name)
        print(f"Directory '{directory_name}' created successfully!")
    except FileExistsError:
        print(f"Directory '{directory_name}' already exists!")
    except Exception as e:
        print(f"An error occurred while creating directory '{directory_name}': {e}")
        return

    current_time = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"sysdiagnose_{current_time}.tar.gz"
    filepath = os.path.join(directory_name, filename)

    try:
        subprocess.run(["sudo", "sysdiagnose", "-f", directory_name, "-A", filename], check=True)
        print(f"Sysdiagnose output saved to '{filepath}' successfully!")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while running sysdiagnose: {e}")
    except Exception as e:
        print(f"An error occurred while saving sysdiagnose output to '{filepath}': {e}")

# Functions to look for System Manipulation


def mad_path():
    file_path = os.path.join('system_hawk', 'mad_path.txt')
    script = '''#! /bin/bash
while IFS=: read -d: -r path; do
cd $path
echo $path
ls -altR
done <<< "${PATH:+"${PATH}:"}"'''
    process = subprocess.Popen(['sudo', 'bash', '-c', script], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    with open(file_path, 'w') as f:
        f.write(stdout.decode('utf-8'))

    if stdout:
        print(stdout.decode('utf-8'))
    if stderr:
        print(stderr.decode('utf-8'))


def etc_listing():
    file_path = os.path.join('system_hawk', 'etc_listing.txt')
    command = 'cd /etc; ls -altR'
    result = subprocess.run(command, stdout=subprocess.PIPE, shell=True)
    output = result.stdout.decode()
    with open(file_path, 'w') as f:
        f.write(output)
    print(f"etc listing output saved to {file_path}")


def hosts_content():
    file_path = os.path.join('system_hawk', 'hosts_content.txt')
    command = ['sudo', 'cat', '/etc/hosts']
    result = subprocess.run(command, stdout=subprocess.PIPE)
    output = result.stdout.decode()
    with open(file_path, 'w') as f:
        f.write(output)
    print(f"hosts content output saved to {file_path}")


def copy_launchagents():
    src_dir = "/Library/LaunchAgents/"
    dest_dir = "Logs_hawk/LaunchAgents/"
    try:
        shutil.copytree(src_dir, dest_dir)
        print(f"Directory '{src_dir}' copied to '{dest_dir}' successfully!")
    except shutil.Error as e:
        print(f"An error occurred while copying directory '{src_dir}' to '{dest_dir}': {e}")
    except Exception as e:
        print(f"An unexpected error occurred while copying directory '{src_dir}' to '{dest_dir}': {e}")


def copy_launchdaemons():
    src_dir = "/Library/LaunchDaemons/"
    dest_dir = "Logs_hawk/LaunchDaemons/"
    try:
        shutil.copytree(src_dir, dest_dir)
        print(f"Directory '{src_dir}' copied to '{dest_dir}' successfully!")
    except shutil.Error as e:
        print(f"An error occurred while copying directory '{src_dir}' to '{dest_dir}': {e}")
    except Exception as e:
        print(f"An unexpected error occurred while copying directory '{src_dir}' to '{dest_dir}': {e}")