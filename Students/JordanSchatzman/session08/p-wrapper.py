def p_decorate(func):
   def func_wrapper(name):
       return "<p>{0}</p>".format(func(name))
   return func_wrapper
@p_decorate
def return_a_string(string):
    return string

