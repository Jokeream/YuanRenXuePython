import requests
import execjs
import time  # 导入 time 模块
# 读取并编译 JavaScript 代码
with open("date.js", "r", encoding="utf-8") as f:
    js_date = f.read()

# 编译 JavaScript 代码
func_js_date = execjs.compile(js_date)

def get_page(page_num,parameters):
    url = 'http://match.yuanrenxue.com/api/match/1?page={}&m={}'.format(page_num, parameters)
    headers = {
        'Host': 'match.yuanrenxue.com',
        'Referer': 'http://match.yuanrenxue.com/match/1',
        'User-Agent': 'Mozilla/5.0(WindowsNT10.0;Win64;x64)AppleWebKit/537.36(KHTML,likeGecko)Chrome/86.0.4240.111Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',
        # 'Cookie': 'Hm_lvt_9bcbda9cbf86757998a2339a0437208e=1603724411; Hm_lpvt_9bcbda9cbf86757998a2339a0437208e=1603724411'
    }
    response = requests.get(url=url, headers=headers)
    return response.json()

if __name__ == '__main__':
    sum_num = 0
    index_num = 0
    # 循环请求第 1 到第 5 页的数据
    for i in range(1, 6):
        Byron_value = func_js_date.call("generate_m")
        res = get_page(i,Byron_value)
        data = [__['value'] for __ in res['data']]
        sum_num += sum(data)
        index_num += len(data)

        time.sleep(1)
    average = sum_num / index_num
    # 在网站输出答案不能有小数点 answer = 4700
    print('the answer is :', average)
