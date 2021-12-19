import keyboard as k

repeats = 10 # How many times you want the program to repeat the keyboard recording. Default: 10
go = 'ctrl' # Button to continue the program. Default: ctrl
spd = 1 #how many times quicker or slower you want the replay to be. (1 is normal speed!)
abortKey = 'insert' #Hold down this button while the program is repeating and it will end prematurely as a failsafe. Default: insert

k.wait(go)
print('---STARTING RECORDING---')
recording = k.record(until=go)
print('---FINISHED RECORDING---')

k.wait(go)
print('---REPLAYING---')

count = 0

while True:
    k.play(recording, speed_factor=spd)
    count=count+1
    print('Repeat number:',count)
    if count == repeats:
        break
    if k.is_pressed(abortKey):
        print('---PROGRAM ABORTED---')
        break

print('---PROGRAM FINISHED---')

#credits -- Hobbson
