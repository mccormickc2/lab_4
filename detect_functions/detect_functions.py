## Print a list of in-degree and out-degree for functions

from sets import Set

ea = ScreenEA()

callers = dict()
callees = dict()

# Loop through all the functions
for f in Functions(SegStart(ea), SegEnd(ea)):

    f_name = GetFunctionName(f)

    # Create a set with all the names of the functions calling (referring to)
    # the current one.
    callers[f_name] = Set(map(GetFunctionName, CodeRefsTo(f, 0)))

    # For each of the incoming references
    for ref in CodeRefsTo(f, 0):

        
        # Get the name of the referring function
        caller_name = GetFunctionName(ref)
        caller_addr = GetFunctionAttr(ref, FUNCATTR_START)

        called_name = GetFunctionName(f)
    
        if called_name == "strcpy" or  called_name == "sprintf" or called_name == "strncpy" or called_name == "wcsncpy" or called_name == "swprintf":
            print("%s:%s:%s\n" %(caller_name, hex(id(caller_addr)), called_name))

