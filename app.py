from pyzt import inputs,inputi
import platform
import  settings
# print(platform.python_version())
# print(platform.platform())
# print(platform.system())
if __name__=='__main__':
    if platform.python_version()[0]=='3':
        import control
        control1 = control.Control()
        if settings.DEBUG:
            print("DEBUG MODE")
        else:
            control1.run()
    else:
        exit('SHOP :Unsupported Python Version')
