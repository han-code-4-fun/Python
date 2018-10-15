# Write a procedure download_time which takes as inputs a file size, the
# units that file size is given in, bandwidth and the units for
# bandwidth (excluding per second) and returns the time taken to download 
# the file.
# Your answer should be a string in the form
# "<number> hours, <number> minutes, <number> seconds"

# Some information you might find useful is the number of bits
# in kilobits (kb), kilobytes (kB), megabits (Mb), megabytes (MB),
# gigabits (Gb), gigabytes (GB) and terabits (Tb), terabytes (TB).

#print 2 ** 10      # one kilobit, kb
#print 2 ** 10 * 8  # one kilobyte, kB

#print 2 ** 20      # one megabit, Mb
#print 2 ** 20 * 8  # one megabyte, MB

#print 2 ** 30      # one gigabit, Gb
#print 2 ** 30 * 8  # one gigabyte, GB

#print 2 ** 40      # one terabit, Tb
#print 2 ** 40 * 8  # one terabyte, TB

# Often bandwidth is given in megabits (Mb) per second whereas file size 
# is given in megabytes (MB).
def convert_seconds(input):
    result=[0,0,0]
    while input >= 3600:
        input = input - 3600
        result[0]=result[0] + 1
    while input< 3600 and input >=60:
        input = input - 60
        result[1]=result[1] + 1
    while input <60:
        result[2] = input
        h = 'hour'
        m = 'minute'
        s = 'second'
        if result [0] != 1:
            h = 'hours'
        if result [1] != 1:
            m = 'minutes'
        if result [2] != 1: 
            s = 'seconds'
        output = str(result[0])+' '+h+', '+str(result[1])+' '+m+', ' + str(result[2]) + ' '+s
        return output


def download_time(fileSize,fileUnit,bandSize, bandUnit):
    if fileUnit =='kb':
        fileSize = fileSize * 2 **10
    if fileUnit =='kB':
        fileSize = fileSize * 2 **10 *8
    if fileUnit =='Mb':
        fileSize = fileSize * 2 **20
    if fileUnit =='MB':
        fileSize = fileSize * 2 **20*8
    if fileUnit =='Gb':
        fileSize = fileSize * 2 **30
    if fileUnit =='GB':
        fileSize = fileSize * 2 **30*8
    if fileUnit =='Tb':
        fileSize = fileSize * 2 **40
    if fileUnit =='TB':
        fileSize = fileSize * 2 **40 *8
        
    if bandUnit == 'kb':
        bandSize = bandSize * 2 **10
    if bandUnit == 'kB':
        bandSize = bandSize * 2 **10 * 8
    if bandUnit == 'Mb':
        bandSize = bandSize * 2 **20
    if bandUnit == 'MB':
        bandSize = bandSize * 2 **20* 8
    if bandUnit == 'Gb':
        bandSize = bandSize * 2 **30
    if bandUnit == 'GB':
        bandSize = bandSize * 2 **30*8
    if bandUnit == 'Tb':
        bandSize = bandSize * 2 **40
    if bandUnit == 'TB':
        bandSize = bandSize * 2 **40*8

    tempTime = fileSize*1.0 / bandSize
    
    return convert_seconds(tempTime)



print download_time(1024,'kB', 1, 'MB')
#>>> 0 hours, 0 minutes, 1 second

print download_time(1024,'kB', 1, 'Mb')
#>>> 0 hours, 0 minutes, 8 seconds  # 8.0 seconds is also acceptable

print download_time(13,'GB', 5.6, 'MB')
#>>> 0 hours, 39 minutes, 37.1428571429 seconds

print download_time(13,'GB', 5.6, 'Mb')
#>>> 5 hours, 16 minutes, 57.1428571429 seconds

print download_time(10,'MB', 2, 'kB')
#>>> 1 hour, 25 minutes, 20 seconds  # 20.0 seconds is also acceptable

print download_time(10,'MB', 2, 'kb')
#>>> 11 hours, 22 minutes, 40 seconds  # 40.0 seconds is also acceptable

print download_time(11,'GB', 5, 'MB')
#>>> 0 hours, 37 minutes, 32.8 seconds 


