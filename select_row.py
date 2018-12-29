#!/usr/bin/python3

'''This script builds the SQL syntax based on
   user provided information in the CLI arguments.
'''

def build_query(results):
	name = results.item_name
	item_id = results.item_id
	genre = results.item_genre
	table = results.table_name
	base_statement = ["select", "*", "from", table]
    if name || item_id || genre:
    	base_statement.append("where")
    	if sum(map(bool, [name, item_id, genre])) == 3:
    		where_clause = " name ilike " + name + " and genre ilike " + genre + " and id = " + item_id
    		full_query = ' '.join(base_statement) + where_clause + ";"
    		return full_query
    	elif sum(map(bool, [name, item_id, genre])) == 2:
    		if name && item_id:
    			where_clause = " name ilike " + name + " and id = " + item_id
    			full_query = ' '.join(base_statement) + where_clause + ";"
    			return full_query
    		elif name && genre:
    			where_clause = " name ilike " + name + " and genre ilike " + genre
    			full_query = ' '.join(base_statement) + where_clause + ";"
    			return full_query
    		elif genre && item_id:
    			where_clause = " genre ilike " + genre + " and id = " + item_id
    			full_query = ' '.join(base_statement) + where_clause + ";"
    			return full_query
    	elif sum(map(bool, [name, item_id, genre])) == 1:
    		if name:
    			where_clause = " name ilike " + name
    			full_query = ' '.join(base_statement) + where_clause + ";"
    			return full_query
    		elif item_id:
    			where_clause = " id = " + item_id
    			full_query = ' '.join(base_statement) + where_clause + ";"
    			return full_query
    		elif genre:
    			where_clause = " genre = " + genre
    			full_query = ' '.join(base_statement) + where_clause + ";"
    			return full_query
    else:
    	return base_statement + ";"