
class HTMLNode():

    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        if self.props is None:
            return ""
        props_html = ""
        for prop in self.props:
            props_html += f'{prop}=\"{self.props[prop]}\" '
        return props_html.strip()

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})"


class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag=tag, value=value,props=props, children=None)

    def to_html(self):
        if not self.value:
            raise ValueError("All leaf nodes must have a value.")
         
        if not self.tag:
            return self.value
        else:
            return f"<{self.tag}>{self.value}</{self.tag}>"
        

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, value=None, children=children, props=props)

    def to_html(self):
        if not self.tag:
            raise ValueError("No Tag!")
        if not self.children:
            raise ValueError("No Children, This Is Not a Parent Node")
        
        value = ""
        for child_element in self.children:
            value += child_element.to_html()
        return f"<{self.tag}>{value}</{self.tag}>"