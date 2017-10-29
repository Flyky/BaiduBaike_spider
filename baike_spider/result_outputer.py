#-*- coding: utf-8 -*-


class ResultOutputer(object):
    def __init__(self):
        self.datas = []
    
    def collect_data(self, data):
        if data is None:
            return
        self.datas.append(data)

    
    def output_html(self, fileName):
        with open(fileName+'.html', 'w', encoding = 'utf-8') as f:
            f.write('<html>')
            f.write("<head><meta http-equiv=\"content-type\" content=\"text/html;charset=utf-8\"></head>")
            f.write('<body>')
            f.write('<table class="table table-striped">')
            f.write('<tr><th>词条名</th><th>简介</th></tr>')
            
            for data in self.datas:
                f.write('<tr>')
                f.write('<td><button type="button" class="btn btn-link"><a href="%s">%s</a></button></td>' % (data['url'], data['title']))
                f.write('<td>%s</td>' % data['summary'])
                f.write('</tr>')
            
            f.write('</table>')
            f.write('<link rel="stylesheet" href="https://cdn.bootcss.com/bootstrap/3.3.7/css/bootstrap.min.css" integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous">')
            f.write('</body>')
            f.write('</html>')
    
    
    
    



