import requests
 
class Settings:
    
    def __init__(self, page):
        self.page = page
        
        self.url = 'http://54.push2.eastmoney.com/api/qt/clist/get'
        
        self.cookies = {
            'qgqp_b_id': '02d480cce140d4a420a0df6b307a945c',
            'cowCookie': 'true',
            'em_hq_fls': 'js',
            'intellpositionL': '1168.61px',
            'HAList': 'a-sz-300059-%u4E1C%u65B9%u8D22%u5BCC%2Ca-sz-000001-%u5E73%u5B89%u94F6%u884C',
            'st_si': '07441051579204',
            'st_asi': 'delete',
            'st_pvi': '34234318767565',
            'st_sp': '2021-09-28%2010%3A43%3A13',
            'st_inirUrl': 'http%3A%2F%2Fdata.eastmoney.com%2F',
            'st_sn': '31',
            'st_psi': '20211020210419860-113300300813-5631892871',
            'intellpositionT': '1007.88px',
        }  
        
        self.headers = {
            'Connection': 'keep-alive',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36 Edg/94.0.992.50',
            'DNT': '1',
            'Accept': '*/*',
            'Referer': 'http://quote.eastmoney.com/',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        }
        
        self.params = (
            ('cb', 'jQuery112404825022376475756_1634735261901'),
            ('pn', str(self.page)),
            ('pz', '20'),
            ('po', '1'),
            ('np', '1'),
            ('ut', 'bd1d9ddb04089700cf9c27f6f7426281'),
            ('fltt', '2'),
            ('invt', '2'),
            ('fid', 'f3'),
            ('fs', 'm:0 t:6,m:0 t:80,m:1 t:2,m:1 t:23'),
            ('fields', 'f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f12,f13,f14,f15,f16,f17,f18,f20,f21,f23,f24,f25,f22,f11,f62,f128,f136,f115,f152'),
            ('_', '1634735261902'),
        )

#NB. Original query string below. It seems impossible to parse and
#reproduce query strings 100% accurately so the one below is given
#in case the reproduced version is not "correct".
# response = requests.get('http://54.push2.eastmoney.com/api/qt/clist/get?cb=jQuery112404825022376475756_1634735261901&pn=1&pz=20&po=1&np=1&ut=bd1d9ddb04089700cf9c27f6f7426281&fltt=2&invt=2&fid=f3&fs=m:0+t:6,m:0+t:80,m:1+t:2,m:1+t:23&fields=f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f12,f13,f14,f15,f16,f17,f18,f20,f21,f23,f24,f25,f22,f11,f62,f128,f136,f115,f152&_=1634735261902', headers=headers, cookies=cookies, verify=False)