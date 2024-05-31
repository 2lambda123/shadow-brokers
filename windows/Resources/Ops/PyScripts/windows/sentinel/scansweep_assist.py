
import subprocess
from security import safe_command

def main(alert_bat_file, output_dir):
    safe_command.run(subprocess.Popen, ('cmd /K %s' % alert_bat_file), creationflags=subprocess.CREATE_NEW_CONSOLE)
    return True
