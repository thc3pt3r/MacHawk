import subprocess, os, datetime, shutil


def hunt_for_all():
    create_output_dir()
    get_safari_history()


def create_output_dir():
    try:
        os.mkdir("browsing_hawk")
        os.mkdir("browsing_hawk/Safari")
        os.mkdir("browsing_hawk/google_chrome")
        os.mkdir("browsing_hawk/mozilla_firefox")
    except FileExistsError:
        print("the directory already exist")
    except Exception as e:
        print(f"There was an error creating the Directory: {e}")


def get_safari_history():
    file_path = os.path.join('browsing_hawk', 'safari', 'history.txt')
    command = '''
    sqlite3 browsing_hawk/Safari/History.db "SELECT h.visit_time,
i.url FROM history_visits h INNER JOIN history_items i ON
h.history_item = i.id"
    '''
    result = subprocess.run(command, stdout=subprocess.PIPE, shell=True)
    output = result.stdout.decode()
    with open(file_path, 'w') as f:
        f.write(output)
    print(f'f"Safari Browsing history saved to {file_path}"')