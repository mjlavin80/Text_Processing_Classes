import nltk
from nltk.stem import WordNetLemmatizer
from nltk import FreqDist
from BeautifulSoup import BeautifulSoup
import string
import urllib

# assumes passing it a text as string
class Text():
    def __init__(self, original_text, purge_html=None):
        if purge_html is None:
            purge_html = True
        self.purge_html = purge_html     
        self.original_text = original_text
        self.process() #define last
        
    # convert fields to utf-8 if text
    def decode_encode_utf8(self):
        try:
            if isinstance(self.original_text, basestring): 
                mystring = self.original_text.encode('utf-8', 'replace')
            else:
                mystring = str(self.original_text).encode('utf-8', 'replace')
        except:
            if isinstance(self.original_text, basestring):
                mystring = self.original_text.decode('utf-8').encode('utf-8', 'replace')
            else:
                mystring = str(self.original_text.decode('utf-8')).encode('utf-8', 'replace')
        self.utf8 = mystring
        #no return statement needed ... only use for getters if you need them
    
    def remove_html_escape(self):
        if self.purge_html is True:
            self.html_decoded= BeautifulSoup(self.utf8, convertEntities=BeautifulSoup.HTML_ENTITIES).getText().encode('utf-8')
        else:
            self.html_decoded= self.utf8
            
    def remove_all_html(self):
        if self.purge_html is True:
            soup = BeautifulSoup(self.utf8) 
            self.html_removed = soup.getText(" ").encode('utf-8')
        else:
            self.html_removed = self.utf8
        
    def sub_punct_for_windows_crap(self):
        windows_codes = {"'":"\xe2\x80\x98", "'":"\xe2\x80\x99", """: "\xe2\x80\x9c", """:"\xe2\x80\x9d", "-":"\xe2\x80\x93", "--":"\xe2\x80\x94", "...":"\xe2\x80\xa6"}
        for i,j in windows_codes.iteritems():
            if j != "\xe2\x80\x94" and j != "\xe2\x80\xa6" and j != "\xe2\x80\x93":
                self.html_removed = self.html_removed.replace(j, "")
        self.utf8_no_windows_chars = self.html_removed.replace("\xe2\x80\x94", " ").replace("\xe2\x80\xa6", "...").replace("\xe2\x80\x93", "-")
        
    #removes unicode punctuation
    def remove_punctuation(self):
        self.no_punctuation = self.utf8_no_windows_chars.translate(string.maketrans("",""), string.punctuation)
    
    #remove extra white spaces, tabs, and newlines
    def remove_whitespace(self):
        self.no_whitespace = ' '.join(self.no_punctuation.split())
        
    def lowercase(self):
        self.lowercase_text = self.no_whitespace.lower()
    
    def tokenize(self):
        self.tokenized_text = nltk.word_tokenize(self.lowercase_text)        
        
    #removes stray punctuation tokens
    def stray_non_alpha_tokens(self):
        for i in self.tokenized_text:
            if i.isalpha()==False:
                self.tokenized_text.remove(i)
    
    def fdist(self, token_list):
        # run a FreqDist on the lemmatized token list
        fdist = FreqDist(token_list)
        return fdist
    
    def lemmatize(self):
        wnl = WordNetLemmatizer()
        self.lemma_list = []

        for i in self.tokenized_text:
            lemmy_word = wnl.lemmatize(i)    
            self.lemma_list.append(lemmy_word)

    def pos_tag(self):    
        #parts of speech
        self.pos_tuples = nltk.pos_tag(self.tokenized_text)
    
    def process(self):
        #decode_encode to utf-8
        self.decode_encode_utf8() #on original
        #strip html and entities
        self.remove_html_escape()
        self.remove_all_html()
        #remove windows BS
        self.sub_punct_for_windows_crap()     
        #remove regular punctuation
        self.remove_punctuation()
        #whitespace
        self.remove_whitespace()
        #lowercase
        self.lowercase()
        self.tokenize()
        self.stray_non_alpha_tokens()
        #lemmas
        #self.lemmatize()
        
        #pos
        #self.pos_tag()

# in if name == main, basic file and url handling
if __name__ == '__main__':
    """
    #test text
    my_text_link = urllib.urlopen('http://www.gutenberg.org/cache/epub/2701/pg2701.txt')
    my_text = my_text_link.read()
    a = Text(my_text)
    
    print a.original_text
    
    string_type = raw_input("Enter 1 for url and 2 for local file and press Return: ")
    
    if string_type == "1":
        #do stuff
        pass
    
    elif string_type == "2":
        pass
    
    else:
        print "Bad command or keyboard error."
        die
    """