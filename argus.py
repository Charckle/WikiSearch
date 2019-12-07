import os.path
from whoosh.index import create_in
from whoosh.fields import Schema, TEXT
from whoosh.index import open_dir
from whoosh.query import *
from whoosh.qparser import QueryParser
from modules import web_module

class WSearch():
    def __init__(self, storage_location = "data\\"):
        
        self.storage_location = storage_location
        
    def create_index_object_file(self, schema):
        if not os.path.exists(".index"):
            os.mkdir(".index")
        ix = create_in(".index", schema)
        
        return ix
    
    def index_create(self):
        
        schema = Schema(file_name=TEXT(stored=True), content=TEXT)
        
        ix = self.create_index_object_file(schema)
        
        files = []
        # r=root, d=directories, f = files
        for _, _, f in os.walk(self.storage_location):
            for file in f:
                if '.txt' in file:
                    files.append(os.path.join(self.storage_location, file))
                    
        
        writer = ix.writer()
        
        for f in files:
            with open(f'{f}', 'r') as file:
                data = file.read().replace('\n', '')
                
                writer.add_document(file_name=u"{}".format(f), content=u"{}".format(data))                
            #print(f)
            
        writer.commit()
    
    def index_create_from_wiki(self, wiki_http):
        schema = Schema(file_name=TEXT(stored=True), content=TEXT)
        
        ix = self.create_index_object_file(schema)
        
        #get text data from web articles
        articles = web_module.ih_web_scrap(wiki_http)  #"https://wiki.razor.si"
        #
        
        writer = ix.writer()
        
        for link, data in articles:
            
            writer.add_document(file_name=u"{}".format(link), content=u"{}".format(data))
        
        writer.commit()

    def index_search(self,querystring):
        
        ix = open_dir(".index")
        
        parser = QueryParser("content", ix.schema)
        myquery = parser.parse(querystring)
        
        file_names = []
        with ix.searcher() as searcher:
            results = searcher.search(myquery)
            print(f"Found {len(results)} results.")
            for found in results:
                file_names.append(found["file_name"])
            
            return file_names

        
        
