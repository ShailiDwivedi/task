from task import get_api_data as api
from select_data import check_data 
from insert_data_into_table import insert_query


def insert_data():
     
     for i in range(16):
        res = api("https://api.worldbank.org/v2/country/ARG;BOL;BRA;CHL;COL;ECU;GUY;PRY;PER;SUR;URY;VEN/indicator/NY.GDP.MKTP.CD?format=json&page=1&per_page=50")   
    
        for item in res[1]:
            ID = item.get("country").get("id")
            name = item.get("country").get("value")
            codeiso = item.get("countryiso3code")
            date = item.get("date")
            value = item.get("value")
            result = check_data(f"""SELECT * FROM country where id='{ID}'""")
            if len(result) == 0:
                insert_query(f"""
                            INSERT INTO country (id, name ,iso3_code) VALUES ('{ID}', '{name}', '{codeiso}')
                                """)
            if value is not None:  # Check if value is not None
                    insert_query(f"""
                        INSERT INTO gdp (country_id, year ,value) VALUES ('{ID}', '{date}', '{value}')
                            """)
            else:
                # Insert NULL for the value if it is None
                insert_query(f"""
                        INSERT INTO gdp (country_id, year ,value) VALUES ('{ID}', '{date}', NULL)
                            """)

insert_data()
