from typing import *
import numpy as np 

class Features():
    '''
    #FIXME: implement functions to extract feature vector from a parsed page, 
    '''


    def __init__(self, html_lxml_object): 
        self.html_lxml_object = html_lxml_object
        self.og_text = self.find_og_desc_text(html_lxml_object)
        pass


    def get_feature_vectors(self, ) -> Tuple[List[np.ndarray[np.float16]], List[np.bool8]]: 
        '''
        return a tuple containing the feature vectors alongside of their correspounding labels
        '''
        features = []
        labels = []
        for leaf in self.leaf_nodes: 
            features.append(self.get_feature_leaf(leaf))
            labels.append(self.check_label(leaf))



    def _extract_leafs(self, ): 
        desired_tags = ['a', 'h1', 'p', 'div', 'article', 'span']
        leaf_nodes = [node for node in 
                    self.html_lxml_object[0].body.css('*:not(:has(*))') 
                    if node.tag in desired_tags 
                        and node.text(deep=False).strip()]
        self.leaf_nodes = leaf_nodes



    def _find_og_desc_text(page):
        head = page.css_first('head')
        if head is None:
            return None
        
        og_description = head.css_first('meta[property="og:description"]')
        if og_description is None:
            return None
        return og_description.attributes.get('content')



    def _is_description_node(self, node):
        return True if node.text_content() == self.og_text else 0
            


    def _get_feature_leaf(self, node_lxml_object) -> np.ndarray[np.float16]: 
        present_nodes = self._get_present_tags(node_lxml_object)
        lenght = self._extract_text_lengh(node_lxml_object)
        depth = self._extract_depth(node_lxml_object)
        word_count = self._extract_word_count(node_lxml_object)



    def _get_present_tags(self, lxml_object) -> np.ndarray[np.bool8]:
        '''
        returns the present tags of a specefic node as a fixed-size binary array
        ex: [p, div, a, h1, ...] -> [1, 0, 2, 0, 0, ...]
        '''
        #FIXME



    def _extract_depth(self, lxml_object: object) -> int:
        """Write a function to extract the text_lenght inside the lxml_object

        Args:
            lxml_object: a lxml object for each node, children involved
        Returns:
            None
        """
        return list(lxml_object.text_content().split())



    def _extract_text_lengh(self, lxml_object: object) -> int:
        """Write a function to extract the text_lenght inside the lxml_object

        Args:
            lxml_object: Dictionary of line data for the coverage file.

        Returns:
            None
        """
        return len(lxml_object.text_content())




    def _extract_word_count(self, lxml_object: object) -> int:
        """Write a function to extract the text_lenght inside the lxml_object

        Args:
            lxml_object: Dictionary of line data for the coverage file.

        Returns:
            None
        """
        return list(lxml_object.text_content().split())


