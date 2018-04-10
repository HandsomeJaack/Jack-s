import psutil
import datetime

PROCNAME1 = 'pycharm64.exe'
PROCNAME2 = 'codeblocks.exe'

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

    current_time = to_integer(datetime.datetime.now())
    print(datetime.datetime.now())

    python_file = open("python_data.txt", "r+")
    lastsave_python = python_file.read()
    if lastsave_python:
        lastsave_python = int(lastsave_python)
    else:
        print("Python data file is empty!")

    cpp_file = open("cpp_data.txt", "r+")
    lastsave_cpp = cpp_file.read()
    if lastsave_cpp:
        lastsave_cpp = int(lastsave_cpp)
    else:
        print("C++ data file is empty!")

    python_run = open("python_run.txt", "r+")
    python_day = python_run.read()
    if python_day:
        python_day = str(python_day)
    else:
        print("Latest python run file is empty!")

    cpp_run = open("cpp_run.txt", "r+")
    cpp_day = cpp_run.read()
    if cpp_day:
        cpp_day = str(cpp_day)
    else:
        print("Latest C++ run file is empty!")

    for proc in psutil.process_iter():
        if proc.name() == PROCNAME1:
            print(proc)
            print(datetime.datetime.fromtimestamp(proc.create_time()).strftime("%Y-%m-%d %H:%M:%S"))
            x = to_integer(datetime.datetime.fromtimestamp(proc.create_time()))
            y = datetime.datetime.fromtimestamp(proc.create_time()).strftime("%Y-%m-%d %H:%M:%S")

            if current_time <= x:
                current_time += 86400

            if y == python_day:
                python_run.close()
                break
            elif y != python_day:
                python_run.seek(0)
                python_run.write(y)
                python_run.close()

            python_today = current_time - x
            print("Python programmed today: " + str(time(python_today)))
            lastsave_python = lastsave_python + python_today

        if proc.name() == PROCNAME2:
            print(proc)
            print(datetime.datetime.fromtimestamp(proc.create_time()).strftime("%H:%M:%S"))
            x = to_integer(datetime.datetime.fromtimestamp(proc.create_time()))
            y = datetime.datetime.fromtimestamp(proc.create_time()).strftime("%Y-%m-%d %H:%M:%S")

            if current_time <= x:
                current_time += 86400

            if y == cpp_day:
                cpp_run.close()
                break
            elif y != cpp_day:
                cpp_run.seek(0)
                cpp_run.write(y)
                cpp_run.close()

            cpp_today = current_time - x
            print("C++ programmed today: " + str(time(cpp_today)))
            lastsave_cpp = lastsave_cpp + cpp_today

    python_file.seek(0)
    python_file.write(str(lastsave_python))
    python_file.close()

    cpp_file.seek(0)
    cpp_file.write(str(lastsave_cpp))
    cpp_file.close()

    lastsave_common = lastsave_cpp + lastsave_python
    print("Python programming hours: " + str(time(lastsave_python)))
    print("C++ programming hours: " + str(time(lastsave_cpp)))
    print("Total programming hours:" + str(time(lastsave_common)))


