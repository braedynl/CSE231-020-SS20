#################################
## CSE 231
## Debug exercise for Lab 5
## print() not allowed
## @amirootyet
#################################

fp = open('data.txt')  # open the file; set breakpoint
total_height = 0       # keep track of total height

for line in fp:
    name = line[:20]
    height = line[12:20]
    total_height += float(height.strip())
    
fp.close()

fp = open('data2.txt', 'w')  # open another file in write mode
fp.write(str(total_height))