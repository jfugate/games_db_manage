#!/usr/bin/python3

import psycopg2, argparse, json

''' This script will add, retreive, or update values 
    to the local postgresql "video_games"database'''

#Define, parse, and call functions based on command line arguments
def parse_args():
	parser = argparse.ArgumentParser()
	parser.add_argument("-d", "--databse", help="Name of databse to connect to.", action="store", dest="dbname")
	parser.add_argument("-a", "--add", help="Add new data to the table.", action="store_true", default=False, dest="add_new")
	parser.add_argument("-t", "--table", help="Name of table to operate within.", action="store", dest="table_name")
	parser.add_argument("-R", "--remove", help="Remove a row from the database.", action="store_true", default=False, dest="del_row")
	parser.add_argument("-u", "--update", help="Update a row with new values.", action="store_true", default=False, dest="update_row")
	parser.add_argument("-i", "--id", help="data id from the table to interact with (pair with -s, -u, -R)", action="store_true", type="str", dest="item_id")
	parser.add_argument("-n", "--name", help="Name field. case insensitive when searching, also used with --add", action="store", dest="item_name")
	parser.add_argument("-g", "--genre", help="Genre Field. case insensitive when searching, also used with --add", action="store", dest="item_genre")
	parser.add_argument("-j", "--json", help="Submit JSON form for defining data (pair with add, remove, update, select)", action="store", dest="json_blob")
	parser.add_argument("-s", "--select", help="Run a select query against the database. Use other script options to build where clause", action="store_true", default=False, dest="select_row")

	results = parser.parse_args()

	if results.dbmname:
		if results.table_name:
			if results.add_new:
				pass
			elif results.select_row:
				pass
			elif results.update_row:
				pass
			elif results.del_row:
				pass
			else:
				print("No action chosen between Select, Add, Update, Remove. Try again.")
				parser.print_help()
		else:
			print("Missing Table Name! Try again!")
			parser.print_help()
	else:
		print("Missing Database Name! Try again!")
		parser.print_help()
