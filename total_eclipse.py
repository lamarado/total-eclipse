# Total Eclipse of The Heart
#
# Based on the flowchart from https://jeannr.tumblr.com/
# specifically on the post
# "I made a flow chart, that we might better understand" at
# https://jeannr.tumblr.com/post/165291081/i-made-a-flow-chart-that-we-might-better
#
# The flowchart is based on the lyrics of the song by Bonnie Tyler
#
# Python code by Lionel
#
# Shameless plug: Our development team is hiring!
# https://www.innovuze.com/careers

def total_eclipse_of_the_heart():
    turn_around(0)

def turn_around(i):
    print("Turn around")
    if i < 4:
        every_now_and_then(i)
    elif i < 6:
        print("Bright eyes")
        every_now_and_then(i)
        if i == 5:
            and_i_need_you(0)
            return
    turn_around(i + 1)
        
def every_now_and_then(i):
    print("Every now and then I")
    if i < 4:
        get_a_little_bit(i)
    elif i < 6:
        print("fall apart")
        
def get_a_little_bit(i):
    print("get a little bit")
    if i==0:
        print("lonely and you're never coming 'round")
    elif i==1:
        print("tired of listening to the sound of my tears")
    elif i==2:
        print("nervous that the best of all the years have gone by")
    elif i==3:
        print("bit terrified and then I see the look in your eyes") 

def and_i_need_you(i):
    print("And I need you")
    if i == 0:
        print("now tonight")
        and_i_need_you(i + 1)
    else:
        print("more than ever!!")
        
total_eclipse_of_the_heart()
