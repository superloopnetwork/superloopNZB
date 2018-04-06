# superloopNZB

Problem Statment: Majority, if not all of the newsgroup indexers only permit a single (1) IP address per api. This essentially means PVR applications such as sickbeard or sonarr may only be used by a single entity.

Use case: superloopNZB allows multiple users to share a single PRV application. Users would populate their favourite TV shows in the PVR application. Modify the dictionary file to tell superloopNZB where to send the downloaded content to (single or multiple destinations). superloopNZB sits in the background and constantly scans for any new content to arrive before reacting.

How to use:

Simply execute 'python main.py' in bash.

The current scanning directory points to ~/movies. This is the folder where you newsgroup client (sabnzbd) downloads and extracts completed files to. You may modify the destination(s) in the /lib folder. To expand on this, destinations may be mounting points.
