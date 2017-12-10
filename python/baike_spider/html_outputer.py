# coding=utf-8


'''

Created on 2017年12月4日

 

@author: Li Yongqiang

'''
from _io import open

class HtmlOutputer(object):
    def __init__(self):
        self.datas = []
    
    def collect_data(self,data):
        if data is None:
            return
        self.datas.append(data)

    
    def output_html(self):
        fout = open('output.html','w')
        
        fout.write('<html>')
        fout.write('<body>')
        fout.write('<table>')
        fout.write('</table>')
        for data in self.datas:
            fout.write('<tr>')
            fout.write('<td>%s</td>' % data['url'])
            fout.write('</tr>')
        fout.write('</body>')
        fout.write('</html>')
    
    
    
    



