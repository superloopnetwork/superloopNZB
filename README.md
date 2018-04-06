# superloopNZB

Problem Statment: Majority, if not all of the newsgroup indexers only permit a single (1) IP address per API. Because the sites only provide one API, this essentially means PVR applications such as sickbeard or sonarr may only be used by a single entity to an indexer. As soon as the index site detects multiple IP addresses from the same API, the usual action is an immediate ban as they restrict account sharing.

Use case: superloopNZB allows multiple users to share a single PRV application. Users would populate their favourite TV shows in the PVR application. Modify the dictionary file to tell superloopNZB where to send the downloaded content to (single or multiple destinations). superloopNZB sits in the background and constantly scans for any new content that has arrived before reacting.

How to use:

Simply execute 'python main.py' in bash. A better option would be to create a daemon so that the python application executes automatically upon start up.

The current scanning directory points to ~/movies. This is the folder where your newsgroup client (sabnzbd) downloads and extracts completed files to. You may modify the destination(s) in the /lib folder. Ideally, destinations should be mounting points to take advantage of this application.
