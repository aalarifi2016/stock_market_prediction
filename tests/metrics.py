import subprocess


def calculate_complexity():
    Bash_command = 'radon cc -s -j libs/'
    results = subprocess.run(Bash_command)
    print(results)


calculate_complexity()


