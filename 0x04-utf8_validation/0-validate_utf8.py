#!/usr/bin/python3
"""
method that determines if a given data set represents a valid UTF-8 encoding
"""
def validUTF8(data):
    """
    validate input data for valid UTF-8 encoding
    """
    # Number of bytes in the current UTF-8 character
    num_bytes = 0
    
    # Masks to check the most significant bits
    mask1 = 1 << 7
    mask2 = 1 << 6
    
    # Iterate through each integer in the data list
    for byte in data:
        mask = 1 << 7
        if num_bytes == 0:
            # Determine how many bytes are in the current UTF-8 character
            while mask & byte:
                num_bytes += 1
                mask = mask >> 1
                
            # 1 byte character (0xxxxxxx)
            if num_bytes == 0:
                continue
            
            # Invalid scenarios for UTF-8
            if num_bytes == 1 or num_bytes > 4:
                return False
        else:
            # Check if the current byte is a valid continuation byte (10xxxxxx)
            if not (byte & mask1 and not (byte & mask2)):
                return False
        
        num_bytes -= 1
    
    # If num_bytes is not 0, it means we have leftover bytes that were expected to be part of a character
    return num_bytes == 0
