RoadrunnerServer Python Project
===============================

This Project is the Server Component of the Roadrunner Project.
Currently it only contains a UDP Timeservice.

Dependencies
------------

	Python 2.7

Using the Service
-----------------

	1. Create an UDP Request to `roadrunner.server:10500` or create a TCP Request to `roadrunner.server:10501
	2. Wait for UDP Response and receive a package with size 1024
	3. The Server Response will be a UTC Timestamp


