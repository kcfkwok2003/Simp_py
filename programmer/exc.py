import sys, string, traceback

def get_exc_details():
    type,val,tb = sys.exc_info()
    details = string.join(traceback.format_exception(type,val,tb),'')
    return details
