from creators.variables.variables import resources_folder
from datetime import datetime, timezone


report_file = f'{resources_folder}\\report.txt'


def run_reporter(text):
    with open(report_file, 'a') as file:
        file.write(f'\n{text}\n {datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S")}\n')
        print(f'{text}\n {datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S")}\n')


