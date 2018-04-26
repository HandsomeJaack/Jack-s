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
		for proc in psutil.process_iter():
			current_time = to_integer(datetime.datetime.now())

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

			common_file = open("common_data.txt", "r+")
			lastsave_sublime = common_file.read()
			if lastsave_sublime:
				lastsave_sublime = int(lastsave_sublime)
			else:
				print("Common data file is empty!")

			sublime_run = open("sublime_run.txt","r+")
			sublime_day = sublime_run.read()
			if sublime_day:
				sublime_day = str(sublime_day)
			else:
				print("Latest Sublime Text Editor run file is Empty!")

			if proc.name() == PROCNAME1:
				#print(proc)
				#print(datetime.datetime.fromtimestamp(proc.create_time()).strftime("%Y-%m-%d %H:%M:%S"))
				x = to_integer(datetime.datetime.fromtimestamp(proc.create_time()))

				if current_time <= x:
					current_time += 86400

				python_today = current_time - x - python_today
				lastsave_python = lastsave_python + python_today

			if proc.name() == PROCNAME2:
				#print(proc)
				#print(datetime.datetime.fromtimestamp(proc.create_time()).strftime("%H:%M:%S"))
				x = to_integer(datetime.datetime.fromtimestamp(proc.create_time()))

				if current_time <= x:
					current_time += 8640

				cpp_today = current_time - x - cpp_today
				lastsave_cpp = lastsave_cpp + cpp_today

			if proc.name() == PROCNAME3:
				#print(proc)
				#print(datetime.datetime.fromtimestamp(proc.create_time()).strftime("%H:%M:%S"))
				x = to_integer(datetime.datetime.fromtimestamp(proc.create_time()))
				y = datetime.datetime.fromtimestamp(proc.create_time()).strftime("%Y-%m-%d %H:%M:%S")
				if current_time <= x:
					current_time += 86400

				sublime_today = current_time - x - sublime_today
				lastsave_sublime = lastsave_sublime + sublime_today

		print("Worked in Sublime today: %s " % str(time(sublime_today)))
		print("C++ programmed today: %s " % str(time(cpp_today)))
		print("Python programmed today: %s " %  str(time(python_today)))
		print("Common Python programming hours: %s " %  str(time(lastsave_python)))
		print("Common C++ programming hours: %s " %  str(time(lastsave_cpp)))
		print("Total programming hours: %s " %  str(time(lastsave_python + lastsave_cpp + lastsave_sublime)))

		common_file.seek(0)
		common_file.write(str(lastsave_sublime))
		common_file.close()

		python_file.seek(0)
		python_file.write(str(lastsave_python))
		python_file.close()

		cpp_file.seek(0)
		cpp_file.write(str(lastsave_cpp))
		cpp_file.close()

		python_run.close()
		cpp_run.close()
		sublime_run.close()



