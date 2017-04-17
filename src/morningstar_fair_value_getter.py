import urllib2
import urllib
from time import sleep
import time

sectors = ['Basic Materials',
'Financial Services',
'Consumer Cyclical',
'Healthcare',
'Technology',
'Industrials',
'Real Estate',
'Consumer Defensive',
'Communication Services',
'Utilities',
'Energy']


industry = ['Advertising Agencies',
'Aerospace & Defense',
'Agricultural Inputs',
'Airlines',
'Airports & Air Services',
'Aluminum',
'Apparel Manufacturing',
'Apparel Stores',
'Asset Management',
'Auto & Truck Dealerships',
'Auto Manufacturers',
'Auto Parts',
'Banks - Global',
'Banks - Regional - Africa',
'Banks - Regional - Asia',
'Banks - Regional - Australia',
'Banks - Regional - Canada',
'Banks - Regional - Europe',
'Banks - Regional - Latin America',
'Banks - Regional - US',
'Beverages - Brewers',
'Beverages - Soft Drinks',
'Beverages - Wineries & Distilleries',
'Biotechnology',
'Broadcasting - Radio',
'Broadcasting - TV',
'Building Materials',
'Business Equipment',
'Business Services',
'Capital Markets',
'Chemicals',
'Coal',
'Communication Equipment',
'Computer Distribution',
'Computer Systems',
'Confectioners',
'Conglomerates',
'Consumer Electronics',
'Contract Manufacturers',
'Copper',
'Credit Services',
'Data Storage',
'Department Stores',
'Diagnostics & Research',
'Discount Stores',
'Diversified Industrials',
'Drug Manufacturers - Major',
'Drug Manufacturers - Specialty & Generic',
'Education & Training Services',
'Electronic Components',
'Electronic Gaming & Multimedia',
'Electronics Distribution',
'Engineering & Construction',
'Farm & Construction Equipment',
'Farm Products',
'Financial Exchanges',
'Food Distribution',
'Footwear & Accessories',
'Gambling',
'Gold',
'Grocery Stores',
'Health Care Plans',
'Health Information Services',
'Home Furnishings & Fixtures',
'Home Improvement Stores',
'Household & Personal Products',
'Industrial Distribution',
'Industrial Metals & Minerals',
'Information Technology Services',
'Infrastructure Operations',
'Insurance - Diversified',
'Insurance - Life',
'Insurance - Property & Casualty',
'Insurance - Reinsurance',
'Insurance - Specialty',
'Insurance Brokers',
'Integrated Shipping & Logistics',
'Internet Content & Information',
'Leisure',
'Lodging',
'Long-Term Care Facilities',
'Lumber & Wood Production',
'Luxury Goods',
'Marketing Services',
'Media - Diversified',
'Medical Care',
'Medical Devices',
'Medical Distribution',
'Medical Instruments & Supplies',
'Metal Fabrication',
'Oil & Gas Drilling',
'Oil & Gas E&P',
'Oil & Gas Equipment & Services',
'Oil & Gas Integrated',
'Oil & Gas Midstream',
'Oil & Gas Refining & Marketing',
'Packaged Foods',
'Packaging & Containers',
'Paper & Paper Products',
'Pay TV',
'Personal Services',
'Pharmaceutical Retailers',
'Pollution & Treatment Controls',
'Publishing',
'Railroads',
'Real Estate - General',
'Real Estate Services',
'Recreational Vehicles',
'REIT - Diversified',
'REIT - Healthcare Facilities',
'REIT - Hotel & Motel',
'REIT - Industrial',
'REIT - Office',
'REIT - Residential',
'REIT - Retail',
'Rental & Leasing Services',
'Residential Construction',
'Resorts & Casinos',
'Restaurants',
'Rubber & Plastics',
'Savings & Cooperative Banks',
'Scientific & Technical Instruments',
'Security & Protection Services',
'Semiconductor Equipment & Materials',
'Semiconductor Memory',
'Semiconductors',
'Shipping & Ports',
'Silver',
'Software - Application',
'Software - Infrastructure',
'Solar',
'Specialty Chemicals',
'Specialty Finance',
'Specialty Retail',
'Staffing & Outsourcing Services',
'Steel',
'Telecom Services',
'Textile Manufacturing',
'Tobacco',
'Tools & Accessories',
'Truck Manufacturing',
'Trucking',
'Utilities - Diversified',
'Utilities - Independent Power Producers',
'Utilities - Regulated Electric',
'Utilities - Regulated Gas',
'Utilities - Regulated Water',
'Waste Management']

#1=sector; 2=sub-sector industry
doWhat = 2

tickerQuery = "http://www.morningstar.com/market-valuation/info.aspx?Ticker={0}&Period=Y3"

if doWhat == 1:
    with open("mstar_sector.txt", 'w') as f:
        for ticker in sectors:
            quoted = urllib.quote(ticker)
            resp = urllib2.urlopen(tickerQuery.format(quoted)).read()
            f.write(ticker + "|" + resp + "\n")
            time.sleep(5)

if doWhat == 2:
    with open("mstar_industry.txt", 'w') as f:
        for ticker in industry:
            quoted = urllib.quote(ticker)
            resp = urllib2.urlopen(tickerQuery.format(quoted)).read()
            f.write(ticker + "|" + resp + "\n")
            time.sleep(5)
                    

