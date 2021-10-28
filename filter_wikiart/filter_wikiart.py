import json
from glob import glob
import os

def filter_wikiart(folder_in='wikiart-saved', folder_out='wikiart-filtered', field='genre', target_value='abstract'):
	"""
	this function does the trick of filtering all wikiart entries (artists and their paintings) for a wanted category (e.g. 'genre' or 'style') in the wikiarts annnotations.

	it builds on the 'wikiart' repository by lucasdavid (https://github.com/lucasdavid/wikiart)

	how to use it:
	- download all metainfo from wikiart using lucasdavid's code (takes forever) 
	python3 wikiart.py --datadir ./wikiart-saved/ fetch --only paintings
	- build custom subsets using my function
	- use lucasdavid's code again to download the wanted jpegs
	python3 wikiart.py --datadir wikiart-filtered/field/target-value/ fetch

	author: Dominik Welke, dominik.welke@web.de, https://github.com/dominikwelke

	"""

	# check if artsits.json file exists
	if not os.path.isfile(os.path.join(folder_in, 'meta', 'artists.json')):
		raise FileNotFoundError('artists.json file not in %s. stop execution' % folder_in)

	# create necessary folders
	try:
		os.makedirs(os.path.join(folder_out, 'meta'))
	except FileExistsError:
		pass
	try:
		os.makedirs(os.path.join(folder_out, 'images'))
	except FileExistsError:
		pass 

	
	# get list of all artist json files
	olddir = os.getcwd()
	os.chdir(folder_in)
	json_list = glob(os.path.join('meta', '*.json'))
	json_list = [i for i in json_list if i != os.path.join(folder_in, 'meta', 'artists.json')]
	json_list.sort()
	os.chdir(olddir)


	# loop through artists
	n_artists = len(json_list)  # total number of artists
	c_artists = 0  # counter
	c_artwork = 0  # counter
	keep_artists = []
	for i_artist in range(n_artists):
		# load json
		with open(os.path.join(folder_in, json_list[i_artist])) as f:
			d_artist = json.load(f)

		# subselect the wanted pics
		pics = []
		for pic in d_artist:
			if field in pic:
				if pic[field] == target_value:
					pics.append(pic)


		# save subsetted json to disc
		if pics != []:
			with open(os.path.join(folder_out, json_list[i_artist]), 'w+') as f:
				json.dump(pics,f,indent=True)
			# compile relevant metainfo
			c_artists += 1
			c_artwork += len(pics)
			keep_artists.append(json_list[i_artist])
			



	# clean out and save updated artists.json (important for only downloading the wanted pictures)
	with open(os.path.join(folder_in, 'meta', 'artists.json')) as f:
		artists_json = json.load(f)
	
	artists_json_keep = [art for art in artists_json if any([(art['url'] in arti) for arti in keep_artists])]
	
	with open(os.path.join(folder_out, 'meta', 'artists.json'),'w+') as f:
		json.dump(artists_json_keep, f, indent=True)



	# print a summary
	print('SUMMARY:')
	print('%s - %s' % (field, target_value))
	print('artists - %i out of %i ' % (c_artists, n_artists))
	print('artworks - %i in total' % c_artwork)

	# clean up
	os.chdir(olddir)

