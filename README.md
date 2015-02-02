# Text_Processing_Classes

These classes (so far just Text()) perform basic text prcocessing tasks, such as standardizing text to utf8 encoding, stripping punctuation, cleaning out html tags, tokenization, part-of-speech tagging, lemmatization, frequency distribution tables, etc. Many leverage NLTK but add to its functionality or package it for ease of use.

Eventually I hope to add Corpus-level functionalities such as  vector space conversion, tf-idf weighting, etc. 

# Usage

1. import classes at the beginning of any python script, like so

<pre>import text_process_classes</pre>

2. Instantiate with a source text 

<pre>
my_string = "Hello, world"
a = Text(my_string)</pre>

3. Set the purge_html parameter (default is True)
<pre>my_string = "Hello, world"
a = Text(my_string, False)</pre>

4. Run lemmas and parts of speech via methods (these don't run on instantiation, as they are memory heavy)
<pre>
my_text= "run runs hello, world!"
a = Text(my_text)
a.lemmatize()
a.pos_tag()
    
print a.lemma_list
print a.pos_tuples
## ['run', 'run', 'hello', 'world']
## [('run', 'NN'), ('runs', 'VBZ'), ('hello', 'NN'), ('world', 'NN')]
</pre>
