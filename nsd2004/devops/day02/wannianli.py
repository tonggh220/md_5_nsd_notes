# import requests
#
# url = 'http://jisuwnl.market.alicloudapi.com/calendar/query'
# headers = {'Content-Type': 'application/json; charset=UTF-8', 'Authorization': 'APPCODE xxxx'}
# params = {'date': '2020-09-23'}
# r = requests.get(url, headers=headers, params=params)
# data = r.json()
# print(data)

# import pprint
# data = {'status': 0, 'msg': 'ok', 'result': {'year': '2020', 'month': '09', 'day': '23', 'week': '三', 'lunaryear': '2020', 'lunarmonth': '八月', 'lunarday': '初七', 'ganzhi': '庚子', 'shengxiao': '鼠', 'star': '天秤座', 'huangli': {'nongli': '农历二〇二〇年八月初七', 'taishen': '占门床外正南', 'wuxing': '大林木', 'chong': '冲（癸亥）猪', 'sha': '煞东', 'jiri': '朱雀成日', 'zhiri': '朱雀（黑道日）', 'xiongshen': '小耗 天贼 土府', 'jishenyiqu': '月恩 天恩 阳德 天德合 不将 解神 司命', 'caishen': '正北', 'xishen': '东北', 'fushen': '正南', 'suici': ['庚子年', '乙酉月', '己巳日'], 'yi': ['搬家', '装修', '开业', '结婚', '领证', '开工', '动土', '出行', '订婚', '安葬', '开张', '旅游', '入学', '修造', '祭祀', '开市', '纳财', '裁衣', '嫁娶', '纳采', '移徙', '盖屋', '立券', '求医', '竖柱', '栽种', '求财', '招赘', '开仓', '纳婿', '置产'], 'ji': ['入宅', '安床', '上梁', '祈福', '纳畜', '伐木', '斋醮', '词讼', '分居', '打官司']}}}
# pprint.pprint(data)

data = {
    'msg': 'ok',
    'result': {'day': '23',
               'ganzhi': '庚子',
               'huangli': {'caishen': '正北',
                           'chong': '冲（癸亥）猪',
                           'fushen': '正南',
                           'ji': ['入宅',
                                  '安床',
                                  '上梁',
                                  '祈福',
                                  '纳畜',
                                  '伐木',
                                  '斋醮',
                                  '词讼',
                                  '分居',
                                  '打官司'],
                           'jiri': '朱雀成日',
                           'jishenyiqu': '月恩 天恩 阳德 天德合 不将 解神 司命',
                           'nongli': '农历二〇二〇年八月初七',
                           'sha': '煞东',
                           'suici': ['庚子年', '乙酉月', '己巳日'],
                           'taishen': '占门床外正南',
                           'wuxing': '大林木',
                           'xiongshen': '小耗 天贼 土府',
                           'xishen': '东北',
                           'yi': ['搬家',
                                  '装修',
                                  '开业',
                                  '结婚',
                                  '领证',
                                  '开工',
                                  '动土',
                                  '出行',
                                  '订婚',
                                  '安葬',
                                  '开张',
                                  '旅游',
                                  '入学',
                                  '修造',
                                  '祭祀',
                                  '开市',
                                  '纳财',
                                  '裁衣',
                                  '嫁娶',
                                  '纳采',
                                  '移徙',
                                  '盖屋',
                                  '立券',
                                  '求医',
                                  '竖柱',
                                  '栽种',
                                  '求财',
                                  '招赘',
                                  '开仓',
                                  '纳婿',
                                  '置产'],
                           'zhiri': '朱雀（黑道日）'},
               'lunarday': '初七',
               'lunarmonth': '八月',
               'lunaryear': '2020',
               'month': '09',
               'shengxiao': '鼠',
               'star': '天秤座',
               'week': '三',
               'year': '2020'},
    'status': 0}

# print(data['result']['huangli']['ji'])
ji = ', '.join(data['result']['huangli']['ji'])
yi = ', '.join(data['result']['huangli']['yi'])
print('忌:', ji)
print('宜:', yi)
