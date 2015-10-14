#!/usr/bin/env python

"""
Python class example.
"""

# The start of it all:
# Fill it all in here.

# indent: start with just x amount of spaces, then use string formatting
# justify right {:>x}

TAB_SIZE = 4


class Element(object):
    def __init__(self, content='', indent=0, **attrs):
        self.tag = ''
        self.indent = indent
        self.children_indent = indent + TAB_SIZE
        self.content = ''
        self.children = []
        self.parent = None
        self.append(content)

    #def __str__(self):
     #   return self.render()

    def render(self, f):
        f.write(self.render_html())

    def render_html(self):
        return u'\n{i}<{t}>{c}{ch}\n{i}</>'.format(
            i=' ' * self.indent,
            t=self.tag,
            c=self.content,
            ch=''.join([child.render_html() for child in self.children]))

    def format_content(self, content):
        return '\n{}{}'.format(' ' * self.children_indent, content)

    def append(self, child=None):
        if child:
            if isinstance(child, Element):
                self.children.append(child)
                child.indent = self.children_indent
                child.parent = self
            elif isinstance(child, str) or isinstance(child, unicode):
                self.content = ''.join(
                    [self.content, self.format_content(child)])
            else:
                pass
                ''' raise TypeError('Object appended to Element must be a string'
                                'or another Element; got {} instead'
                                .format(type(child)))'''


class Html(Element):
    def __init__(self, *args, **kwargs):
        super(Html, self).__init__(*args, **kwargs)
        self.tag = 'html'


class Body(Element):
    def __init__(self, *args, **kwargs):
        super(Body, self).__init__(*args, **kwargs)
        self.tag = 'body'


class P(Element):
    def __init__(self, *args, **kwargs):
        super(P, self).__init__(*args, **kwargs)
        self.tag = 'p'
