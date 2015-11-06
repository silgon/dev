import numpy as np
import matplotlib.pyplot as plt
import matplotlib.widgets as mwidget
# import matplotlib.patches as mpatches

# init plot
fig = plt.figure()
fig.subplots_adjust(left=0, right=1, bottom=0, top=1)
ax = fig.add_subplot(111, aspect='equal', autoscale_on=False,
                     xlim=(0, 1), ylim=(0, 1))
ax.xaxis.set_ticks([])
ax.yaxis.set_ticks([])

circ = plt.Circle((.5, .5), radius=0.07, color='g')
ax.add_patch(circ)

axcolor = 'w'

resetax = plt.axes([0.8, 0.025, 0.1, 0.04])
button = mwidget.Button(resetax, 'Reset', color=axcolor, hovercolor='0.975')

def reset(event):
    circ.center = (.5, .5)
    fig.canvas.draw()
button.on_clicked(reset)
import matplotlib
def onkeypress(key_event):
    # key_event = matplotlib.backend_bases.KeyEvent
    x, y = circ.center
    # print('you pressed', key_event.key)
    if key_event.key== u'up':
        y+=.1
    if key_event.key== u'down':
        y-=.1
    if key_event.key== u'left':
        x-=.1
    if key_event.key== u'right':
        x+=.1
    circ.center = (x, y)
    fig.canvas.draw()
    

cid = fig.canvas.mpl_connect('key_press_event', onkeypress)


rax = plt.axes([0.025, 0.5, 0.15, 0.15], axisbg=axcolor)
radio = mwidget.RadioButtons(rax, ('red', 'blue', 'green'), active=2)

def colorfunc(label):
    circ.set_color(label)
    fig.canvas.draw_idle()
radio.on_clicked(colorfunc)
plt.show()
