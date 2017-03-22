ea = ScreenEA()

# Loop through all the functions
for f in Functions(SegStart(ea), SegEnd(ea)):

    # For each of the incoming references
    for ref in CodeRefsTo(f, 0):

        
        # Get the name of the referring function
        caller_name = GetFunctionName(ref)
        caller_addr = GetFunctionAttr(ref, FUNCATTR_START)

        called_name = GetFunctionName(f)
    
        if called_name == "strcpy" or  called_name == "sprintf" or called_name == "strncpy" or called_name == "wcsncpy" or called_name == "swprintf":
            print("%s:%s:%s\n" %(caller_name, hex(id(caller_addr)), called_name))

