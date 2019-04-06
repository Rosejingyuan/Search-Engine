import json
from nltk.stem.snowball import SnowballStemmer


def get_json(indexFile):
    with open(indexFile) as handle:
        return json.load(handle)


def get_query_url(query):
    index_file = "/Users/jingyuan_wang/Downloads/WEBPAGES_RAW/Index_Copy.json"
    index = get_json(index_file)

    stemmer = SnowballStemmer('english')
    for term in query:
        stem_term = stemmer.stem(term.lower()).encode('utf-8')

        entry = index[stem_term]
        documents = entry.keys()

        MapFile = "/Users/jingyuan_wang/Downloads/WEBPAGES_RAW/bookkeeping.json"
        hash = get_json(MapFile)
        count = 0
        with open('/Users/jingyuan_wang/Downloads/WEBPAGES_RAW/' + term + '.txt', 'w') as f:
            for k in documents:
                baseUrl = hash[k.decode('utf-8')].encode('utf-8')
                count += 1
                print>>f, baseUrl, '\n'
            print>>f, "Number of urls:" , count

query = ['Informatics', 'Mondego', 'Irvine' ]
get_query_url(query)
