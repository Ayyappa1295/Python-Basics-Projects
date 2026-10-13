
import tkinter as tk
from tkinter import messagebox
import requests
from datetime import datetime

# ---------------- WEATHER CODES ----------------

WEATHER_CODES = {
    0: "Clear Sky ☀️",
    1: "Mainly Clear 🌤️",
    2: "Partly Cloudy ⛅",
    3: "Overcast ☁️",
    45: "Foggy 🌫️",
    48: "Rime Fog 🌫️",
    51: "Light Drizzle 🌦️",
    53: "Moderate Drizzle 🌦️",
    55: "Heavy Drizzle 🌧️",
    61: "Light Rain 🌧️",
    63: "Moderate Rain 🌧️",
    65: "Heavy Rain 🌧️",
    71: "Light Snow 🌨️",
    73: "Moderate Snow ❄️",
    75: "Heavy Snow ❄️",
    80: "Rain Showers 🌦️",
    81: "Heavy Rain Showers 🌧️",
    82: "Violent Rain Showers ⛈️",
    95: "Thunderstorm ⛈️",
    96: "Thunderstorm with Hail ⛈️",
    99: "Heavy Thunderstorm ⛈️"
}


# ---------------- WEATHER FUNCTIONS ----------------

def get_city_coordinates(city):
    url = "https://geocoding-api.open-meteo.com/v1/search"

    params = {
        "name": city,
        "count": 1,
        "language": "en",
        "format": "json"
    }

    response = requests.get(url, params=params, timeout=10)
    response.raise_for_status()

    data = response.json()

    if not data.get("results"):
        return None

    place = data["results"][0]

    return {
        "name": place["name"],
        "country": place.get("country", ""),
        "latitude": place["latitude"],
        "longitude": place["longitude"]
    }


def get_weather(latitude, longitude):
    url = "https://api.open-meteo.com/v1/forecast"

    params = {
        "latitude": latitude,
        "longitude": longitude,
        "current": (
            "temperature_2m,relative_humidity_2m,"
            "apparent_temperature,is_day,precipitation,"
            "weather_code,wind_speed_10m,surface_pressure"
        ),
        "daily": (
            "weather_code,temperature_2m_max,"
            "temperature_2m_min"
        ),
        "timezone": "auto",
        "forecast_days": 5
    }

    response = requests.get(url, params=params, timeout=10)
    response.raise_for_status()

    return response.json()


# ---------------- MAIN APPLICATION ----------------

class WeatherApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Weather Forecast App")
        self.root.geometry("650x760")
        self.root.minsize(520, 650)
        self.root.configure(bg="#101B35")

        self.setup_ui()

    def setup_ui(self):
        title = tk.Label(
            self.root,
            text="🌦 WEATHER FORECAST",
            font=("Arial", 23, "bold"),
            bg="#101B35",
            fg="white"
        )
        title.pack(pady=(25, 5))

        subtitle = tk.Label(
            self.root,
            text="Check live weather for any city",
            font=("Arial", 11),
            bg="#101B35",
            fg="#B8C7E0"
        )
        subtitle.pack(pady=(0, 20))

        search_frame = tk.Frame(self.root, bg="#101B35")
        search_frame.pack(padx=25, fill="x")

        self.city_entry = tk.Entry(
            search_frame,
            font=("Arial", 14),
            justify="center",
            relief="flat",
            bg="#FFFFFF",
            fg="#101B35"
        )
        self.city_entry.pack(
            side="left", fill="x", expand=True, ipady=12
        )
        self.city_entry.insert(0, "Bengaluru")
        self.city_entry.bind("<Return>", lambda event: self.search_weather())

        search_button = tk.Button(
            search_frame,
            text="Search",
            font=("Arial", 12, "bold"),
            bg="#4F8CFF",
            fg="white",
            activebackground="#3474E6",
            activeforeground="white",
            relief="flat",
            cursor="hand2",
            command=self.search_weather
        )
        search_button.pack(side="left", padx=(10, 0), ipady=8, ipadx=10)

        self.status_label = tk.Label(
            self.root,
            text="Enter a city to get started",
            font=("Arial", 10),
            bg="#101B35",
            fg="#B8C7E0"
        )
        self.status_label.pack(pady=12)

        self.result_frame = tk.Frame(
            self.root,
            bg="#1D2B4A",
            padx=20,
            pady=18
        )
        self.result_frame.pack(
            fill="both", expand=True, padx=25, pady=(0, 25)
        )

        self.city_label = tk.Label(
            self.result_frame,
            text="Welcome!",
            font=("Arial", 20, "bold"),
            bg="#1D2B4A",
            fg="white"
        )
        self.city_label.pack(pady=(0, 8))

        self.temperature_label = tk.Label(
            self.result_frame,
            text="-- °C",
            font=("Arial", 44, "bold"),
            bg="#1D2B4A",
            fg="#7CB4FF"
        )
        self.temperature_label.pack()

        self.condition_label = tk.Label(
            self.result_frame,
            text="Search for a city",
            font=("Arial", 14),
            bg="#1D2B4A",
            fg="#FFFFFF"
        )
        self.condition_label.pack(pady=8)

        self.feels_label = tk.Label(
            self.result_frame,
            text="Feels like: -- °C",
            font=("Arial", 11),
            bg="#1D2B4A",
            fg="#B8C7E0"
        )
        self.feels_label.pack(pady=(0, 15))

        self.details_label = tk.Label(
            self.result_frame,
            text="Humidity: --%\n"
                 "Wind Speed: -- km/h\n"
                 "Pressure: -- hPa\n"
                 "Precipitation: -- mm",
            font=("Arial", 12),
            justify="left",
            bg="#1D2B4A",
            fg="white",
            pady=10
        )
        self.details_label.pack()

        separator = tk.Frame(
            self.result_frame, height=1, bg="#425477"
        )
        separator.pack(fill="x", pady=12)

        tk.Label(
            self.result_frame,
            text="5-DAY FORECAST",
            font=("Arial", 13, "bold"),
            bg="#1D2B4A",
            fg="white"
        ).pack(pady=(0, 10))

        self.forecast_frame = tk.Frame(
            self.result_frame, bg="#1D2B4A"
        )
        self.forecast_frame.pack(fill="x")

        self.refresh_button = tk.Button(
            self.result_frame,
            text="↻ Refresh Weather",
            font=("Arial", 11, "bold"),
            bg="#263C62",
            fg="white",
            activebackground="#344E79",
            activeforeground="white",
            relief="flat",
            cursor="hand2",
            command=self.search_weather
        )
        self.refresh_button.pack(pady=(18, 0), ipadx=15, ipady=7)

        self.root.after(300, self.search_weather)

    def search_weather(self):
        city = self.city_entry.get().strip()

        if not city:
            messagebox.showwarning(
                "Missing City",
                "Please enter a city name."
            )
            return

        self.status_label.config(text="Loading weather data...")
        self.root.update_idletasks()

        try:
            place = get_city_coordinates(city)

            if place is None:
                self.status_label.config(text="City not found.")
                messagebox.showerror(
                    "City Not Found",
                    "Please check the city name and try again."
                )
                return

            data = get_weather(
                place["latitude"],
                place["longitude"]
            )

            self.display_weather(place, data)

            self.status_label.config(
                text="Last updated: " +
                datetime.now().strftime("%d %b %Y, %I:%M %p")
            )

        except requests.exceptions.Timeout:
            self.status_label.config(text="Request timed out.")
            messagebox.showerror(
                "Timeout",
                "The server took too long to respond. Try again."
            )

        except requests.exceptions.RequestException:
            self.status_label.config(text="Connection error.")
            messagebox.showerror(
                "Network Error",
                "Could not connect to the weather service. "
                "Check your internet connection."
            )

        except (KeyError, ValueError, IndexError):
            self.status_label.config(text="Invalid weather response.")
            messagebox.showerror(
                "Data Error",
                "Unable to process the weather data. Try again."
            )

    def display_weather(self, place, data):
        current = data["current"]
        daily = data["daily"]

        city_name = place["name"]
        country = place["country"]

        self.city_label.config(
            text=f"📍 {city_name}, {country}"
        )

        self.temperature_label.config(
            text=f"{current['temperature_2m']:.1f} °C"
        )

        code = current["weather_code"]
        condition = WEATHER_CODES.get(code, "Weather unavailable")

        if current["is_day"] == 0:
            condition += " 🌙"

        self.condition_label.config(text=condition)

        self.feels_label.config(
            text=f"Feels like: {current['apparent_temperature']} °C"
        )

        self.details_label.config(
            text=(
                f"💧 Humidity: {current['relative_humidity_2m']}%\n"
                f"💨 Wind Speed: {current['wind_speed_10m']} km/h\n"
                f"🌡 Pressure: {current['surface_pressure']} hPa\n"
                f"🌧 Precipitation: {current['precipitation']} mm"
            )
        )

        for widget in self.forecast_frame.winfo_children():
            widget.destroy()

        for index in range(len(daily["time"])):
            date = datetime.strptime(
                daily["time"][index], "%Y-%m-%d"
            )

            day_name = "Today" if index == 0 else date.strftime("%a")

            code = daily["weather_code"][index]
            description = WEATHER_CODES.get(code, "Unknown")

            card = tk.Frame(
                self.forecast_frame,
                bg="#263C62",
                padx=5,
                pady=10
            )
            card.pack(
                side="left", fill="both", expand=True, padx=3
            )

            tk.Label(
                card,
                text=day_name,
                font=("Arial", 10, "bold"),
                bg="#263C62",
                fg="white"
            ).pack()

            tk.Label(
                card,
                text=description.split(" ")[-1],
                font=("Arial", 19),
                bg="#263C62",
                fg="white"
            ).pack(pady=5)

            tk.Label(
                card,
                text=(
                    f"{daily['temperature_2m_max'][index]:.0f}°\n"
                    f"{daily['temperature_2m_min'][index]:.0f}°"
                ),
                font=("Arial", 10),
                bg="#263C62",
                fg="#D9E6FF"
            ).pack()


# ---------------- RUN APPLICATION ----------------

if __name__ == "__main__":
    root = tk.Tk()
    app = WeatherApp(root)
    root.mainloop()
