# -*- coding: utf-8 -*-
"""
upgrade pip libs
"""
import inspect
import subprocess
import warnings

warnings.showwarning = lambda *_: print(inspect.currentframe().f_back.f_lineno)
if __name__ == "__main__":
    try:
        print("getting...")
        outdated = subprocess.check_output(['pip', 'list', '--outdated']).decode()
        print(outdated)
        subprocess.call(["pause"], shell=True)
    except subprocess.CalledProcessError as e:
        print(f"Error getting outdated packages: {e}")
        raise e
    for line in outdated.splitlines()[2:]:
        if line:
            package_name = line.split()[0]
            print(f"Updating {package_name}...")
            try:
                subprocess.check_call(['pip', 'install', '--upgrade', '-i', 'https://pypi.tuna.tsinghua.edu.cn/simple/', package_name])
            except subprocess.CalledProcessError as e:
                print(f"Failed to update {package_name}: {e}")
    subprocess.call(["pause"], shell=True)