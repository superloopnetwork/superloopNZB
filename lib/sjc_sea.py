######################## FUNCTIONS ##############################
import subprocess

def sjc_sea(directory):
	print 'mv ~/movies/%s /mnt/sanjose/' % directory
	mv = subprocess.call('tee /mnt/sanjose/%s /mnt/seattle/%s < ~/movies/%s >/dev/null' % (directory,directory,directory), shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
	mv = subprocess.call('rm -rf ~/movies/%s' % directory, shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
	print 'mv complete'
