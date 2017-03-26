ea = ScreenEA()


# Loop through all the functions.
for f in Functions(SegStart(ea), SegEnd(ea)):

    # For each of the incoming references.
    for ref in CodeRefsTo(f, 0):

        
        # Get the name of the referring function.
        caller_name = GetFunctionName(ref)
        # Get the address of the referring function.
        caller_addr = GetFunctionAttr(ref, FUNCATTR_START)

        # Get the name of the function being called.
        called_name = GetFunctionName(f)
    
        # If the called function is any of the desired functions, print "Name of caller function:Address of caller function:Name of called function".
        if called_name == "strcpy" or  called_name == "sprintf" or called_name == "strncpy" or called_name == "wcsncpy" or called_name == "swprintf":
            print("%s:%s:%s\n" %(caller_name, hex(id(caller_addr)), called_name))


