#-----To beat or not to beat?------

#-----From a conversation between two programmers:

# – Well, imagine you have 1000 rubles...

# – Nooo, let's round it... let’s say I have 1024 rubles.

# This programmer joke shocks people who are not into computers. Indeed, it’s quite hard to understand why the number 1024 is considered “round.” It’s because computers work in the binary system, and 1024 in binary is one followed by ten zeros: 10000000000. For a computer, this is round. That’s why derived measurements in computing are based on 1024, not 1000 as in everyday units (1 kg = 1000 g, 1 km = 1000 m, etc.).

# Organize memory output for a beginner programmer. You need to write a program so that the computed values in the top line are displayed right before printing and are substituted in place of XXXX.

# 1 bit — the smallest unit of information.

# 1 byte = 8 bits.

# 1 kilobit = 1024 bits.

# 1 kilobyte = 1024 bytes.

# 1 kilobyte = XXXX bits.

# Output format
# Memory filled in 5 lines.


#===========================================================================================
#==============SOLUTION=============


bits_in_byte = 8
bytes_in_kilobyte = 1024

kilobyte_in_bits = bytes_in_kilobyte * bits_in_byte

print("1 bit is the minimum unit of information.")
print("1 byte = 8 bits.")
print("1 Kilobit = 1024 bits.")
print("1 Kilobyte = 1024 bytes.")
print(f"1 Kilobyte = {kilobyte_in_bits} bits.")