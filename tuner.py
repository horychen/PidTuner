from pylab import np, plt

def get_coeffs_dc_motor_current_regulator(R, L, Bandwidth_Hz):
    Kp = Bandwidth_Hz * 2 * np.pi * L
    Ki = R / L
    return Kp, Ki

import control
from control import bode_plot
def display(x):
    pass

R = 3 # Ohm
L = 0.4 # H

Kp, Ki = get_coeffs_dc_motor_current_regulator(R, L, 200)

dc_motor = control.tf([1], [L, R])
pi_regulator = control.tf([Kp, Kp*Ki], [1, 0])
display(dc_motor)
display(pi_regulator)
# figure()
# mag, phase, omega = bode_plot(dc_motor, 2*np.pi*np.logspace(-2,4,1000), dB=1, Hz=1, deg=1)
# figure()
# mag, phase, omega = bode_plot(pi_regulator, 2*np.pi*np.logspace(-2,4,1000), dB=1, Hz=1, deg=1)

open_sys = control.series(pi_regulator, dc_motor)
closed_sys = control.feedback(dc_motor, pi_regulator, sign=-1)

# open_sys = pi_regulator * dc_motor
closed_sys = open_sys / (1+open_sys)

display(open_sys)
display(control.minreal(closed_sys))
closed_sys = control.minreal(closed_sys)

# figure()
# mag, phase, omega = bode_plot(open_sys, 2*np.pi*np.logspace(-2,4,1000), dB=1, Hz=1, deg=1)
plt.figure()
mag, phase, omega = bode_plot(closed_sys, 2*np.pi*np.logspace(-2,4,1000), dB=1, Hz=1, deg=1)

T, yout = control.step_response(closed_sys, np.arange(0,2,1e-4))
plt.figure()
plt.plot(T, yout)

plt.show()












delta = 4 # damping factor

for delta in np.arange(1.0, 50, 2):

    BW_speed = np.arange(5, 100, 10)
    BW_current = BW_speed * (delta + 2.16 * exp(-delta/2.8) - 1.86)

    plt.plot(BW_speed, BW_current, '--')


