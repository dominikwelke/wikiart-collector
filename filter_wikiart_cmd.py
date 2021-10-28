from filter_wikiart.filter_wikiart import filter_wikiart
import argparse


if __name__ == '__main__':
	args = []

	parser = argparse.ArgumentParser(description='parameters for wikiart filter function')
	parser.add_argument(
		'-in','--folder_in', type=str, 
		#default='wikiart-saved',
        help='folder with downloaded wikiart metadata')
	parser.add_argument(
		'-out', '--folder_out', type=str, 
		#default='wikiart-filtered',
        help='base folder to store filtered wikiart metadata')
	parser.add_argument(	
		'-f','--field', type=str, 
		#default='genre',
        help='field of wikiart metainfo used to filter the database, e.g. "genre"')
	parser.add_argument(
		'-t', '--target_value', type=str, 
		#default='abstract',
        help='wanted value for the above field, e.g. "abstract"')


	args = vars(parser.parse_args())
	#print(args)

	filter_wikiart(
		folder_in=args['folder_in'], folder_out=args['folder_out'],
		field=args['field'],target_value=args['target_value']
		)
