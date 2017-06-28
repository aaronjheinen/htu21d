IR Thermometer - MLX90614
======

Read temperature from an IR Thermometer.

Properties
----------
* **Platform**: Platform

Dependencies
------------
None

Commands
--------
None

Input
-----
Any list of signals.

Output
------
Each signal has a `temperature` attribute added to the input signal.

If the sensors fails to read from either sensors, the new attribute value will be `None`.
