from typing import *
import numpy as np 
from scipy.stats import zscore

class Features():
    '''
    #FIXME: implement functions to extract feature vector from a parsed page 
    '''


    def __init__(self, html_object, n_negative_sample = 10): 
        self.html_object = html_object
        self.og_desc_text = self.find_og_desc_text(html_object)
        self.n_negative_sample = n_negative_sample
        self.desired_tags = ['h1', 'p', 'div']
        self.tag_index = {'div' : 0, 'p': 1, 'h1':2}
        pass

    def get_feature_vectors(self, ) -> Tuple[np.ndarray, List[np.bool8]]: 
        '''
        return a tuple containing the feature vectors alongside of their correspounding labels
        '''
        features = []
        labels = []
        count = 0

        for leaf in self.html_object.body.traverse(include_text=True): 
            node_text = leaf.text(deep=False, separator='', strip=True)
          
            if leaf.tag in self.desired_tags and len(node_text) > 0:
                count += 1

                features.append(self.get_feature_leaf(leaf, node_text))
                labels.append(self.check_label(node_text))
            
            if count >= self.n_negative_sample : 
                break
        
        return [features, labels]

    def check_label(self, node_text : str) -> bool:
        if self._is_description_node(node_text):
            return 1
        else:
            return 0

    def find_og_desc_text(self, page : object) -> str:
        head = page.css_first('meta[property="og:description"]')
        if head is None:
            return None

        og_description = head.attributes.get('content')
        if og_description is None:
            return None
        return og_description


    def _is_description_node(self, node_text : str) -> bool:
        return True if node_text == self.og_desc_text else False



    def get_feature_leaf(self, node: object, node_text: str) -> np.ndarray: 
        present_nodes = self._get_present_tags(node)
        depth = self._extract_depth(node)
        lenght = self._extract_text_lengh(node_text)
        word_count = self._extract_word_count(node_text)

        return [lenght, depth, word_count]



    def _get_present_tags(self, node) -> np.ndarray:
        '''
        returns the present tags of a specefic node as a fixed-size binary array
        ex: [p, div, h1, ...] -> [1, 0, 2, 0, 0, ...]
        '''

        parent_tag = node.parent.tag
        #TODO
        return []


    def _extract_depth(self, node: object) -> int:
        """Write a function to extract the text_lenght inside the lxml_object
        Args:
            lxml_object: a lxml object for each node, children involved
        Returns:
            None
        """
        depth = 0

        while(node.tag != 'body'):
            depth+=1
            node = node.parent
        
        return depth

    def _extract_text_lengh(self, node_text: str) -> int:

        """Write a function to extract the text_lenght inside the lxml_object
        Args:
            lxml_object: Dictionary of line data for the coverage file.
        Returns:
            None
        """
        return len(node_text)



    def _extract_word_count(self, node_text: str) -> int:
        """Write a function to extract the text_lenght inside the lxml_object
        Args:
            node: Dictionary of line data for the coverage file.
        Returns:
            None
        """
        return len(list(node_text.split()))
