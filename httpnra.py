import webbrowser

year = [2019]
month = [2]
day = [26,27]
for yr in year:
    for mnth in month:
        for dy in day:
            if dy <= 9:

                webbrowser.open('https://data.tii.ie/Datasets/TrafficCountData/{yy}/0{mm}/0{dd}/per-site-class-aggr-{yy}-0{mm}-0{dd}.csv'.format(yy = yr, mm = mnth, dd = dy))
            else:
                webbrowser.open('https://data.tii.ie/Datasets/TrafficCountData/{yy}/0{mm}/{dd}/per-site-class-aggr-{yy}-0{mm}-{dd}.csv'.format(yy = yr, mm = mnth, dd = dy))

