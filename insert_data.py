from task import get_api_data as api
from select_data import check_data 
from insert_data_into_table import insert_query

firstcall = api("https://api.worldbank.org/v2/country/ARG;BOL;BRA;CHL;COL;ECU;GUY;PRY;PER;SUR;URY;VEN/indicator/NY.GDP.MKTP.CD?format=json&page=1&per_page=50") 

print(firstcall)
# print(res[0]["pages"])
def insert_data():
    for i in range(1,firstcall[0]["pages"]+1):
        #{'page': 1, 'pages': 16, 'per_page': 50, 'total': 768, 'sourceid': '2', 'lastupdated': '2024-05-30'}
        res = api(f"""https://api.worldbank.org/v2/country/ARG;BOL;BRA;CHL;COL;ECU;GUY;PRY;PER;SUR;URY;VEN/indicator/NY.GDP.MKTP.CD?format=json&page={i}&per_page=50""") 
    
        for item in res[1]:
            ID = item.get("country").get("id")
            name = item.get("country").get("value")
            codeiso = item.get("countryiso3code")
            date = item.get("date")
            value = item.get("value")
            country_list = check_data(f"""SELECT * FROM country where id='{ID}'""")
            if len(country_list) == 0:
                insert_query(f"""
                            INSERT INTO country (id, name ,iso3_code) VALUES ('{ID}', '{name}', '{codeiso}')
                                """)
            if value is not None:  # Check if value is not None
                    insert_query(f"""
                        INSERT INTO gdp (country_id, year ,value) VALUES ('{ID}', '{date}', '{value}')
                            """)
            else:
                
                insert_query(f"""
                        INSERT INTO gdp (country_id, year ,value) VALUES ('{ID}', '{date}', NULL)
                            """)

# insert_data()

# SELECT 
#     c.id,
#     c.name,
#     c.iso3_code,
#     ROUND(SUM(CASE WHEN g.year = '2019' THEN g.value / 1000000000 ELSE 0 END), 2) AS '2019',
#     ROUND(SUM(CASE WHEN g.year = '2020' THEN g.value / 1000000000 ELSE 0 END), 2) AS '2020',
#     ROUND(SUM(CASE WHEN g.year = '2021' THEN g.value / 1000000000 ELSE 0 END), 2) AS '2021',
#     ROUND(SUM(CASE WHEN g.year = '2022' THEN g.value / 1000000000 ELSE 0 END), 2) AS '2022',
#     ROUND(SUM(CASE WHEN g.year = '2023' THEN g.value / 1000000000 ELSE 0 END), 2) AS '2023'
# FROM 
#     country c 
# INNER JOIN 
#     gdp g ON c.id = g.country_id
# GROUP BY 
#     c.id, c.name, c.iso3_code;
