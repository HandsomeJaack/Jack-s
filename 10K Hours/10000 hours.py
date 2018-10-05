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
    current_time = to_integer(datetime.datetime.now())

    python_file = open("python_data.txt", "r+")
    lastsave_python = python_file.read()

    # Последнее кол-во часов по Python
    if lastsave_python:
        lastsave_python = int(lastsave_python)
    else:
        print("Python data file is empty!")

    # Последнее кол-во часов по C++
    cpp_file = open("cpp_data.txt", "r+")
    lastsave_cpp = cpp_file.read()
    if lastsave_cpp:
        lastsave_cpp = int(lastsave_cpp)
    else:
        print("C++ data file is empty!")

    # Последний запуск среды PyCharm
    python_run = open("python_run.txt", "r+")
    python_day = python_run.read()
    if python_day:
        python_day = str(python_day)
    else:
        print("Latest python run file is empty!")

    # Последний запуск среды CodeBlocks
    cpp_run = open("cpp_run.txt", "r+")
    cpp_day = cpp_run.read()
    if cpp_day:
        cpp_day = str(cpp_day)
    else:
        print("Latest C++ run file is empty!")
    
    common_file = open("common_data.txt", "r+")
    lastsave_sublime = common_file.read()
    if lastsave_sublime:
        lastsave_sublime = int(lastsave_sublime)
    else:
        print("Common data file is empty!")

    # Последний запуск Sublime
    sublime_run = open("sublime_run.txt", "r+")
    sublime_day = sublime_run.read()
    if sublime_day:
        sublime_day = str(sublime_day)
    else:
        print("Latest Sublime Text Editor run file is Empty!")

    for proc in psutil.process_iter():
        if proc.name() == PROCNAME1:
            x = to_integer(datetime.datetime.fromtimestamp(proc.create_time()))
            if current_time <= x:
                current_time += 86400
            python_today = current_time - x
            print("Python programmed today: %s " % str(time(python_today)))
            if int(python_day) != x:
                lastsave_python = lastsave_python + python_today
                python_run.seek(0)
                python_run.write(str(x))
                print("Common Python programming hours: %s " % str(time(lastsave_python)))
                python_file.seek(0)
                python_file.write(str(lastsave_python))
                python_file.close()
            else:
                print("Common Python programming hours: %s " % str(time(lastsave_python)))
                python_file.seek(0)
                python_file.write(str(lastsave_python))
                python_file.close()
                pass

        if proc.name() == PROCNAME2:
            x = to_integer(datetime.datetime.fromtimestamp(proc.create_time()))
            if current_time <= x:
                current_time += 8640
            cpp_today = current_time - x
            print("C++ programmed today: %s " % str(time(cpp_today)))
            lastsave_cpp = lastsave_cpp + cpp_today
            cpp_file.seek(0)
            cpp_file.write(str(lastsave_cpp))
            cpp_file.close()
            print("Common C++ programming hours: %s " % str(time(lastsave_cpp)))

        if proc.name() == PROCNAME3:
            x = to_integer(datetime.datetime.fromtimestamp(proc.create_time()))
            if current_time <= x:
                current_time += 86400
            sublime_today = current_time - x
            print("Worked in Sublime today: %s " % str(time(sublime_today)))
            lastsave_sublime = lastsave_sublime + sublime_today
            common_file.seek(0)
            common_file.write(str(lastsave_sublime))
            common_file.close()
        else:
            pass

    print("Total programming hours: %s " % str(time(lastsave_python + lastsave_cpp + lastsave_sublime)))

    python_run.close()
    cpp_run.close()
    sublime_run.close()



