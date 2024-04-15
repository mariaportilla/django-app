import requests
import os


def get_commet_data(api_key):
    print("::: COMETS INFORMATION")
    api_url= f"https://api.nasa.gov/neo/rest/v1/neo/3726712?api_key={api_key}"

    try:
        response = requests.get(api_url)
        response.raise_for_status()
        data = response.json()

        #Show:
        os.system('clear')
        #Comet name
        print(f"Comet name: {data['name']}")

        #Absolute magnitude
        #Estimated diameter max (KM)
        #Estimated diameter min (KM)
        #Estimated diameter max (FT)
        #Estimated diameter min (FT)
        #Orbital_data:

    except requests.exceptions.RequestException as e:
            print(f"API error {e}")

    #main
    api_key_nasa='nPAMagtcH7GXLkfZTxul3X7DIjlYT7JspHpq1vMK'
    get_commet_data(api_key_nasa)