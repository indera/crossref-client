
# http://wokinfo.com/mbl/publishers/
# https://images.webofknowledge.com/WOK46/help/WOS/0-9_abrvjt.html
# http://www.publishersglobal.com/directory/list-countries/
#
# TO read
# http://sciencewatch.com/sites/sw/files/sw-article/media/sw-journal-selection-white-paper.pdf
#
get_publishers_count:
	@# curl -s http://api.crossref.org/members?rows=0 | python -m json.tool | grep total-results
	python crossref-client.py -c

get_publishers:
	python crossref-client.py
