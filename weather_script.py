import requests

# Configuración de la API
API_KEY = "TU_API_KEY"  # Reemplaza con tu clave de API de OpenWeatherMap
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def obtener_clima(ciudad):
    """
    Obtiene los datos meteorológicos de una ciudad específica usando la API de OpenWeatherMap.
    """
    try:
        # Parámetros de la solicitud
        params = {
            "q": ciudad,
            "appid": API_KEY,
            "units": "metric",  # Para obtener la temperatura en grados Celsius
            "lang": "es"       # Idioma español
        }

        # Realizar la solicitud a la API
        respuesta = requests.get(BASE_URL, params=params)
        respuesta.raise_for_status()  # Lanza una excepción si hay un error HTTP

        # Procesar los datos de la respuesta
        datos = respuesta.json()
        clima = {
            "ciudad": datos["name"],
            "temperatura": datos["main"]["temp"],
            "descripcion": datos["weather"][0]["description"],
            "humedad": datos["main"]["humidity"],
            "viento": datos["wind"]["speed"]
        }
        return clima

    except requests.exceptions.RequestException as e:
        return f"Error al conectar con la API: {e}"
    except KeyError:
        return "Error al procesar los datos de la API."

def main():
    print("Aplicación de Clima - OpenWeatherMap")
    ciudad = input("Ingresa el nombre de la ciudad: ")
    clima = obtener_clima(ciudad)

    if isinstance(clima, dict):
        print(f"\nClima en {clima['ciudad']}:")
        print(f"Temperatura: {clima['temperatura']}°C")
        print(f"Descripción: {clima['descripcion']}")
        print(f"Humedad: {clima['humedad']}%")
        print(f"Velocidad del viento: {clima['viento']} m/s")
    else:
        print(clima)

if __name__ == "__main__":
    main()