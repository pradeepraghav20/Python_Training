def set_grade(avg_marks):
    def get_grade(marks):
        print ("decoo called")
        avg_marks1=avg_marks(marks)
        if (avg_marks1>20):
            print("C")

        return  avg_marks(marks)
    return get_grade


@set_grade
def avg_marks(marks):
    avg_marks=sum(marks)/len(marks)
    return  avg_marks


marks=[10,20,30,40,50]
print (avg_marks(marks))



# def decorator_func(func):
# def wrapper_func():
# print("wrapper_func Worked")
# return func()
# print("decorator_func worked")
# return wrapper_func
# def show():
# print("Show Worked")
# decorator_show = decorator_func(show)
# decorator_show()