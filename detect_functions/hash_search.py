first = False
second = False
third = False
fourth = False


# For each of the segments.
for seg in Segments():
    # For each of the defined elements.
    for head in Heads(seg, SegEnd(seg)):
        # If it's data
        if isData(GetFlags(head)):
            # Get address of current data element.
            hash = hex(id(head))
            # Check if address equals any of the desired addresses.
            if hash == "0xd76aa478":
                first = True
            if hash == "0xe8c7b756":
                second = True
            if hash == "0x242070db":
                third = True
            if hash == "0xc1bdceee":
                fourth = True
# If all dersired addresses are found, print "MD5 Constants present".
if first and second and third and fourth:
    print("MD5 Constants present")