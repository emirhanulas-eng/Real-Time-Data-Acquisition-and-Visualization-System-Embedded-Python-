import serial
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time

ESP = serial.Serial("COM6", 9600)

fig, ax = plt.subplots(figsize=(10,6))
ax.set(xlabel="Time [s]",
       ylabel="Analog Input [Bit]",
       title="POT",
       xlim=[0,10],
       ylim=[0,4100])

ax.grid(True, linestyle = "-", linewidth = 0.7)

times = []
value = []
graph, = ax.plot([],[])
starting_time = None

new_int = 0

def update(frame):
    global starting_time
    global input
    global new_int

    input = ESP.readline().decode().strip()

    if starting_time is None:
        starting_time = time.time()

    if input.isdigit():
       value.append(int(input))
       times.append(time.time() - starting_time)

       if times[-1] > 10:
          ax.set_xlim(times[-1]-10, times[-1])

       graph.set_data(times, value)


ani = animation.FuncAnimation(fig, update, interval=50)
plt.show()

