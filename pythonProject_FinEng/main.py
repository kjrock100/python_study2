import company_code
import financial


def test_1m_수익율():
    data = dict()
    target = 0  # (1m, 3m, 6m, 12m)
    for company, code in company_code.codes.items():
        d = dict()
        financial.get_sise_fnguide(d, code)
        data[company] = d
        dd = d['시세']['수익률'].split('/')
        for n in range(len(dd)):
            if dd[n] == '-':
                dd[n] = 0
            else:
                dd[n] = float(dd[n])
        # print(dd)
        data[company] = dd

    res = sorted(data.items(), key=lambda item: item[1][target], reverse=True)
    for n in range(len(res)):
        print(n, res[n][0], res[n][1][target])


def kospi_1m_수익율():
    data = dict()
    target = 0  # (1m, 3m, 6m, 12m)
    total = len(company_code.codes_kospi)
    count = 0
    for company, code in company_code.codes_kospi.items():
        d = dict()
        financial.get_sise_fnguide(d, code)
        data[company] = d
        dd = d['시세']['수익률'].split('/')
        for n in range(len(dd)):
            if dd[n] == '-':
                dd[n] = 0
            else:
                dd[n] = float(dd[n].replace(',', ''))
        # print(dd)
        data[company] = dd

        count += 1
        if count % 10 == 0:
            print('{} / {}'.format(count, total))

    res = sorted(data.items(), key=lambda item: item[1][target], reverse=True)
    for n in range(len(res)):
        print(n, res[n][0], res[n][1][target])


def kosdaq_1m_수익율():
    data = dict()
    target = 0  # (1m, 3m, 6m, 12m)
    total = len(company_code.codes_kosdaq)
    count = 0
    for company, code in company_code.codes_kosdaq.items():
        d = dict()
        financial.get_sise_fnguide(d, code)
        data[company] = d
        dd = d['시세']['수익률'].split('/')
        for n in range(len(dd)):
            if dd[n] == '-':
                dd[n] = 0
            else:
                dd[n] = float(dd[n].replace(',', ''))
        # print(dd)
        data[company] = dd

        count += 1
        if count % 10 == 0:
            print('{} / {}'.format(count, total))

    res = sorted(data.items(), key=lambda item: item[1][target], reverse=True)
    for n in range(len(res)):
        print(n, res[n][0], res[n][1][target])


def test_3q_실적():
    data = dict()
    for company, code in company_code.codes.items():
        d = dict()
        d['순위'] = dict()
        financial.get_estimated_performance(d, code, 1)
        dd = d['추정실적_quarter']['2021.09(A)']

        dd['매출액(금액)'] = dd['매출액(금액)'].replace(',', '').replace('N/A', '0')
        if dd['매출액(금액)']:
            dd['매출액(금액)'] = float(dd['매출액(금액)'])
        else:
            dd['매출액(금액)'] = 0

        dd['매출액(YoY)'] = dd['매출액(YoY)'].replace(',', '').replace('N/A', '0')
        if dd['매출액(YoY)']:
            dd['매출액(YoY)'] = float(dd['매출액(YoY)'])
        else:
            dd['매출액(YoY)'] = 0

        dd['영업이익'] = dd['영업이익'].replace(',', '').replace('N/A', '0')
        if dd['영업이익']:
            dd['영업이익'] = float(dd['영업이익'])
        else:
            dd['영업이익'] = 0

        dd['당기순이익'] = dd['당기순이익'].replace(',', '').replace('N/A', '0')
        if dd['당기순이익']:
            dd['당기순이익'] = float(dd['당기순이익'])
        else:
            dd['당기순이익'] = 0

        dd['EPS'] = dd['EPS'].replace(',', '').replace('N/A', '0')
        if dd['EPS']:
            dd['EPS'] = float(dd['EPS'])
        else:
            dd['EPS'] = 0

        dd['PER'] = dd['PER'].replace(',', '').replace('N/A', '-1000')
        if dd['PER']:
            dd['PER'] = float(dd['PER'])
        else:
            dd['PER'] = -1000

        dd['PBR'] = dd['PBR'].replace(',', '').replace('N/A', '-1000')
        if dd['PBR']:
            dd['PBR'] = float(dd['PBR'])
        else:
            dd['PBR'] = -1000

        dd['ROE'] = dd['ROE'].replace(',', '').replace('N/A', '-1000')
        if dd['ROE']:
            dd['ROE'] = float(dd['ROE'])
        else:
            dd['ROE'] = -1000

        dd['EV/EBITDA'] = dd['EV/EBITDA'].replace(',', '').replace('N/A', '-1000')
        if dd['EV/EBITDA']:
            dd['EV/EBITDA'] = float(dd['EV/EBITDA'])
        else:
            dd['EV/EBITDA'] = -1000

        dd['순부채비율'] = dd['순부채비율'].replace(',', '').replace('N/A', '100')
        if dd['순부채비율']:
            dd['순부채비율'] = float(dd['순부채비율'])
        else:
            dd['순부채비율'] = 100

        data[company] = d

    res = sorted(data.items(), key=lambda item: 1 / (0.000000001 + item[1]['추정실적_quarter']['2021.09(A)']['PER']),
                 reverse=True)
    for n in range(len(res)):
        data[res[n][0]]['순위']['PER'] = n
        if n != 0:
            prev = data[res[n - 1][0]]['추정실적_quarter']['2021.09(A)']['PER']
            cur = data[res[n][0]]['추정실적_quarter']['2021.09(A)']['PER']
            if prev == cur:
                data[res[n][0]]['순위']['PER'] = data[res[n - 1][0]]['순위']['PER']

        # print(n, res[n][0], res[n][1]['추정실적_quarter']['2021.09(A)']['PER'])

    res = sorted(data.items(), key=lambda item: 1 / (0.000000001 + item[1]['추정실적_quarter']['2021.09(A)']['PBR']),
                 reverse=True)
    for n in range(len(res)):
        data[res[n][0]]['순위']['PBR'] = n
        if n != 0:
            prev = data[res[n - 1][0]]['추정실적_quarter']['2021.09(A)']['PBR']
            cur = data[res[n][0]]['추정실적_quarter']['2021.09(A)']['PBR']
            if prev == cur:
                data[res[n][0]]['순위']['PBR'] = data[res[n - 1][0]]['순위']['PBR']
        # print(n, res[n][0], res[n][1]['추정실적_quarter']['2021.09(A)']['PBR'])

    res = sorted(data.items(), key=lambda item: item[1]['추정실적_quarter']['2021.09(A)']['EPS'], reverse=True)
    for n in range(len(res)):
        data[res[n][0]]['순위']['EPS'] = n
        if n != 0:
            prev = data[res[n - 1][0]]['추정실적_quarter']['2021.09(A)']['EPS']
            cur = data[res[n][0]]['추정실적_quarter']['2021.09(A)']['EPS']
            if prev == cur:
                data[res[n][0]]['순위']['EPS'] = data[res[n - 1][0]]['순위']['EPS']
        # print(n, res[n][0], res[n][1]['추정실적_quarter']['2021.09(A)']['EPS'])

    res = sorted(data.items(), key=lambda item: item[1]['추정실적_quarter']['2021.09(A)']['ROE'], reverse=True)
    for n in range(len(res)):
        data[res[n][0]]['순위']['ROE'] = n
        if n != 0:
            prev = data[res[n - 1][0]]['추정실적_quarter']['2021.09(A)']['ROE']
            cur = data[res[n][0]]['추정실적_quarter']['2021.09(A)']['ROE']
            if prev == cur:
                data[res[n][0]]['순위']['ROE'] = data[res[n - 1][0]]['순위']['ROE']
        # print(n, res[n][0], res[n][1]['추정실적_quarter']['2021.09(A)']['ROE'])

    res = sorted(data.items(), key=lambda item: 1 / (0.000000001 + item[1]['추정실적_quarter']['2021.09(A)']['EV/EBITDA']),
                 reverse=True)
    for n in range(len(res)):
        data[res[n][0]]['순위']['EV/EBITDA'] = n
        if n != 0:
            prev = data[res[n - 1][0]]['추정실적_quarter']['2021.09(A)']['EV/EBITDA']
            cur = data[res[n][0]]['추정실적_quarter']['2021.09(A)']['EV/EBITDA']
            if prev == cur:
                data[res[n][0]]['순위']['EV/EBITDA'] = data[res[n - 1][0]]['순위']['EV/EBITDA']
        # print(n, res[n][0], res[n][1]['추정실적_quarter']['2021.09(A)']['EV/EBITDA'])

    for name, ddd in data.items():
        data[name]['순위']['종합순위'] = 0
        for item, grade in ddd['순위'].items():
            data[name]['순위']['종합순위'] += grade

    res = sorted(data.items(), key=lambda item: item[1]['순위']['종합순위'])
    for n in range(len(res)):
        print(n, res[n][0], res[n][1]['순위'])



def kospi_3q_실적():
    data = dict()
    total = len(company_code.codes_kospi)
    count = 0
    quartar = '2021.09(A)'
    for company, code in company_code.codes_kospi.items():
        d = dict()
        d['순위'] = dict()
        financial.get_estimated_performance(d, code, 1)
        if d['추정실적_quarter'].get(quartar):
            dd = d['추정실적_quarter'][quartar]
        else:
            continue

        dd['매출액(금액)'] = dd['매출액(금액)'].replace(',', '').replace('N/A', '0')
        if dd['매출액(금액)']:
            dd['매출액(금액)'] = float(dd['매출액(금액)'])
        else:
            dd['매출액(금액)'] = 0

        dd['매출액(YoY)'] = dd['매출액(YoY)'].replace(',', '').replace('N/A', '0')
        if dd['매출액(YoY)']:
            dd['매출액(YoY)'] = float(dd['매출액(YoY)'])
        else:
            dd['매출액(YoY)'] = 0

        dd['영업이익'] = dd['영업이익'].replace(',', '').replace('N/A', '0')
        if dd['영업이익']:
            dd['영업이익'] = float(dd['영업이익'])
        else:
            dd['영업이익'] = 0

        dd['당기순이익'] = dd['당기순이익'].replace(',', '').replace('N/A', '0')
        if dd['당기순이익']:
            dd['당기순이익'] = float(dd['당기순이익'])
        else:
            dd['당기순이익'] = 0

        dd['EPS'] = dd['EPS'].replace(',', '').replace('N/A', '0')
        if dd['EPS']:
            dd['EPS'] = float(dd['EPS'])
        else:
            dd['EPS'] = 0

        dd['PER'] = dd['PER'].replace(',', '').replace('N/A', '-1000')
        if dd['PER']:
            dd['PER'] = float(dd['PER'])
        else:
            dd['PER'] = -1000

        dd['PBR'] = dd['PBR'].replace(',', '').replace('N/A', '-1000')
        if dd['PBR']:
            dd['PBR'] = float(dd['PBR'])
        else:
            dd['PBR'] = -1000

        dd['ROE'] = dd['ROE'].replace(',', '').replace('N/A', '-1000')
        if dd['ROE']:
            dd['ROE'] = float(dd['ROE'])
        else:
            dd['ROE'] = -1000

        dd['EV/EBITDA'] = dd['EV/EBITDA'].replace(',', '').replace('N/A', '-1000')
        if dd['EV/EBITDA']:
            dd['EV/EBITDA'] = float(dd['EV/EBITDA'])
        else:
            dd['EV/EBITDA'] = -1000

        dd['순부채비율'] = dd['순부채비율'].replace(',', '').replace('N/A', '100')
        if dd['순부채비율']:
            dd['순부채비율'] = float(dd['순부채비율'])
        else:
            dd['순부채비율'] = 100

        data[company] = d
        count += 1
        if count % 10 == 0:
            print('{} / {}'.format(count, total))

    res = sorted(data.items(), key=lambda item: 1 / (0.000000001 + item[1]['추정실적_quarter'][quartar]['PER']),
                 reverse=True)
    for n in range(len(res)):
        data[res[n][0]]['순위']['PER'] = n
        if n != 0:
            prev = data[res[n - 1][0]]['추정실적_quarter'][quartar]['PER']
            cur = data[res[n][0]]['추정실적_quarter'][quartar]['PER']
            if prev == cur:
                data[res[n][0]]['순위']['PER'] = data[res[n - 1][0]]['순위']['PER']
        # print(n, res[n][0], res[n][1]['추정실적_quarter']['2021.09(A)']['PER'])

    res = sorted(data.items(), key=lambda item: 1 / (0.000000001 + item[1]['추정실적_quarter'][quartar]['PBR']),
                 reverse=True)
    for n in range(len(res)):
        data[res[n][0]]['순위']['PBR'] = n
        if n != 0:
            prev = data[res[n - 1][0]]['추정실적_quarter'][quartar]['PBR']
            cur = data[res[n][0]]['추정실적_quarter'][quartar]['PBR']
            if prev == cur:
                data[res[n][0]]['순위']['PBR'] = data[res[n - 1][0]]['순위']['PBR']
        # print(n, res[n][0], res[n][1]['추정실적_quarter']['2021.09(A)']['PBR'])

    res = sorted(data.items(), key=lambda item: item[1]['추정실적_quarter'][quartar]['EPS'], reverse=True)
    for n in range(len(res)):
        data[res[n][0]]['순위']['EPS'] = n
        if n != 0:
            prev = data[res[n - 1][0]]['추정실적_quarter'][quartar]['EPS']
            cur = data[res[n][0]]['추정실적_quarter'][quartar]['EPS']
            if prev == cur:
                data[res[n][0]]['순위']['EPS'] = data[res[n - 1][0]]['순위']['EPS']
        # print(n, res[n][0], res[n][1]['추정실적_quarter']['2021.09(A)']['EPS'])

    res = sorted(data.items(), key=lambda item: item[1]['추정실적_quarter'][quartar]['ROE'], reverse=True)
    for n in range(len(res)):
        data[res[n][0]]['순위']['ROE'] = n
        if n != 0:
            prev = data[res[n - 1][0]]['추정실적_quarter'][quartar]['ROE']
            cur = data[res[n][0]]['추정실적_quarter'][quartar]['ROE']
            if prev == cur:
                data[res[n][0]]['순위']['ROE'] = data[res[n - 1][0]]['순위']['ROE']
        # print(n, res[n][0], res[n][1]['추정실적_quarter']['2021.09(A)']['ROE'])

    res = sorted(data.items(), key=lambda item: 1 / (0.000000001 + item[1]['추정실적_quarter'][quartar]['EV/EBITDA']),
                 reverse=True)
    for n in range(len(res)):
        data[res[n][0]]['순위']['EV/EBITDA'] = n
        if n != 0:
            prev = data[res[n - 1][0]]['추정실적_quarter'][quartar]['EV/EBITDA']
            cur = data[res[n][0]]['추정실적_quarter'][quartar]['EV/EBITDA']
            if prev == cur:
                data[res[n][0]]['순위']['EV/EBITDA'] = data[res[n - 1][0]]['순위']['EV/EBITDA']
        # print(n, res[n][0], res[n][1]['추정실적_quarter']['2021.09(A)']['EV/EBITDA'])

    for name, ddd in data.items():
        data[name]['순위']['종합순위'] = 0
        for item, grade in ddd['순위'].items():
            data[name]['순위']['종합순위'] += grade

    res = sorted(data.items(), key=lambda item: item[1]['순위']['종합순위'])
    for n in range(len(res)):
        print(n, res[n][0], res[n][1]['순위'])

def kospi_4q_실적():
    data = dict()
    total = len(company_code.codes_kospi)
    count = 0
    quarter = '2021.12(E)'
    for company, code in company_code.codes_kospi.items():
        d = dict()
        d['순위'] = dict()
        financial.get_estimated_performance(d, code, 1)
        if d['추정실적_quarter'].get(quarter):
            dd = d['추정실적_quarter'][quarter]
        else:
            continue

        dd['매출액(금액)'] = dd['매출액(금액)'].replace(',', '').replace('N/A', '0')
        if dd['매출액(금액)']:
            dd['매출액(금액)'] = float(dd['매출액(금액)'])
        else:
            dd['매출액(금액)'] = 0

        dd['매출액(YoY)'] = dd['매출액(YoY)'].replace(',', '').replace('N/A', '0')
        if dd['매출액(YoY)']:
            dd['매출액(YoY)'] = float(dd['매출액(YoY)'])
        else:
            dd['매출액(YoY)'] = 0

        dd['영업이익'] = dd['영업이익'].replace(',', '').replace('N/A', '0')
        if dd['영업이익']:
            dd['영업이익'] = float(dd['영업이익'])
        else:
            dd['영업이익'] = 0

        dd['당기순이익'] = dd['당기순이익'].replace(',', '').replace('N/A', '0')
        if dd['당기순이익']:
            dd['당기순이익'] = float(dd['당기순이익'])
        else:
            dd['당기순이익'] = 0

        dd['EPS'] = dd['EPS'].replace(',', '').replace('N/A', '0')
        if dd['EPS']:
            dd['EPS'] = float(dd['EPS'])
        else:
            dd['EPS'] = 0

        dd['PER'] = dd['PER'].replace(',', '').replace('N/A', '-1000')
        if dd['PER']:
            dd['PER'] = float(dd['PER'])
        else:
            dd['PER'] = -1000

        dd['PBR'] = dd['PBR'].replace(',', '').replace('N/A', '-1000')
        if dd['PBR']:
            dd['PBR'] = float(dd['PBR'])
        else:
            dd['PBR'] = -1000

        dd['ROE'] = dd['ROE'].replace(',', '').replace('N/A', '-1000')
        if dd['ROE']:
            dd['ROE'] = float(dd['ROE'])
        else:
            dd['ROE'] = -1000

        dd['EV/EBITDA'] = dd['EV/EBITDA'].replace(',', '').replace('N/A', '-1000')
        if dd['EV/EBITDA']:
            dd['EV/EBITDA'] = float(dd['EV/EBITDA'])
        else:
            dd['EV/EBITDA'] = -1000

        dd['순부채비율'] = dd['순부채비율'].replace(',', '').replace('N/A', '100')
        if dd['순부채비율']:
            dd['순부채비율'] = float(dd['순부채비율'])
        else:
            dd['순부채비율'] = 100

        data[company] = d
        count += 1
        if count % 10 == 0:
            print('{} / {}'.format(count, total))

    res = sorted(data.items(), key=lambda item: 1 / (0.000000001 + item[1]['추정실적_quarter'][quarter]['PER']),
                 reverse=True)
    for n in range(len(res)):
        data[res[n][0]]['순위']['PER'] = n
        # print(n, res[n][0], res[n][1]['추정실적_quarter']['2021.09(A)']['PER'])

    res = sorted(data.items(), key=lambda item: 1 / (0.000000001 + item[1]['추정실적_quarter'][quarter]['PBR']),
                 reverse=True)
    for n in range(len(res)):
        data[res[n][0]]['순위']['PBR'] = n
        # print(n, res[n][0], res[n][1]['추정실적_quarter']['2021.09(A)']['PBR'])

    res = sorted(data.items(), key=lambda item: item[1]['추정실적_quarter'][quarter]['EPS'], reverse=True)
    for n in range(len(res)):
        data[res[n][0]]['순위']['EPS'] = n
        # print(n, res[n][0], res[n][1]['추정실적_quarter']['2021.09(A)']['EPS'])

    res = sorted(data.items(), key=lambda item: item[1]['추정실적_quarter'][quarter]['ROE'], reverse=True)
    for n in range(len(res)):
        data[res[n][0]]['순위']['ROE'] = n
        # print(n, res[n][0], res[n][1]['추정실적_quarter']['2021.09(A)']['ROE'])

    res = sorted(data.items(), key=lambda item: 1 / (0.000000001 + item[1]['추정실적_quarter'][quarter]['EV/EBITDA']),
                 reverse=True)
    for n in range(len(res)):
        data[res[n][0]]['순위']['EV/EBITDA'] = n
        # print(n, res[n][0], res[n][1]['추정실적_quarter']['2021.09(A)']['EV/EBITDA'])

    for name, ddd in data.items():
        data[name]['순위']['종합순위'] = 0
        for item, grade in ddd['순위'].items():
            data[name]['순위']['종합순위'] += grade

    res = sorted(data.items(), key=lambda item: item[1]['순위']['종합순위'])
    for n in range(len(res)):
        print(n, res[n][0], res[n][1]['순위'])


def kosdaq_3q_실적():
    data = dict()
    total = len(company_code.codes_kosdaq)
    count = 0
    quarter = '2021.09(A)'
    for company, code in company_code.codes_kosdaq.items():
        d = dict()
        d['순위'] = dict()
        financial.get_estimated_performance(d, code, 1)
        if d['추정실적_quarter'].get(quarter):
            dd = d['추정실적_quarter'][quarter]
        else:
            continue

        dd['매출액(금액)'] = dd['매출액(금액)'].replace(',', '').replace('N/A', '0')
        if dd['매출액(금액)']:
            dd['매출액(금액)'] = float(dd['매출액(금액)'])
        else:
            dd['매출액(금액)'] = 0

        dd['매출액(YoY)'] = dd['매출액(YoY)'].replace(',', '').replace('N/A', '0')
        if dd['매출액(YoY)']:
            dd['매출액(YoY)'] = float(dd['매출액(YoY)'])
        else:
            dd['매출액(YoY)'] = 0

        dd['영업이익'] = dd['영업이익'].replace(',', '').replace('N/A', '0')
        if dd['영업이익']:
            dd['영업이익'] = float(dd['영업이익'])
        else:
            dd['영업이익'] = 0

        dd['당기순이익'] = dd['당기순이익'].replace(',', '').replace('N/A', '0')
        if dd['당기순이익']:
            dd['당기순이익'] = float(dd['당기순이익'])
        else:
            dd['당기순이익'] = 0

        dd['EPS'] = dd['EPS'].replace(',', '').replace('N/A', '0')
        if dd['EPS']:
            dd['EPS'] = float(dd['EPS'])
        else:
            dd['EPS'] = 0

        dd['PER'] = dd['PER'].replace(',', '').replace('N/A', '-1000')
        if dd['PER']:
            dd['PER'] = float(dd['PER'])
        else:
            dd['PER'] = -1000

        dd['PBR'] = dd['PBR'].replace(',', '').replace('N/A', '-1000')
        if dd['PBR']:
            dd['PBR'] = float(dd['PBR'])
        else:
            dd['PBR'] = -1000

        dd['ROE'] = dd['ROE'].replace(',', '').replace('N/A', '-1000')
        if dd['ROE']:
            dd['ROE'] = float(dd['ROE'])
        else:
            dd['ROE'] = -1000

        dd['EV/EBITDA'] = dd['EV/EBITDA'].replace(',', '').replace('N/A', '-1000')
        if dd['EV/EBITDA']:
            dd['EV/EBITDA'] = float(dd['EV/EBITDA'])
        else:
            dd['EV/EBITDA'] = -1000

        dd['순부채비율'] = dd['순부채비율'].replace(',', '').replace('N/A', '100')
        if dd['순부채비율']:
            dd['순부채비율'] = float(dd['순부채비율'])
        else:
            dd['순부채비율'] = 100

        data[company] = d
        count += 1
        if count % 10 == 0:
            print('{} / {}'.format(count, total))

    res = sorted(data.items(), key=lambda item: 1 / (0.000000001 + item[1]['추정실적_quarter'][quarter]['PER']),
                 reverse=True)
    for n in range(len(res)):
        data[res[n][0]]['순위']['PER'] = n
        # print(n, res[n][0], res[n][1]['추정실적_quarter']['2021.09(A)']['PER'])

    res = sorted(data.items(), key=lambda item: 1 / (0.000000001 + item[1]['추정실적_quarter'][quarter]['PBR']),
                 reverse=True)
    for n in range(len(res)):
        data[res[n][0]]['순위']['PBR'] = n
        # print(n, res[n][0], res[n][1]['추정실적_quarter']['2021.09(A)']['PBR'])

    res = sorted(data.items(), key=lambda item: item[1]['추정실적_quarter'][quarter]['EPS'], reverse=True)
    for n in range(len(res)):
        data[res[n][0]]['순위']['EPS'] = n
        # print(n, res[n][0], res[n][1]['추정실적_quarter']['2021.09(A)']['EPS'])

    res = sorted(data.items(), key=lambda item: item[1]['추정실적_quarter'][quarter]['ROE'], reverse=True)
    for n in range(len(res)):
        data[res[n][0]]['순위']['ROE'] = n
        # print(n, res[n][0], res[n][1]['추정실적_quarter']['2021.09(A)']['ROE'])

    res = sorted(data.items(), key=lambda item: 1 / (0.000000001 + item[1]['추정실적_quarter'][quarter]['EV/EBITDA']),
                 reverse=True)
    for n in range(len(res)):
        data[res[n][0]]['순위']['EV/EBITDA'] = n
        # print(n, res[n][0], res[n][1]['추정실적_quarter']['2021.09(A)']['EV/EBITDA'])

    for name, ddd in data.items():
        data[name]['순위']['종합순위'] = 0
        for item, grade in ddd['순위'].items():
            data[name]['순위']['종합순위'] += grade

    res = sorted(data.items(), key=lambda item: item[1]['순위']['종합순위'])
    for n in range(len(res)):
        print(n, res[n][0], res[n][1]['순위'])


def kosdaq_4q_실적():
    data = dict()
    total = len(company_code.codes_kosdaq)
    count = 0
    quarter = '2021.12(E)'
    for company, code in company_code.codes_kosdaq.items():
        d = dict()
        d['순위'] = dict()
        financial.get_estimated_performance(d, code, 1)
        if d['추정실적_quarter'].get(quarter):
            dd = d['추정실적_quarter'][quarter]
        else:
            continue

        dd['매출액(금액)'] = dd['매출액(금액)'].replace(',', '').replace('N/A', '0')
        if dd['매출액(금액)']:
            dd['매출액(금액)'] = float(dd['매출액(금액)'])
        else:
            dd['매출액(금액)'] = 0

        dd['매출액(YoY)'] = dd['매출액(YoY)'].replace(',', '').replace('N/A', '0')
        if dd['매출액(YoY)']:
            dd['매출액(YoY)'] = float(dd['매출액(YoY)'])
        else:
            dd['매출액(YoY)'] = 0

        dd['영업이익'] = dd['영업이익'].replace(',', '').replace('N/A', '0')
        if dd['영업이익']:
            dd['영업이익'] = float(dd['영업이익'])
        else:
            dd['영업이익'] = 0

        dd['당기순이익'] = dd['당기순이익'].replace(',', '').replace('N/A', '0')
        if dd['당기순이익']:
            dd['당기순이익'] = float(dd['당기순이익'])
        else:
            dd['당기순이익'] = 0

        dd['EPS'] = dd['EPS'].replace(',', '').replace('N/A', '0')
        if dd['EPS']:
            dd['EPS'] = float(dd['EPS'])
        else:
            dd['EPS'] = 0

        dd['PER'] = dd['PER'].replace(',', '').replace('N/A', '-1000')
        if dd['PER']:
            dd['PER'] = float(dd['PER'])
        else:
            dd['PER'] = -1000

        dd['PBR'] = dd['PBR'].replace(',', '').replace('N/A', '-1000')
        if dd['PBR']:
            dd['PBR'] = float(dd['PBR'])
        else:
            dd['PBR'] = -1000

        dd['ROE'] = dd['ROE'].replace(',', '').replace('N/A', '-1000')
        if dd['ROE']:
            dd['ROE'] = float(dd['ROE'])
        else:
            dd['ROE'] = -1000

        dd['EV/EBITDA'] = dd['EV/EBITDA'].replace(',', '').replace('N/A', '-1000')
        if dd['EV/EBITDA']:
            dd['EV/EBITDA'] = float(dd['EV/EBITDA'])
        else:
            dd['EV/EBITDA'] = -1000

        dd['순부채비율'] = dd['순부채비율'].replace(',', '').replace('N/A', '100')
        if dd['순부채비율']:
            dd['순부채비율'] = float(dd['순부채비율'])
        else:
            dd['순부채비율'] = 100

        data[company] = d
        count += 1
        if count % 10 == 0:
            print('{} / {}'.format(count, total))

    res = sorted(data.items(), key=lambda item: 1 / (0.000000001 + item[1]['추정실적_quarter'][quarter]['PER']),
                 reverse=True)
    for n in range(len(res)):
        data[res[n][0]]['순위']['PER'] = n
        # print(n, res[n][0], res[n][1]['추정실적_quarter']['2021.09(A)']['PER'])

    res = sorted(data.items(), key=lambda item: 1 / (0.000000001 + item[1]['추정실적_quarter'][quarter]['PBR']),
                 reverse=True)
    for n in range(len(res)):
        data[res[n][0]]['순위']['PBR'] = n
        # print(n, res[n][0], res[n][1]['추정실적_quarter']['2021.09(A)']['PBR'])

    res = sorted(data.items(), key=lambda item: item[1]['추정실적_quarter'][quarter]['EPS'], reverse=True)
    for n in range(len(res)):
        data[res[n][0]]['순위']['EPS'] = n
        # print(n, res[n][0], res[n][1]['추정실적_quarter']['2021.09(A)']['EPS'])

    res = sorted(data.items(), key=lambda item: item[1]['추정실적_quarter'][quarter]['ROE'], reverse=True)
    for n in range(len(res)):
        data[res[n][0]]['순위']['ROE'] = n
        # print(n, res[n][0], res[n][1]['추정실적_quarter']['2021.09(A)']['ROE'])

    res = sorted(data.items(), key=lambda item: 1 / (0.000000001 + item[1]['추정실적_quarter'][quarter]['EV/EBITDA']),
                 reverse=True)
    for n in range(len(res)):
        data[res[n][0]]['순위']['EV/EBITDA'] = n
        # print(n, res[n][0], res[n][1]['추정실적_quarter']['2021.09(A)']['EV/EBITDA'])

    for name, ddd in data.items():
        data[name]['순위']['종합순위'] = 0
        for item, grade in ddd['순위'].items():
            data[name]['순위']['종합순위'] += grade

    res = sorted(data.items(), key=lambda item: item[1]['순위']['종합순위'])
    for n in range(len(res)):
        print(n, res[n][0], res[n][1]['순위'])

def investment_opinion_순위(codes):
    data = dict()
    for company, code in codes.items():
        d = dict()
        d['순위'] = dict()
        financial.get_investment_opinion_naver(d, code)
        financial.get_sise_naver_api(d, code)
        if d['투자의견']['목표주가'] == 0 or d['시세']['주가'] == 0:
            d['투자의견']['목표주가율'] = 0
        else:
            d['투자의견']['목표주가율'] = (d['투자의견']['목표주가'] - d['시세']['주가']) / d['시세']['주가']
        data[company] = d

    res = sorted(data.items(), key=lambda item: item[1]['투자의견']['목표주가율'], reverse=True)
    for n in range(len(res)):
        if n == 0:
            data[res[n][0]]['순위']['목표주가율'] = n
        else:
            prev = data[res[n - 1][0]]['투자의견']['목표주가율']
            cur = data[res[n][0]]['투자의견']['목표주가율']
            if prev == cur:
                data[res[n][0]]['순위']['목표주가율'] = data[res[n - 1][0]]['순위']['목표주가율']
            else:
                data[res[n][0]]['순위']['목표주가율'] = n
        # print(n, res[n][0], res[n][1]['투자의견']['목표주가율'], data[res[n][0]]['순위']['목표주가율'])

    res = sorted(data.items(), key=lambda item: item[1]['투자의견']['투자의견'], reverse=True)
    for n in range(len(res)):
        if n == 0:
            data[res[n][0]]['순위']['투자의견'] = n
        else:
            prev = data[res[n - 1][0]]['투자의견']['투자의견']
            cur = data[res[n][0]]['투자의견']['투자의견']
            if prev == cur:
                data[res[n][0]]['순위']['투자의견'] = data[res[n - 1][0]]['순위']['투자의견']
            else:
                data[res[n][0]]['순위']['투자의견'] = n
        # print(n, res[n][0], res[n][1]['투자의견']['투자의견'], data[res[n][0]]['순위']['투자의견'])

    for name, d in data.items():
        data[name]['순위']['순위합'] = data[name]['순위']['목표주가율'] + data[name]['순위']['투자의견']

    print('종합순위\t종목\t순위합\t목표주가율순위\t목표주가율\t투자의견순위\t투자의견')
    res = sorted(data.items(), key=lambda item: item[1]['순위']['순위합'])
    for n in range(len(res)):
        if n == 0:
            data[res[n][0]]['순위']['최종순위'] = n
        else:
            prev = data[res[n - 1][0]]['순위']['순위합']
            cur = data[res[n][0]]['순위']['순위합']
            if prev == cur:
                data[res[n][0]]['순위']['최종순위'] = data[res[n - 1][0]]['순위']['최종순위']
            else:
                data[res[n][0]]['순위']['최종순위'] = n
        print("{}\t{}\t{}\t{}\t{:.2f}\t{}\t{}".format(data[res[n][0]]['순위']['최종순위'],
              res[n][0],
              data[res[n][0]]['순위']['순위합'],
              data[res[n][0]]['순위']['목표주가율'],
              data[res[n][0]]['투자의견']['목표주가율'],
              data[res[n][0]]['순위']['투자의견'],
              data[res[n][0]]['투자의견']['투자의견']))

def test_investment_opinion():
    print('kosdaq / kospi 순위')
    codecs = dict()

    codecs.update(company_code.codes_kosdaq)
    codecs.update(company_code.codes_kospi)

    # codecs.update(company_code.codes)

    investment_opinion_순위(codecs)

test_investment_opinion()

# print("get_company_code_kosdq()")
# company_code.get_company_code_kosdq()