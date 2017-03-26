
## Print a list of exports.


for i in range(GetEntryPointQty()):
    ord = GetEntryOrdinal(i)
    if ord == 0:
        continue
    addr = GetEntryPoint(ord)
    
    # Each call made by exported function.
    for original_call in CodeRefsFrom(addr, 0):
        # Sets called_name to function being called directly by exported function.
        called_name = GetFunctionName(original_call)
        # Print "Name of Exported Function:called_name" if any of the desired functions are found.
        if called_name == "strcpy" or  called_name == "sprintf" or called_name == "strncpy" or called_name == "wcsncpy" or called_name == "swprintf":
                        print("%s:%s\n" %(GetFunctionName(addr), called_name))
        
        # One call deep into called function.
        for deep_1 in CodeRefsFrom(original_call, 0):
            # Sets called_name to function being called by original_function.
            called_name = GetFunctionName(deep_1)
            # Print "Name of Exported Function:called_name" if any of the desired functions are found.
            if called_name == "strcpy" or  called_name == "sprintf" or called_name == "strncpy" or called_name == "wcsncpy" or called_name == "swprintf":
                        print("%s:%s\n" %(GetFunctionName(addr), called_name))
            
            # Two calls deep into called function.
            for deep_2 in CodeRefsFrom(deep_1, 0):
                # Sets called_name to function being called by deep_1.
                called_name = GetFunctionName(deep_2)
                # Print "Name of Exported Function:called_name" if any of the desired functions are found.
                if called_name == "strcpy" or  called_name == "sprintf" or called_name == "strncpy" or called_name == "wcsncpy" or called_name == "swprintf":
                        print("%s:%s\n" %(GetFunctionName(addr), called_name))
                
                # Three calls deep into called function.
                for deep_3 in CodeRefsFrom(deep_2, 0):
                    # Sets called_name to function being called by deep_2.
                    called_name = GetFunctionName(deep_3)
                    # Print "Name of Exported Function:called_name" if any of the desired functions are found.
                    if called_name == "strcpy" or  called_name == "sprintf" or called_name == "strncpy" or called_name == "wcsncpy" or called_name == "swprintf":
                        print("%s:%s\n" %(GetFunctionName(addr), called_name))