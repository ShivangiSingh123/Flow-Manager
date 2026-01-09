def task1():
	print("Task 1 : Fetching data")
	return True

def task2():
	print("Task 2 : Processing data")
	return True

def task3():
	print("Task 2 : Storing data")
	return True


TASK_REGISTRY = {"task1" : task1,
                 "task2" : task2,
		 "task3" : task3}