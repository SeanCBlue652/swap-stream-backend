from spotify import library
from spotify import auth_new
def test():
    new_sp = auth_new.run()
    lib = library.Library(new_sp)
    return lib