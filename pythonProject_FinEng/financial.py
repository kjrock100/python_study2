import datetime as dt
from urllib.request import urlopen
import bs4
import pandas as pd
import requests, json  # 해외지수는 json 형태로 표출됨
import pprint
import company_code
import numeric
from selenium import webdriver
from selenium.webdriver.common.by import By

headers = {
    'User-Agent': 'Mozilla/5.0',
    'X-Requested-With': 'XMLHttpRequest',
}

indices = {
    'SPI@SPX': 'S&P 500',
    'NAS@NDX': 'Nasdaq 100',
    'NII@NI225': 'Nikkei 225',
}


def date_format(d=''):
    if d != '':
        this_date = pd.to_datetime(d).date()
    else:
        this_date = pd.Timestamp.today().date()  # 오늘 날짜를 지정
    return (this_date)


def historical_index_naver(d, index_cd, start_date='', end_date='', page_n=1, last_page=0):
    if start_date:  # start_date가 있으면
        start_date = date_format(start_date)  # date 포맷으로 변환
    else:  # 없으면
        start_date = dt.date.today()  # 오늘 날짜를 지정
    if end_date:
        end_date = date_format(end_date)
    else:
        end_date = dt.date.today()

    naver_index = 'http://finance.naver.com/sise/sise_index_day.nhn?code=' + index_cd + '&page=' + str(page_n)

    source = urlopen(naver_index).read()  # 지정한 페이지에서 코드 읽기
    source = bs4.BeautifulSoup(source, 'lxml')  # 뷰티풀 스프로 태그별로 코드 분류

    dates = source.find_all('td', class_='date')  # <td class="date">태그에서 날짜 수집
    prices = source.find_all('td', class_='number_1')  # <td class="number_1">태그에서 지수 수집

    for n in range(len(dates)):
        if dates[n].text.split('.')[0].isdigit():
            # 날짜 처리
            this_date = dates[n].text
            this_date = date_format(this_date)

            if this_date <= end_date and this_date >= start_date:
                # start_date와 end_date 사이에서 데이터 저장
                # 종가 처리
                this_close = prices[n * 4].text  # prices 중 종가지수인 0,4,8,...번째 데이터 추출
                this_close = this_close.replace(',', '')
                this_close = float(this_close)

                # 딕셔너리에 저장
                d[this_date] = this_close

            elif this_date < start_date:
                # start_date 이전이면 함수 종료
                return d

                # 페이지 네비게이션
    if last_page == 0:
        last_page = source.find('td', class_='pgRR').find('a')['href']
        # 마지막페이지 주소 추출
        last_page = last_page.split('&')[1]  # & 뒤의 page=506 부분 추출
        last_page = last_page.split('=')[1]  # = 뒤의 페이지번호만 추출
        last_page = int(last_page)  # 숫자형 변수로 변환

    # 다음 페이지 호출
    if page_n < last_page:
        page_n = page_n + 1
        historical_index_naver(d, index_cd, start_date, end_date, page_n, last_page)

    return d


def test1():
    index_cd = 'KPI200'
    historical_prices = dict()
    historical_prices = historical_index_naver(historical_prices, index_cd, '2021-4-1', '2021-4-1')
    print(historical_prices)


def read_json(d, symbol, page=1):
    url = 'https://finance.naver.com/world/worldDayListJson.nhn?symbol=' + symbol + '&fdtc=0&page=' + str(page)
    r = requests.post(url, headers=headers)
    data = json.loads(r.text)

    for n in range(len(data)):
        date = pd.to_datetime(data[n]['xymd']).date()
        price = float(data[n]['clos'])
        d[date] = price

    if len(data) >= 9 and page < 3:
        page += 1
        read_json(d, symbol, page)

    return d


def index_global(d, symbol, start_date='', end_date='', page=1):
    end_date = date_format(end_date)
    if start_date == '':
        start_date = end_date - pd.DateOffset(months=1)
    start_date = date_format(start_date)

    url = 'https://finance.naver.com/world/worldDayListJson.nhn?symbol=' + symbol + '&fdtc=0&page=' + str(page)
    r = requests.post(url, headers=headers)
    data = json.loads(r.text)

    if len(data) > 0:
        for n in range(len(data)):
            date = pd.to_datetime(data[n]['xymd']).date()

            if date <= end_date and date >= start_date:
                # start_date와 end_date 사이에서 데이터 저장
                # 종가 처리
                price = float(data[n]['clos'])
                # 딕셔너리에 저장
                d[date] = price
            elif date < start_date:
                # start_date 이전이면 함수 종료
                return d

        if len(data) >= 9:
            page += 1
            index_global(d, symbol, start_date, end_date, page)

    return d


def test2():
    historical_indices = dict()
    start_date = '2021-3-31'
    end_date = '2021-3-31'
    for key, value in indices.items():
        s = dict()
        s = index_global(s, key, start_date, end_date)
        historical_indices[value] = s
    prices_df = pd.DataFrame(historical_indices)
    print(prices_df)


def get_estimated_performance(ret, index_cd, frq=0):
    naver_index = 'https://navercomp.wisereport.co.kr/v2/company/cF1002.aspx?cmp_cd=' + index_cd \
                  + '&finGubun=MAIN&frq=' + str(frq)
    source = urlopen(naver_index).read()
    source = bs4.BeautifulSoup(source, 'lxml')
    # print(source)
    data = source.find_all('td')
    # pprint.pprint(data)
    result = []
    for n in range(len(data)):
        if data[n].find('sp'):
            result.append(data[n].find('sp').text)
        else:
            result.append(data[n].text)

    performance = dict()
    for n in range(len(data) // 12):
        d = dict()
        d['재무년월'] = result[n * 12]
        d['매출액(금액)'] = result[n * 12 + 1]
        d['매출액(YoY)'] = result[n * 12 + 2]
        d['영업이익'] = result[n * 12 + 3]
        d['당기순이익'] = result[n * 12 + 4]
        d['EPS'] = result[n * 12 + 5]
        d['PER'] = result[n * 12 + 6]
        d['PBR'] = result[n * 12 + 7]
        d['ROE'] = result[n * 12 + 8]
        d['EV/EBITDA'] = result[n * 12 + 9]
        d['순부채비율'] = result[n * 12 + 10]
        d['주재무제표'] = result[n * 12 + 11]
        performance[result[n * 12]] = d

    if frq == 0:
        ret["추정실적_annual"] = performance
    else:
        ret["추정실적_quarter"] = performance


def test3():
    for company, code in company_code.codes.items():
        s = dict()
        get_estimated_performance(s, code, 0)
        get_estimated_performance(s, code, 1)
        print(company, s)


def get_summary_naver(ret, index_cd, frq='Y'):
    # frq = Y or Q
    naver_index = 'https://navercomp.wisereport.co.kr/v2/company/ajax/cF1001.aspx?cmp_cd=' + index_cd \
                  + '&fin_typ=0&freq_typ=' + frq + '&encparam=K2dqNE5rNDltTXVLVWFvazl0VzRsZz09&id=RVArcVR1a2'
    print(naver_index)
    heads = []
    source = urlopen(naver_index).read()
    source = bs4.BeautifulSoup(source, 'lxml')
    tables = source.find_all('table')
    print(tables)
    ths = tables[1].find_all('th')
    for i in range(len(ths)):
        for t in ths[i].strings:
            heads.append(t.strip())
            break

    # for i in range(len(heads)):
    #     print(i, heads[i])

    tds = tables[1].find_all('td')
    data = []
    for i in range(len(tds)):
        if tds[i].find('span'):
            data.append(tds[i].find('span').text)
        else:
            data.append(tds[i].text)

    # for i in range(len(data)):
    #     print(i, data[i])

    if (len(heads) - 10) * 8 != len(data):
        print('error, not equal')
        return

    summary1 = dict()
    for i in range(len(heads) - 10):
        s = dict()
        s[heads[2]] = data[i * 8]
        s[heads[3]] = data[i * 8 + 1]
        s[heads[4]] = data[i * 8 + 2]
        s[heads[5]] = data[i * 8 + 3]
        s[heads[6]] = data[i * 8 + 4]
        s[heads[7]] = data[i * 8 + 5]
        s[heads[8]] = data[i * 8 + 6]
        s[heads[9]] = data[i * 8 + 7]
        summary1[heads[i + 10]] = s

    # print(summary1)

    if frq == 'Y':
        ret["실적_annual"] = summary1
    else:
        ret["실적_quarter"] = summary1


def get_summary_daum(ret, index_cd):
    # frq = Y or Q
    daum_index = 'https://wisefn.finance.daum.net/v1/company/cF1001.aspx?cmp_cd=' + index_cd + '&frq=0&rpt=1&finGubun=MAIN'
    print(daum_index)

    source = urlopen(daum_index).read()
    source = bs4.BeautifulSoup(source, 'lxml')
    print(source)
    tr_row1 = source.find('tr', class_='row1')
    print(tr_row1)


def get_summary_fnguide(ret, index_cd):
    fnguide_index = 'https://comp.fnguide.com/SVO2/asp/SVD_Main.asp?pGB=1&gicode=A' \
                    + index_cd + '&cID=&MenuYn=Y&ReportGB=&NewMenuID=101&stkGb=701'
    # print(fnguide_index)

    source = urlopen(fnguide_index).read()
    source = bs4.BeautifulSoup(source, 'lxml')
    # print(source)

    # 날짜
    date_ = source.find(attrs={'id': 'div1'}).find(attrs={'class': 'date'}).text
    # print(date_)
    ret['날짜'] = date_.replace('[', '').replace(']', '')

    # 시세
    tds = source.find(attrs={'id': 'div1'}).find('tbody').find_all('td')
    # for n in range(len(tds)):
    #     print(n, ''.join(tds[n].text.split()))
    data = dict()
    data['종가/전일대비'] = ''.join(tds[0].text.split())
    data['거래량'] = ''.join(tds[1].text.split())
    data['52주.최고가/최저가'] = ''.join(tds[2].text.split())
    data['거래대금'] = ''.join(tds[3].text.split())
    data['수익률'] = ''.join(tds[4].text.split())
    data['외국인보유비중'] = ''.join(tds[5].text.split())
    data['시가총액(상장예정포함)'] = ''.join(tds[6].text.split())
    data['베타'] = ''.join(tds[7].text.split())
    data['시가총액(보통주)'] = ''.join(tds[8].text.split())
    data['액면가'] = ''.join(tds[9].text.split())
    data['발행주식수'] = ''.join(tds[10].text.split())
    data['유동주식수/비율'] = ''.join(tds[11].text.split())
    ret['시세'] = data

    # 투자의견
    data = dict()
    tds = source.find(attrs={'id': 'div6'}).find('tbody').find_all('td')
    if len(tds) == 5:
        data['투자의견'] = tds[0].text
        data['목표주가'] = tds[1].text
        data['EPS'] = tds[2].text
        data['PER'] = tds[3].text
        data['추정기관수'] = tds[4].text
    ret['투자의견'] = data

    # 실적
    heads = []
    ths = source.find(attrs={'id': 'div15'}).find('thead').find_all('th')
    for n in range(len(ths)):
        if ths[n].find('span'):
            heads.append(ths[n].find('span').text)
        else:
            heads.append(ths[n].text)
    # print(heads)

    ths = source.find(attrs={'id': 'div15'}).find('tbody').find_all('th')
    for n in range(len(ths)):
        if ths[n].find('a'):
            ths[n] = ths[n].find('a').text.strip()
        else:
            ths[n] = ths[n].text.strip()
    # print(ths)

    tds = source.find(attrs={'id': 'div15'}).find('tbody').find_all('td')
    if len(ths) * 8 == len(tds):
        data = dict()
        for n in range(len(ths)):
            d = dict()
            d[heads[7]] = tds[n * 8].text.strip()
            d[heads[8]] = tds[n * 8 + 1].text.strip()
            d[heads[9]] = tds[n * 8 + 2].text.strip()
            d[heads[10]] = tds[n * 8 + 3].text.strip()
            data[ths[n]] = d
        ret['실적_annual'] = data
        data = dict()
        for n in range(len(ths)):
            d = dict()
            d[heads[7]] = tds[n * 8 + 4].text.strip()
            d[heads[8]] = tds[n * 8 + 5].text.strip()
            d[heads[9]] = tds[n * 8 + 6].text.strip()
            d[heads[10]] = tds[n * 8 + 7].text.strip()
            data[ths[n]] = d
        ret['실적_quarter'] = data


def get_sise_fnguide(ret, index_cd):
    fnguide_index = 'https://comp.fnguide.com/SVO2/asp/SVD_Main.asp?pGB=1&gicode=A' \
                    + index_cd + '&cID=&MenuYn=Y&ReportGB=&NewMenuID=101&stkGb=701'
    # print(fnguide_index)

    source = urlopen(fnguide_index).read()
    source = bs4.BeautifulSoup(source, 'lxml')
    # print(source)

    # 시세
    tds = source.find(attrs={'id': 'div1'}).find('tbody').find_all('td')

    data = dict()
    data['종가/전일대비'] = ''.join(tds[0].text.split())
    data['거래량'] = ''.join(tds[1].text.split())
    data['52주.최고가/최저가'] = ''.join(tds[2].text.split())
    data['거래대금'] = ''.join(tds[3].text.split())
    data['수익률'] = ''.join(tds[4].text.split())
    data['외국인보유비중'] = ''.join(tds[5].text.split())
    data['시가총액(상장예정포함)'] = ''.join(tds[6].text.split())
    data['베타'] = ''.join(tds[7].text.split())
    data['시가총액(보통주)'] = ''.join(tds[8].text.split())
    data['액면가'] = ''.join(tds[9].text.split())
    data['발행주식수'] = ''.join(tds[10].text.split())
    data['유동주식수/비율'] = ''.join(tds[11].text.split())
    ret['시세'] = data


def get_investment_opinion_fnguide(ret, index_cd):
    fnguide_index = 'https://comp.fnguide.com/SVO2/asp/SVD_Main.asp?pGB=1&gicode=A' \
                    + index_cd + '&cID=&MenuYn=Y&ReportGB=&NewMenuID=101&stkGb=701'
    # print(fnguide_index)

    source = urlopen(fnguide_index).read()
    source = bs4.BeautifulSoup(source, 'lxml')
    # print(source)

    # 투자의견
    data = dict()
    tds = source.find(attrs={'id': 'div6'}).find('tbody').find_all('td')
    if len(tds) == 5:
        data['투자의견'] = tds[0].text
        data['목표주가'] = tds[1].text
        data['EPS'] = tds[2].text
        data['PER'] = tds[3].text
        data['추정기관수'] = tds[4].text
    ret['투자의견'] = data


def get_performance_fnguide(ret, index_cd):
    fnguide_index = 'https://comp.fnguide.com/SVO2/asp/SVD_Main.asp?pGB=1&gicode=A' \
                    + index_cd + '&cID=&MenuYn=Y&ReportGB=&NewMenuID=101&stkGb=701'
    # print(fnguide_index)

    source = urlopen(fnguide_index).read()
    source = bs4.BeautifulSoup(source, 'lxml')
    # print(source)

    # 실적
    heads = []
    ths = source.find(attrs={'id': 'div15'}).find('thead').find_all('th')
    for n in range(len(ths)):
        if ths[n].find('span'):
            heads.append(ths[n].find('span').text)
        else:
            heads.append(ths[n].text)
    # print(heads)

    ths = source.find(attrs={'id': 'div15'}).find('tbody').find_all('th')
    for n in range(len(ths)):
        if ths[n].find('a'):
            ths[n] = ths[n].find('a').text.strip()
        else:
            ths[n] = ths[n].text.strip()
    # print(ths)

    tds = source.find(attrs={'id': 'div15'}).find('tbody').find_all('td')
    if len(ths) * 8 == len(tds):
        data = dict()
        for n in range(len(ths)):
            d = dict()
            d[heads[7]] = tds[n * 8].text.strip()
            d[heads[8]] = tds[n * 8 + 1].text.strip()
            d[heads[9]] = tds[n * 8 + 2].text.strip()
            d[heads[10]] = tds[n * 8 + 3].text.strip()
            data[ths[n]] = d
        ret['실적_annual'] = data
        data = dict()
        for n in range(len(ths)):
            d = dict()
            d[heads[7]] = tds[n * 8 + 4].text.strip()
            d[heads[8]] = tds[n * 8 + 5].text.strip()
            d[heads[9]] = tds[n * 8 + 6].text.strip()
            d[heads[10]] = tds[n * 8 + 7].text.strip()
            data[ths[n]] = d
        ret['실적_quarter'] = data


def test4():
    for company, code in company_code.codes.items():
        s = dict()
        get_performance_fnguide(s, code)
        print(company, s)


def get_investment_opinion_naver(ret, index_cd):
    naver_index = 'https://navercomp.wisereport.co.kr/v2/company/c1010001.aspx?cmp_cd=' + index_cd + '&cn='
    # print(naver_index)
    s = dict()
    s['투자의견'] = 0
    s['목표주가'] = 0

    try:
        source = urlopen(naver_index).read()
        source = bs4.BeautifulSoup(source, 'lxml')
        # print(source)
        table = source.find('table', id='cTB15')
        # print(table)
        ths = table.find_all('tr')
        tds = ths[1].find_all('td')

        if len(tds) == 5:
            opinion = tds[0].text
            if numeric.is_valid_float(opinion):
                s['투자의견'] = float(opinion)

            target = tds[1].text.replace(',', '')
            if numeric.is_valid_int(target):
                s['목표주가'] = int(target)

        ret['투자의견'] = s
    except AttributeError:
        print('get_investment_opinion_naver, AttributeError, code:', index_cd)
        ret['투자의견'] = s


def test5():
    for company, code in company_code.codes.items():
        s = dict()
        get_investment_opinion_naver(s, code)
        print(company, s)


def get_sise_naver(ret, index_cd):
    naver_index = 'https://navercomp.wisereport.co.kr/v2/company/c1010001.aspx?cmp_cd=' + index_cd
    # print(naver_index)
    sise = dict()
    sise['주가'] = 0
    try:
        source = urlopen(naver_index).read()
        source = bs4.BeautifulSoup(source, 'lxml')
        # print(source)
        trs = source.find('table', id='cTB11').find_all('tr')

        for tr in trs:
            th = tr.find('th')
            subject = th.text
            td = tr.find('td')
            data = ''.join(td.text.split())

            sise[subject] = data
        # print(sise)
        ret['시세'] = sise
    except AttributeError:
        print('get_sise_naver, AttributeError, code:', index_cd)
        ret['시세'] = sise


def get_sise_naver_api(ret, index_cd):
    get_sise_naver(ret, index_cd)
    try:
        values = ret['시세']['주가/전일대비/수익률'].split('/')
        ret['시세']['주가'] = values[0][:-1].replace(',', '')
        ret['시세']['전일대비'] = values[1][:-1]
        ret['시세']['수익률'] = values[2][:-1]
        ret['시세'].pop('주가/전일대비/수익률')

        if (numeric.is_valid_int(ret['시세']['주가'])):
            ret['시세']['주가'] = int(ret['시세']['주가'])
        else:
            ret['시세']['주가'] = int(0)
    except KeyError:
        print('get_sise_naver_api, KeyError, code:', index_cd)


def test6():
    s = dict()
    get_sise_naver_api(s, company_code.codes['삼성전자'])
    print('삼성전자', s)


def get_day_sise_naver(code, page_count=0):
    # https://finance.naver.com/item/sise_day.naver?code=066570&page=1
    naver_index_base = 'https://finance.naver.com/item/sise_day.naver'
    last_page = 0
    # print(naver_index_base)
    browser = webdriver.Chrome()
    browser.get(naver_index_base + '?code=' + code)

    td = browser.find_element(By.CLASS_NAME, 'pgRR')
    # print(td)
    td.click()
    # print(browser.current_url)
    param = browser.current_url.split('?')[1]
    param2 = param.split('&')
    for p in param2:
        p2 = p.split('=')
        if p2[0] == 'page':
            last_page = int(p2[1])

    print('last_page : {}'.format(last_page))

    sise = dict()
    try:
        for i in range(1, last_page + 1):
            if page_count != 0 and i > page_count:
                break
            naver_index = naver_index_base + '?code=' + code + '&page=' + str(i)
            print('naver_index : ' + naver_index)
            # source = urlopen(naver_index).read()
            browser.get(naver_index)
            source = bs4.BeautifulSoup(browser.page_source, 'lxml')
            trs = source.find('table').find_all('tr')

            for tr in trs:

                tds = tr.find_all('td')
                if len(tds) < 7:
                    continue

                date = ''
                value = 0
                for i2, td in enumerate(tds):
                    if i2 == 0:
                        date = td.find('span').text
                        date = date.replace('.', '/')
                    if i2 == 1:
                        value = int(td.find('span').text.replace(',', ''))
                    if i2 > 1:
                        break
                sise[date] = value

        return sise
    except AttributeError:
        print('get_day_sise_naver, AttributeError, code:', code)
        return sise

def test_day_sise_naver():
    day_sise = get_day_sise_naver('035720')

    f = open("day_sise.txt", 'w')
    for k, v in day_sise.items():
        f.write('{} {}\n'.format(k, v))
    f.close()

test_day_sise_naver()