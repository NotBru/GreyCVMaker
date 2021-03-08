#!/usr/bin/env python
import os

# TODO: fix href

class CV:
    class Text:
        _valid_weights = ["normal", "bold", "bolder", "lighter"]
        def __init__(self, text="", *, weight=None, href=None,
                                       fill=None):
            self._segments=[{'c': text}]
            if weight:
                self._segments[-1]['w']=weight
            if href:
                self._segments[-1]['hr']=href
            if fill:
                self._segments[-1]['f']=fill

        def __add__(left, right):
            ret = CV().Text()
            ret._segments = left._segments+right._segments
            return ret

        def __str__(self):
            ret = ""
            for segment in self._segments:
                if 'w' in segment or 'hr' in segment or 't' in segment:
                    ret += '<tspan'
                    if 'hr' in segment:
                        ret += ' href="' + segment['hr'] + '"'
                    if 'w' in segment:
                        weight = segment['w']
                        ret += ' style="font-family:Cambria;'\
                                       '-inkscape-font-specification:Cambria'
                        if weight == 'bold':
                            ret += ' Bold;font-weight:bold'
                        elif weight == 'italic':
                            ret += ' Italic;font-weight:italic'
                        ret += ';font-size:5.5mm" '
                    if 'f' in segment:
                        ret += ' fill="' + segment['f'] + '"'
                    ret += '>' + segment['c'] + '</tspan>'
                else:
                    ret += segment['c']
            return ret

    def __init__(self, width=210, height=297):
        self._width=width
        self._height=height
        self._name="Nameless"
        self._title="Titleless"
        self._id_data=[]
        self._banner_height=52.5
        self._blocks=[(0., [])]
        self._column=2
        self._endbar=False

    ### Banner factory

    def set_banner_height(self, height=52.5):
        self._banner_height=height
    
    def set_photo(self, photo_path):
        self._photo_path=photo_path

    def set_name(self, name):
        self._name=name

    def set_title(self, title):
        self._title=title

    def add_id_data(self, line):
        self._id_data.append(line)

    def _construct_banner(self):
        if '_photo_path' in self.__dict__:
            # NOTE: xlink is deprecated, but I found no working alternative
            ret = '  <image xlink:href="'+self._photo_path+'" x="0" y="0" '+\
                  'width="'+str(self._banner_height)+'mm" '+\
                  'height="'+str(self._banner_height)+'mm"/>\n'
            rect_offset = self._banner_height
        else:
            ret = ''
            rect_offset = 0
        ret += '  <rect x="'+str(rect_offset)+'mm" y="0" '+\
               'width="'+str(self._width-rect_offset)+'mm" '+\
               'height="'+str(self._banner_height)+'mm" fill="#f0f0f0"/>\n'
        ret += '  <text style="font-family:Cambria;'\
                              '-inkscape-font-specification:Cambria;'\
                              'font-size:8.5mm" '\
               'x="'+str(rect_offset+8.5)+'mm" '\
               'y="13.8mm">'+\
               self._name+'</text>\n'
        ret += '  <text style="font-family:Cambria;'\
                              '-inkscape-font-specification:Cambria;'\
                              'font-size:6.75mm" '\
               'x="'+str(rect_offset+8.5)+'mm" '\
               'y="20.55mm">'+\
               self._title+'</text>\n'
        for i, line in enumerate(self._id_data):
            ret += '  <text style="font-family:Cambria;'\
                                  '-inkscape-font-specification:Cambria;'\
                                  'font-size:5.22mm" '\
                   'x="'+str(rect_offset+8.5)+'mm" '\
                   'y="'+str(30+i*5.25)+'mm">'+\
                   line+'</text>\n'
        return ret

    ### Rest of the document factory

    def set_endbar(self, endbar=True):
        self._endbar=endbar

    def tab(self, steps=1):
        self._column += steps

    def new_block(self):
        self._blocks.append((0., []))

    def step(self, steps=1):
        y, data = self._blocks.pop()
        length, string = data.pop() 
        data.append((length+steps*1.25, string))
        self._blocks.append((y+steps*1.25, data))

    def add_sectionbar(self, name=""):
        y, data = self._blocks.pop()
        data.append((13.75, lambda y0:
              '  <rect x="0" y="'+str(y0)+'mm" '
              'width="'+str(self._width)+'mm" '
              'height="12.5mm" fill="#b5b5b5"/>\n'))
        if name:
            data.append((0, lambda y0:
              '  <text style="font-family:Cambria;'
              '-inkscape-font-specification:Cambria;'
              'font-size:8mm;font-weight:bold" '
              'x="5mm" y="'+str(y0-5)+'mm">'+name+'</text>\n'))
        self._blocks.append((y+13.75, data))

    def add_subsectionbar(self):
        y, data = self._blocks.pop()
        data.append((3.125, lambda y0:
              '  <rect x="0" y="'+str(y0)+'mm" '
              'width="'+str(self._width)+'mm" '
              'height="2.5mm" fill="#f0f0f0"/>\n'))
        self._blocks.append((y+3.125, data))

    def add_text(self, text):
        y, data = self._blocks.pop()
        data.append((6, lambda y0, column=self._column, text=text:
            '  <text x="'+str(column*5)+'mm" y="'+str(y0+6)+'mm" '
            'style="font-family:Cambria;'
            '-inkscape-font-specification:Cambria;'
            'font-size:5.5mm">'+str(text)+'</text>\n'))
        self._blocks.append((y+6, data))

    def _write_header(self, outf):
        outf.write('<svg width="'+str(self._width)+'mm" '
                        'height="'+str(self._height)+'mm"\n'
                   '  xmlns="http://www.w3.org/2000/svg">\n')
        outf.write('  <rect width="100%" height="100%" fill="white"/>\n')

    def write(self, filename="cv"):
        i = 0
        y = self._banner_height
        outf = open(filename+str(i)+'.svg', 'w')
        self._write_header(outf)
        outf.write(self._construct_banner())
        while self._blocks:
            length, data = self._blocks.pop(0)
            if y+length > self._height:
                outf.write('</svg>')
                outf.close()
                i += 1
                outf = open(filename+str(i)+'.svg', 'w')
                self._write_header(outf)
                y = 0
            for inc, obj in data:
                outf.write(obj(y))
                y += inc
        if self._endbar and y+5 < self._height:
            outf.write('  <rect x="0" y="'+str(y)+'mm" height="2.5mm" '
                       'width="'+str(self._width)+'mm" fill="black"/>\n')
        outf.write('</svg>')
        outf.close()
        filenames = [ filename+str(i) for i in range(i+1) ]
        for filename_ in filenames:
            os.system('inkscape --export-dpi=960 "'+filename_+'.svg" '
                      '-o "'+filename_+'.pdf"')
        filenamespdf= [ '"'+filename_+'.pdf"' for filename_ in filenames ]
        filenamessvg= [ '"'+filename_+'.svg"' for filename_ in filenames ]
        os.system('pdftk '+' '.join(filenamespdf)+' cat output "'+
                  filename+'.pdf"')
        os.system('rm '+' '.join(filenamessvg))
        os.system('rm '+' '.join(filenamespdf))
