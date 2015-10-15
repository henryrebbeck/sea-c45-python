#!/usr/bin/env python

"""
Python class example.

"""

# The start of it all:
# Fill it all in here.


#  class Element(object):
class Element(object):
    "doc string :Create Element class to produce HTML"

    tag = ''
    indent = '   '

    def __init__(self, content=None, **attributes):
        if content is not None:
            self.content = [str(content)]
        else:
            self.content = []
        self.attributes = attributes
        print('attributes in __init__:', attributes)

    def append(self, new_content):

        """ Add some new content to the element
        """
        self.content.append(new_content)

    def render(self, file_new, ind=""):
        """Render the content to the given file like object"""
        # Start a new line and print out the tag
        file_new.write("\n")
        file_new.write(ind)
        file_new.write("<%s>" % self.tag)

        '''
        print(r"\n,ind,self.tag from inside render :","\n",ind,self.tag)
        print('self.attributes.itesm', self.attributes.items())
        for key, value in self.attributes.items():
            print('2..key and value in self.attributes.itesm',key,value,self.attributes.items())
            file_new.write(' %s="%s"' % (key, value))
        file_new.write(">")'''

        print('Loop through self.content :', self.content, '\n')
        for s in self.content:  # loop through the content of the class
            # We have defined the content as either a string
            # or an empty list(element??).
            print("s in self.content: s is---->", s)
            if isinstance(s, Element):  # this line is key
                # this says if the item s is of class Element then
                # send it back to the renderer otherwise its a string
                # so print/render it
                print('if isinstance (s,Element)  s:', s, 'Element', Element)
                # this is the recursive render call where we send the element
                # to the renderer again, but making the indent have an
                # additional indent of itself.
                s.render(file_new, ind + self.indent)
            else:
                file_new.write("\n" + ind + self.indent + str(s))
        file_new.write("\n" + ind + "</" + self.tag + ">")

        #  def render(self, f):
        #  f.write(self.render_html())

    def render_html(self):
        return u'\n{i}<{t}>{c}{ch}\n{i}</>'.format(
            i=' ' * self.indent,
            t=self.tag,
            c=self.content,
            ch=''.join([child.render_html() for child in self]))


class Html(Element):
    "Create a subclass element to produce a html tagged element (page)"
    tag = 'Html'
    indent = '    '
    # This indentation is for the next line of text
    # (ie the body tag if thats called next)
    print('Html', indent, tag)


class Body(Element):
    "Create a class element to produce a body element"
    " (which contains the page element (which contains the paragraph element))"
    tag = 'body'
    indent = '    '
    print('Body', indent, tag)


class P(Element):
    "docstring: Create a subclass element to produce a paragraph element"
    tag = 'p'
    indent = '    '
    print('p', indent, tag)
