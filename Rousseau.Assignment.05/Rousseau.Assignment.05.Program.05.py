# Write a Python program to create a chain of function decorators (bold, italic, underline etc.).
# Console
# Original Message: hello world
# Modified Message: <b><i><u>hello world</u></i></b>
# Specifications
# • Create decorator functions: make_bold(), make_italic(), and make_underLine()
# • Add the decorators to the main function:
def make_bold(fn):
    def wrapper(*args, **kwargs):
        return "<b>" + fn(*args, **kwargs) + "</b>"
    
    return wrapper

def make_italic(fn):
    def wrapper(*args, **kwargs):
        return "<i>" + fn(*args, **kwargs) + "</i>"
    
    return wrapper

def make_underline(fn):
    def wrapper(*args, **kwargs):
        return "<u>" + fn(*args, **kwargs) + "</u>"
    
    return wrapper


@make_underline
@make_italic
@make_bold
def print_message(m):
    return m

def main():

    m="hello world"
    print(f"Original Message: {m}")
    print(f"Modified Message: ", print_message(m))


  
if __name__ == "__main__":
    main()


