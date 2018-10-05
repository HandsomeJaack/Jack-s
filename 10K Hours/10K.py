import psutil
import datetime
import sys


PROCNAME1 = 'pycharm64.exe'
PROCNAME2 = 'codeblocks.exe'
PROCNAME3 = 'sublime_text.exe'

python_today = 0
cpp_today = 0
sublime_today = 0


def to_integer(dt_time):
    return 3600*dt_time.hour + 60*dt_time.minute + dt_time.second


def time(total_seconds):
    hours = 0
    minutes = 0
    if total_seconds >= 3600:
        hours = int(total_seconds/3600)
    if total_seconds >= 60:
        minutes = int(total_seconds/60 - hours*60)
    seconds = total_seconds - hours*3600 - minutes*60
    return hours, minutes, seconds


if __name__ == '__main__':
    # Последний запуск среды PyCharm
    python_run = open("python_run.txt", "r+")
    python_day = python_run.read()
    if python_day:
        python_day = str(python_day)
    else:
        print("Latest python run file is empty!")

    right_now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    now_arr = right_now.split()
    now_time_arr = now_arr[1].split(":")
    now_time_arr = list(map(int, now_time_arr))

    python_arr_last = python_day.split()
    python_arr_last_time = python_arr_last[1].split(":")

    for proc in psutil.process_iter():
        if proc.name() == PROCNAME1:
            pycharm_creat = str(datetime.datetime.fromtimestamp(proc.create_time()))
            pycharm_creat_arr = pycharm_creat.split()
            pycharm_creat_date = pycharm_creat_arr[0]
            pycharm_creat_time = pycharm_creat_arr[1]
            pycharm_creat_time_arr = pycharm_creat_time.split(":")
            pycharm_creat_time_arr = list(map(int, pycharm_creat_time_arr))
            if python_arr_last[0] != now_arr[0]:
                diff = []
                for i in range(3):
                    diff.append(abs(pycharm_creat_time_arr[i] - now_time_arr[i]))
                print("Python programmed today: {0}:{1}:{2}".format(diff[0], diff[1], diff[2]))

                python_run.seek(0)
                python_run.write(right_now)
                python_run.close()

                python_file = open("python_data.txt", "r+")
                lastsave_python = python_file.read()

                if lastsave_python:
                    lastsave_python = int(lastsave_python)
                else:
                    print("Python data file is empty!")

                lastsave_python = lastsave_python + diff[0] * 3600 + diff[1] * 60 + diff[2]

                python_file.seek(0)
                python_file.write(str(lastsave_python))
                python_file.close()
                print("Total Python Programmed: %s " % str(time(lastsave_python)))
            else:
                if pycharm_creat_time == python_arr_last[1]:
                    pass
                else:
                    diff = []
                    for i in range(3):
                        diff.append(abs(pycharm_creat_time_arr[i] - now_time_arr[i]))
                    print("Python programmed today: {0}:{1}:{2}".format(diff[0], diff[1], diff[2]))

                    python_run.seek(0)
                    python_run.write(right_now)
                    python_run.close()

                    python_file = open("python_data.txt", "r+")
                    lastsave_python = python_file.read()

                    if lastsave_python:
                        lastsave_python = int(lastsave_python)
                    else:
                        print("Python data file is empty!")

                    lastsave_python = lastsave_python + diff[0] * 3600 + diff[1] * 60 + diff[2]

                    python_file.seek(0)
                    python_file.write(str(lastsave_python))
                    python_file.close()
                    print("Total Python Programmed: %s " % str(time(lastsave_python)))


