import folium
import random

def random_european_city():
    cities = [
        {"name": "London", "lat": 51.5074, "lon": -0.1278},
        {"name": "Paris", "lat": 48.8566, "lon": 2.3522},
        {"name": "Berlin", "lat": 52.5200, "lon": 13.4050},
        {"name": "Madrid", "lat": 40.4168, "lon": -3.7038},
        {"name": "Rome", "lat": 41.9028, "lon": 12.4964},
        {"name": "London", "lat": 51.5074, "lon": -0.1278},
        {"name": "Paris", "lat": 48.8566, "lon": 2.3522},
        {"name": "Berlin", "lat": 52.5200, "lon": 13.4050},
        {"name": "Madrid", "lat": 40.4168, "lon": -3.7038},
        {"name": "Rome", "lat": 41.9028, "lon": 12.4964},
        {"name": "Prague", "lat": 50.0755, "lon": 14.4378},
        {"name": "Lisbon", "lat": 38.7223, "lon": -9.1393},
        {"name": "Vienna", "lat": 48.2082, "lon": 16.3738},
        {"name": "Dublin", "lat": 53.3498, "lon": -6.2603},
        {"name": "Barcelona", "lat": 41.3851, "lon": 2.1734},
        {"name": "Amsterdam", "lat": 52.3676, "lon": 4.9041},
        {"name": "Budapest", "lat": 47.4979, "lon": 19.0402},
        {"name": "Brussels", "lat": 50.8503, "lon": 4.3517},
        {"name": "Athens", "lat": 37.9838, "lon": 23.7275},
        {"name": "Stockholm", "lat": 59.3293, "lon": 18.0686},
        {"name": "Oslo", "lat": 59.9139, "lon": 10.7522}
        # Add as many cities as you want here...
    ]
    return random.choice(cities)

def visualize_city_on_map(city):
    m = folium.Map(location=[city["lat"], city["lon"]], zoom_start=4)
    
    # Add a marker for the city with an icon
    folium.Marker(
        [city["lat"], city["lon"]],
        tooltip=city["name"],
        icon=folium.CustomIcon(icon_image="bullseye-with-dart-icon-image-vector-15032045.jpg",
                               icon_size=(30, 30))
    ).add_to(m)
    
    m.save('europe_map.html')

if __name__ == '__main__':
    city = random_european_city()
    print(f"Selected city: {city['name']}")
    visualize_city_on_map(city)