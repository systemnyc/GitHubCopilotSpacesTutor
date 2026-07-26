#!/usr/bin/env python3
"""
Weather Report Generator

A simple application that reads weather data from a JSON file
and generates a formatted weather report for a specified city.

Usage:
    python main.py "City Name"

Example:
    python main.py "New York"

Output:
    Weather Report for New York
    ================================
    Temperature: 72°F
    Condition: Partly Cloudy
    Humidity: 65%
    Wind Speed: 8 mph
"""

import json
import sys
from pathlib import Path


def load_weather_data(filename="sample_weather.json"):
    """
    Load weather data from a JSON file.
    
    Args:
        filename (str): Path to the JSON file containing weather data.
                       Defaults to sample_weather.json in the same directory.
    
    Returns:
        dict: Weather data with city names as keys.
    
    Raises:
        FileNotFoundError: If the JSON file does not exist.
        json.JSONDecodeError: If the JSON file is malformed.
    """
    file_path = Path(__file__).parent / filename
    
    if not file_path.exists():
        raise FileNotFoundError(f"Weather data file not found: {file_path}")
    
    with open(file_path, 'r') as f:
        data = json.load(f)
    
    return data


def get_city_weather(city_name, weather_data):
    """
    Retrieve weather data for a specific city.
    
    Args:
        city_name (str): The name of the city to look up.
        weather_data (dict): The weather data dictionary.
    
    Returns:
        dict: Weather information for the city, or None if not found.
    """
    return weather_data.get(city_name)


def format_weather_report(city_name, weather_info):
    """
    Format weather information into a readable report.
    
    Args:
        city_name (str): The name of the city.
        weather_info (dict): Weather data containing temperature, condition, humidity, wind_speed.
    
    Returns:
        str: A formatted weather report.
    """
    report = f"""Weather Report for {city_name}
================================
Temperature: {weather_info['temperature']}°F
Condition: {weather_info['condition']}
Humidity: {weather_info['humidity']}%
Wind Speed: {weather_info['wind_speed']} mph
"""
    return report


def main(city_name):
    """
    Main function to generate and display a weather report.
    
    Args:
        city_name (str): The name of the city to get weather for.
    
    Returns:
        int: 0 on success, 1 on error.
    """
    try:
        weather_data = load_weather_data()
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Error loading weather data: {e}", file=sys.stderr)
        return 1
    
    weather_info = get_city_weather(city_name, weather_data)
    
    if weather_info is None:
        print(f"Error: City '{city_name}' not found in weather data.", file=sys.stderr)
        print(f"Available cities: {', '.join(weather_data.keys())}", file=sys.stderr)
        return 1
    
    report = format_weather_report(city_name, weather_info)
    print(report)
    return 0


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python main.py \"City Name\"")
        print("Example: python main.py \"New York\"")
        sys.exit(1)
    
    city = sys.argv[1]
    exit_code = main(city)
    sys.exit(exit_code)
