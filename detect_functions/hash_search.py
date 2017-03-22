# For each of the segments
for seg in Segments():
    # For each of the defined elements
    for head in Heads(seg, SegEnd(seg)):
        # If it's data
        if isData(GetFlags(head)):
            # Get address of current data element
            hash = hex(id(head))
            if hash == "0xd76aa478" or hash == "0xe8c7b756" or hash == "0x242070db" or hash == "0xc1bdceee":
                print("MD5 Constants present")