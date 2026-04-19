import pandas as pd
import os

def get_crop_details(crop):
    info = {
        'rice': {'season': 'Kharif/Rabi', 'water': 'High', 'soil': 'Clay loam', 'days': '90-150'},
        'wheat': {'season': 'Rabi', 'water': 'Medium', 'soil': 'Loamy', 'days': '110-130'},
        'maize': {'season': 'Kharif', 'water': 'Medium', 'soil': 'Well-drained', 'days': '80-100'},
        'cotton': {'season': 'Kharif', 'water': 'High', 'soil': 'Black', 'days': '150-180'},
        'sugarcane': {'season': 'Year-round', 'water': 'High', 'soil': 'Deep loamy', 'days': '12-18m'},
        'groundnut': {'season': 'Kharif', 'water': 'Medium', 'soil': 'Sandy loam', 'days': '90-120'}
    }
    return info.get(crop.lower(), {'season': 'Varies', 'water': 'Medium', 'soil': 'Loamy', 'days': '90-120'})

