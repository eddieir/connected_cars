






The core of the simultaor is Python running a local web server through
[Flask](http://flask.pocoo.org/docs/installation).  The user interface is
accessed through a web browser pointed at localhost.  The Simulator also listens
for incoming network connections from the OpenXC Enabler, running on an Android
device.


In order to Install the simulator you could clone it from the following link:
https://github.com/eddieir/connected_cars.git

After cloning the repository we need to install the Python and the pip(in the case of absence of Python and pip) 

The next step before running the simulator is installing all python dependencies simply by typing : pip install -r requirements.txt

After installation of all dependecies we could run the simulator by typing ./simulator.py

To open the UI, open a browser and navigate to http://localhost:50000/


Set the host address to the address of the machine running the simulator and set
the port to 50001. The terminal running the simulator should indicate that it
received a new connection.If the Enabler fails to connect, you may need to use a different IP address.The python address detection isn't perfect, and multiple IPs on a computer can confuse it.

## under the curtain of this simulator 

The Simulator is comprised of three main components:  The State Manager, The User
Interface, and the Dynamics Model.

### User Interface (UI)
The GUI allows the real-time user input such as pedals,gear,etc).The
GUI also displays the outgoing data to the user.  This is not intended to be any
sort of video game, nor a simulation of the driving experience.  It is only
intended to simulate the data that might be generated on the CAN bus

simulator.py

This is the Python script that sets everything in motion.  It starts the Flask
server, creates the State Manager object, provides data to the UI, and handles
user input.

templates/layout.html

templates/vehicle_controls.html

These provide the html code for the user interface.  They provide the framework
in which the jQuery components work.



static/simulator_scripts.js

This has all the JavaScript code for the UI.  The majority of this file is code
handling the jQuery elemenents.  It also contains the loop that polls the
Dynamics Model for data every second, and displays it.

### State Manager

The Stage Manager keeps track of the simulation’s current state, and handles
sending that information to the TCP connection, the GUI, and the Dynamics Model.
The State Manager does not regulate data internal to the Dynamics Model.  (Air
drag, road friction, etc.)  Nor will it be updated as fast.

state_manager.py

The State Manager object receives incoming user input, monitors the dynamics
model, and sends data to any connected Enablers.  It creates and stores the
Dynamics Model object and Enabler Connection object.  It creates and maintains
the loops that send the regular data to the Enabler.

