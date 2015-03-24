"""
Interactively plots each of the samples from the dataset
"""
import h5py
import matplotlib.pyplot as plt

libras_fh = h5py.File('libras.hdf5','r')

try:
    fig = plt.figure()
    txt = fig.suptitle('',fontsize=12)
    ax = fig.add_subplot(111)
    line = plt.Line2D((),(),marker='o',markerfacecolor='k')
    ax.add_artist(line)
    ax.grid(which='both')
    ax.minorticks_on()

    databuff = ((x,y,cls) for cls,ds in libras_fh.iteritems() for x,y in ds)
    timer = fig.canvas.new_timer(interval=1000)

    def update():
        x,y,c = databuff.next()
        line.set_data(x,y)
        txt.set_text("Class '%s'" % c)
        fig.canvas.draw()

    def onclick(event):
        update()
        timer.start()

    cid = fig.canvas.mpl_connect('button_press_event', onclick)
    timer.add_callback(update)

    # draw first frame then start
    update()        
    timer.start()

    plt.show()
except KeyboardInterrupt:
    pass
finally:
    plt.close(fig)
    fig.canvas.mpl_disconnect(cid)
