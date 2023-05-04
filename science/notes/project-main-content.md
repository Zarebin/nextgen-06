session 02.02.12
	- Parser
		- bs4
		- lxml
		- **[selectolax](https://github.com/rushter/selectolax)**
	=> ~ 3s
	---
	
	```
>>> 	tree = HTMLParser('<div>Get <img src="" alt="Laptop"></div>')
>>> 	img = tree.iter(...)
	```
	
	`iter`(_self_, _include_text=False_)[](https://selectolax.readthedocs.io/en/latest/parser.html#selectolax.parser.Node.iter "Permalink to this definition")
	
	Iterate over nodes on the current level.
	
	- lack of any find method
	
	python
	- comparision objects 
		- ==
			- values (using __eq__)
		- is
			- refrence
	
	using a generated hash and insert it in the nodes
	e.g. : to compare `<tag1>` and `<tag1>`  we could put a hash such as:
	`<tag1 hassan='hash'>` 
	
	
	
	---
	### Profiling:
	- The Python Profilers[¶](https://docs.python.org/3/library/profile.html#the-python-profilers "Permalink to this headline")
	- time.time()
	---
	
	Data structure 
	- numpy
	
	----
	Data
	- k-fold
	
	RForest 
	- overefit 
		- depth (3-5)
		- loss, overfit, curve 
	
	---
	Check other algorithms:
	- BiLSTM
		- sequesnce,
		- position of tags
	
	---
	Hazm -> Stanford
	- but not in project (generally)
	--- 
	1. my feature arryay: array [feature1, feature2,...] 
	2. tags
	``` html
	<p>
		<div>
			<span>
				I am main content
			</span>
		</div>
	</p>
	```
	
	[div, p, a, span, img]
	e.g. [1, 1, 0, 1 , 0]
	
	final feature: [1, 1, 0, 1 , 0] + [my feature arryay]
	
	----
	not balance (+1, -149 per html page) 
	- ignore 50% of html string form bottomn
	- childs of any positive tag could be in positive class
	- Reshape (using numpy)
	- SOMOTE technique for imbalanced data
	- 
	---
	diversity of data
	- 60 news agency and 10 pages from each one
	---
	
	- diflib?
		- similarity between nodes
	- hash in tags?
		- to find a node visited before
	
	
	Overhead: 100-200 ms
	Total runtime to detect main content in a (html) page
