import json
import urllib,urllib2

def main():
	q = raw_input("Enter something to query the Web: ")
	aa = run_query(q)
	i = 1
	for a in aa:
		print str(i)+". "+a['title']
		print a['link']
		print a['summary']
		print
		i += 1

def run_query(search_terms):
	root_url = 'https://api.datamarket.azure.com/Bing/Search/'
	source = 'Web'
	results_per_page = 10
	offset = 0
	query = "'{0}'".format(search_terms)
	query = urllib.quote(query)
	search_url = "{0}{1}?$format=json&$top={2}&$skip={3}&Query={4}".format(root_url,source,results_per_page,offset,query)
	username = ''
	bing_api_key = 'Aa3b7tGlpnwl4fW9jGu720juX6HAegcnTK9hL4EHm2I'
	password_mgr = urllib2.HTTPPasswordMgrWithDefaultRealm()
	password_mgr.add_password(None,search_url,username,bing_api_key)
	results = []
	try:
		handler = urllib2.HTTPBasicAuthHandler(password_mgr)
		opener = urllib2.build_opener(handler)
		urllib2.install_opener(opener)
		response = urllib2.urlopen(search_url).read()
		json_response = json.loads(response)
		for result in json_response['d']['results']:
			results.append({'title':result['Title'],'link':result['Url'],'summary':result['Description']})
	except urllib2.URLError,e:
		print "Error while querying the BING API: ",e
	return results 

if __name__ == '__main__':
	main()
