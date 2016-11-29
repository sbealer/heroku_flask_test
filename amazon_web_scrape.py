
import mechanize
import cookielib
import codecs
import os


#########################################################################
base_url = "https://sellercentral.amazon.com"
sign_in_form = "https://sellercentral.amazon.com/ap/widget"
sign_in_url = 'https://sellercentral.amazon.com/gp/homepage.html'
reports_url = base_url + "/gp/site-metrics/load/csv/page_sales_and_traffic_detail.csv"



#########################################################################

def get_data(account_info, requested_report, start_date, end_date):
    # Browser
    br = mechanize.Browser()

    # Cookie Jar
    cj = cookielib.LWPCookieJar()
    br.set_cookiejar(cj)

    # Browser options
    br.set_handle_equiv(True)
    br.set_handle_redirect(True)
    br.set_handle_referer(True)
    br.set_handle_robots(False)

    # Follows refresh 0 but not hangs on refresh > 0
    br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)

    # User-Agent
    br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]

    r = br.open(sign_in_url)

    br.select_form(name='signinWidget')

    # Let's login

    ##################################
    br.form['username']=os.environ['AZN_AUTH1']
    br.form['password']=os.environ['AZN_AUTH2']
    ##################################
    br.submit()

    print "Logged in."
    report_params = {"cols":"/c0/c1/c2/c3/c4/c5/c6/c7/c8/c9/c10/c11/c12",
         #  "sortColumn":"13",
            "fromDate":start_date,
            "toDate":end_date,
            "reportID":requested_report,
           # "sortIsAscending":"0",
           # "currentPage":"0",
            "dateUnit":"1"
            }

    req = br.click_link(text='Business Reports')
    print "Attempting to open form."
    br.open(req)
    print "Link clicked"

    br.select_form(predicate=lambda f: f.attrs.get('id', None) == 'dwnldFormCSV')
    br.form.set_all_readonly(False)
    for k,v in report_params.iteritems():
        br.form[k]=v
    print "Attempting to get data..."
    r = br.submit()
    import csv
    csv = csv.reader(r.read().splitlines())

    for row in csv:
        if row[0].startswith(codecs.BOM_UTF8):
            row[0] = row[0][3:]
        print row

    return list(csv)

