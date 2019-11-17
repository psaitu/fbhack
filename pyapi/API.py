# -*- coding: utf-8 -*-
from flask import Flask, request
# from flask_mysqldb import MySQL
import wikipedia
from flask import send_file
import numpy as np
import matplotlib.pyplot as plt
try:
    import urllib.request as urllib2
except ImportError:
    import urllib2
import json, requests
from random import randint
from flask import jsonify
import smtplib
from smtplib import SMTPException

# mysql = MySQL()
app = Flask(__name__)
# app.config['MYSQL_DATABASE_USER'] = 'man'
# app.config['MYSQL_DATABASE_PASSWORD'] = 'admin1'
# app.config['MYSQL_DATABASE_DB'] = 'Data'
# app.config['MYSQL_DATABASE_HOST'] = 'localhost'
# mysql.init_app(app)
# pwd = 'Admin12345!'

@app.route("/")
def hello():
    return "<h2><u>MetaData Parser</u></h2><h4>For 10q:</h4>Data:http://127.0.0.1:5000/10q/FinData?Datatype=</br>Plots:http://127.0.0.1:5000/10q/FinPlot?Imgtype=<h4>For 10k:</h4>Data:http://127.0.0.1:5000/10k/FinData?Datatype=</br>Plots:http://127.0.0.1:5000/10k/FinPlot?Imgtype=<h4>For 8k:</h4>Data:http://127.0.0.1:5000/8k/FinData?Datatype=</br>Plots:http://127.0.0.1:5000/8k/FinPlot?Imgtype="

@app.route("/Data")
def geData():
    #content = urllib2.urlopen("https://www.quandl.com/api/v3/datatables/SHARADAR/SF1.json?ticker=AAPL&calendardate=2015-12-31&dimension=MRY&api_key=WyHRuMayFcNMsuCyMYSz").read()
    #temp = content[3][0][0]
    url = 'https://www.quandl.com/api/v3/datatables/SHARADAR/SF1.json?ticker=AAPL&calendardate=2015-12-31&dimension=MRY&api_key=WyHRuMayFcNMsuCyMYSz'
    resp = requests.get(url=url)
    data = json.loads(resp.content)    
    #res = data.json()
    #res = jsonify(data)
    # da = response.json(res)
    #response = requests.post(url)
    #data = response.json()
    return res

@app.route("/PlotImage")
def genPlotImage():
    n_groups = 5

    plt.switch_backend('Agg')

    compA = [randint(40,50), randint(40,50), randint(40,50), randint(40,50), randint(40,50)]
    compAstd = [2, 3, 4, 1, 2]    

    fig, ax = plt.subplots()
    index = np.arange(n_groups)
    bar_width = 0.35
    opacity = 0.4
    
    company1 = request.args.get('comp1')    

    plt.xlabel('Year')
    plt.ylabel('(in $)')
    plt.title(company1)
    plt.xticks(index + bar_width, ('2010', '2011', '2012', '2013', '2014'))

    rects1 = plt.bar(index, compA, bar_width,alpha=opacity,yerr=compAstd,color='b',label='')    

    plt.legend()
    plt.tight_layout()
    plt.savefig('/Users/prabhusaitu/Documents/fbhack/fb-hackathon/public/images/msft.png')
    filename = "/Users/prabhusaitu/Documents/fbhack/fb-hackathon/public/images/msft.png"
    return send_file(filename, mimetype='image/png')

@app.route("/CompareImage")
def genImage():
    n_groups = 5

    plt.switch_backend('Agg')

    compA = [randint(40,50), randint(40,50), randint(40,50), randint(40,50), randint(40,50)]
    compAstd = [2, 3, 4, 5, 2]

    compB = [randint(40,50), randint(40,50), randint(40,50), randint(40,50), randint(40,50)]
    compBstd = [3, 5, 2, 5, 2]

    fig, ax = plt.subplots()
    index = np.arange(n_groups)
    bar_width = 0.35
    opacity = 0.4    
    
    company1 = request.args.get('comp1')
    company2 = request.args.get('comp2')
    
    '''plt.xlabel('Paramaters')'''
    plt.ylabel(' (in %)')
    plt.title(company1 + ' vs ' + company2 )
    plt.xticks(index + bar_width, ('2010', '2011', '2012','2013','2014'))

    rects1 = plt.bar(index, compA, bar_width,alpha=opacity,yerr=compAstd,color='b',label='')

    rects2 = plt.bar(index + bar_width, compB, bar_width,alpha=opacity,color='r',yerr=compBstd,label='')

    plt.legend()
    plt.tight_layout()
    plt.savefig('/Users/prabhusaitu/Documents/fbhack/fb-hackathon/public/images/comp.png')
    filename = "/Users/prabhusaitu/Documents/fbhack/fb-hackathon/public/images/comp.png"
    return send_file(filename, mimetype='image/png')


@app.route("/Summary")
def Summarize():
    liabilitesData = ['Certain forecasted transactions, assets, and liabilities are exposed to foreign currency risk. We monitor our foreign currency exposures daily to maximize the economic effectiveness of our foreign currency hedge positions. Option and forward contracts are used to hedge a portion of forecasted international revenue for up to three years in the future and are designated as cash-flow hedging instruments. Principal currencies hedged include the euro, Japanese yen, British pound, and Canadian dollar. As of March 31, 2015 and June 30, 2014, the total notional amounts of these foreign exchange contracts sold were $9.4 billion and $4.9 billion, respectively.^Tax contingencies and other tax liabilities were $11.8 billion and $10.4 billion as of March 31, 2015 and June 30, 2014, respectively, and are included in other long-term liabilities. This increase relates primarily to current period quarterly growth relating to intercompany transfer pricing adjustments. While we settled a portion of the Internal Revenue Service (“I.R.S.”) audit for tax years 2004 to 2006 during the third quarter of fiscal year 2011, we remain under audit for those years. In February 2012, the I.R.S. withdrew its 2011 Revenue Agents Report and reopened',
    'Tax contingencies and other tax liabilities were $11.8 billion and $10.4 billion as of March 31, 2015 and June 30, 2014, respectively, and are included in other long-term liabilities. This increase relates primarily to current period quarterly growth relating to intercompany transfer pricing adjustments. While we settled a portion of the Internal Revenue Service (“I.R.S.”) audit for tax years 2004 to 2006 during the third quarter of fiscal year 2011, we remain under audit for those years. In February 2012, the I.R.S. withdrew its 2011 Revenue Agents Report and reopened^In general, and where applicable, we use quoted prices in active markets for identical assets or liabilities to determine the fair value of our financial instruments. This pricing methodology applies to our Level 1 investments, such as exchange-traded mutual funds, domestic and international equities, and U.S. government securities. If quoted prices in active markets for identical assets or liabilities are not available to determine fair value, then we use quoted prices for similar assets and liabilities or inputs other than the quoted prices that are observable either directly']
    GenData = ["As of March 31, 2015 and June 30, 2014, the recorded bases of common and preferred stock that are restricted for more than one year or are not publicly traded were $538 million and $520 million, respectively. These investments are carried at cost and are reviewed quarterly for indicators of other-than-temporary impairment.^As of March 31, 2015, the total notional amounts of fixed-interest rate contracts purchased and sold were $2.1 billion and $2.8 billion, respectively. As of June 30, 2014, the total notional amounts of fixed-interest rate contracts purchased and sold were $1.7 billion and $936 million, respectively.^ On November 6, 2014, we acquired Mojang Synergies AB (“Mojang”), the Swedish video game developer of the Minecraft gaming franchise, for $2.5 billion in cash, net of cash acquired. The addition of Minecraft and its community enhances our gaming portfolio across Windows, Xbox, and other ecosystems and devices outside our own.","The Company uses a variety of direct and indirect distribution channels, such as its retail stores, online stores, and direct sales force, and third-party cellular network carriers, wholesalers, retailers, and value-added resellers. The Company believes that sales of its innovative and differentiated products are enhanced by knowledgeable salespersons who can convey the value of the hardware and software integration, and demonstrate the unique solutions that are available on its products.^The Company further believes providing direct contact with its targeted customers is an effective way to demonstrate the advantages of its products over those of its competitors and providing a high-quality sales and after-sales support experience is critical to attracting new and retaining existing customers. To ensure a high-quality buying experience for its products in which service and education are emphasized, the Company continues to expand and improve its distribution capabilities by expanding the number of its own retail stores worldwide.^The preparation of financial statements and related disclosures in conformity with U.S. generally accepted accounting principles (“GAAP”) and the Company’s discussion and analysis of its financial condition and operating results require the Company’s management to make judgments, assumptions and estimates that affect the amounts reported in its consolidated financial statements and accompanying notes."]    
    revenueData = "We generate revenue by developing, licensing, and supporting a wide range of software products and services, by designing and selling hardware devices, and by delivering relevant online advertising to a global customer audience. In addition to selling individual products and services, we offer suites of products and services.^Approximately 80% of Server and Tools revenue comes from product revenue, including purchases through volume licensing programs, licenses sold to OEMs, and retail packaged product, while the remainder comes from Enterprise Services.^During fiscal years 2013, 2012, and 2011, research and development expense was $10.4 billion, $9.8 billion, and $9.0 billion, respectively. These amounts represented 13% of revenue in each of those years. We plan to continue to make significant investments in a broad range of research and development efforts."
    res = GenData[randint(0,1)]
    param = request.args.get('Sum')
    if param == 'liabilities':
        res = liabilitesData[randint(0,1)]
    if param == 'revenue':
        res = revenueData
    return res

@app.route("/Mail") 
def send_email():
    user = 'mvdmanish4@gmail.com'    
    recipient = request.args.get('Mailto').decode('utf-8')
    subject = '10q Filing'
    #body = 'As of March 31, 2015 and June 30, 2014, the recorded bases of common and preferred stock that are restricted for more than one year or are not publicly traded were $538 million and $520 million, respectively. These investments are carried at cost and are reviewed quarterly for indicators of other-than-temporary impairment.As of March 31, 2015, the total notional amounts of fixed-interest rate contracts purchased and sold were $2.1 billion and $2.8 billion, respectively. As of June 30, 2014, the total notional amounts of fixed-interest rate contracts purchased and sold were $1.7 billion and $936 million, respectively. On November 6, 2014, we acquired Mojang Synergies AB (“Mojang”), the Swedish video game developer of the Minecraft gaming franchise, for $2.5 billion in cash, net of cash acquired. The addition of Minecraft and its community enhances our gaming portfolio across Windows, Xbox, and other ecosystems and devices outside our own.'
    body = 'As of March 31, 2015 and June 30, 2014, the recorded bases of common and preferred stock that are restricted for more than one year or are not publicly traded were $538 million and $520 million, respectively. These investments are carried at cost and are reviewed quarterly for indicators of other-than-temporary impairment.As of March 31, 2015, the total notional amounts of fixed-interest rate contracts purchased and sold were $2.1 billion and $2.8 billion, respectively.'
    mail_user = user
    mail_pwd = pwd
    FROM = user
    TO = recipient if type(recipient) is list else [recipient]
    SUBJECT = subject
    TEXT = body

    message = """\From: %s\nTo: %s\nSubject: %s\n\n%s
    """ % (FROM, ", ".join(TO), SUBJECT, TEXT)
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.login(mail_user, mail_pwd)
        server.sendmail(FROM, TO, message)
        server.close()
        res1 = 'Email Sent!'
    except:
        res1 = 'ABORT!'
    return res1   
    
@app.route("/Definition")
def Define():
    term = request.args.get('Def')    
    try:
        res = wikipedia.summary(term,sentences=2)    
    except:
        res = 'Sorry, I did not understand. Please re-enter the term with more context.'
    return res

if __name__ == "__main__":
    app.debug = True
    app.run()