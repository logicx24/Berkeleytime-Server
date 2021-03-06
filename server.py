from pysnap import Snapchat
import userAuth
import sys
import time
import os
import cPickle as pickle

def initialize_and_monitor():
	snapObject = Snapchat()
	snapObject.login(userAuth.USERNAME, userAuth.PASSWORD) #imported from a file called userAuth.py, which has two variables, USERNAME = "USERNAME" and PASSWORD = "PASSWORD"
	added_snaps = []
	if (os.path.isfile("./pickled_files/added_snaps.pkl")):
		added_snaps = pickle.load(open("./pickled_files/added_snaps.pkl", 'rb'))
	try:
		while True:
			snaps = []
			for snap in snapObject.get_snaps():
				if snap['sender'] != 'teamsnapchat' and snap['id'] not in added_snaps:
					snaps.append(snapObject.get_blob(snap['id']))
					added_snaps.append(snap['id'])

			count = 0
			paths = []
			for snap in snaps:
				currpath = 'snap'+ str(count) + ".jpeg"
				if snap:
					with open(currpath, 'wb') as f:
						f.write(snap)
					paths.append(currpath)
					count += 1

			media_ids = [snapObject.upload(path) for path in paths]
			
			for media_id in media_ids:
				is_sent = snapObject.send_to_story(media_id)
				print(is_sent)
			
			for path in paths:
				os.remove(path)
			
			print('Finished one iteration, sleeping for a minute now')
			time.sleep(60)
	except:
		traceback.print_exc(file=sys.stdout)
	finally:
		with open("./pickled_files/added_snaps.pkl", 'wb') as output:
			pickle.dump(added_snaps, output, -1)
		sys.exit()

if __name__ == "__main__":
	initialize_and_monitor()

#storySent = snapObject.send_to_story()
