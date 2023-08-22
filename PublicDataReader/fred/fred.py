"""
FRED API
- https://fred.stlouisfed.org/docs/api/fred/
"""
import requests
import pandas as pd

requests.packages.urllib3.disable_warnings()

class Fred:
    
    def __init__(self, api_key=None):
        self.api_key = api_key
        self.meta_data = {
            
            # Categories
            "category": "https://api.stlouisfed.org/fred/category",
            "category_children": "https://api.stlouisfed.org/fred/category/children",
            "category_related": "https://api.stlouisfed.org/fred/category/related",
            "category_series": "https://api.stlouisfed.org/fred/category/series",
            "category_tags": "https://api.stlouisfed.org/fred/category/tags",
            "category_related_tags": "https://api.stlouisfed.org/fred/category/related_tags",
            
            # Releases
            "releases": "https://api.stlouisfed.org/fred/releases",
            "releases_dates": "https://api.stlouisfed.org/fred/releases/dates",
            "release": "https://api.stlouisfed.org/fred/release",
            "release_dates": "https://api.stlouisfed.org/fred/release/dates",
            "release_series": "https://api.stlouisfed.org/fred/release/series",
            "release_sources": "https://api.stlouisfed.org/fred/release/sources",
            "release_tags": "https://api.stlouisfed.org/fred/release/tags",
            "release_related_tags": "https://api.stlouisfed.org/fred/release/related_tags",
            "release_tables": "https://api.stlouisfed.org/fred/release/tables",
            
            # Series
            "series": "https://api.stlouisfed.org/fred/series",
            "series_categories": "https://api.stlouisfed.org/fred/series/categories",
            "series_observations": "https://api.stlouisfed.org/fred/series/observations",
            "series_release": "https://api.stlouisfed.org/fred/series/release",
            "series_search": "https://api.stlouisfed.org/fred/series/search",
            "series_search_tags": "https://api.stlouisfed.org/fred/series/search/tags",
            "series_search_related_tags": "https://api.stlouisfed.org/fred/series/search/related_tags",
            "series_tags": "https://api.stlouisfed.org/fred/series/tags",
            "series_updates": "https://api.stlouisfed.org/fred/series/updates",
            "series_vintagedates": "https://api.stlouisfed.org/fred/series/vintagedates",
            
            # Sources
            "sources": "https://api.stlouisfed.org/fred/sources",
            "source": "https://api.stlouisfed.org/fred/source",
            "source_releases": "https://api.stlouisfed.org/fred/source/releases",
            
            # Tags
            "tags": "https://api.stlouisfed.org/fred/tags",
            "related_tags": "https://api.stlouisfed.org/fred/related_tags",
            "tags_series": "https://api.stlouisfed.org/fred/tags/series",
            
            # Maps API
            "maps_shape_files": "https://api.stlouisfed.org/geofred/shapes/file",
            "maps_series_group_meta": "https://api.stlouisfed.org/geofred/series/group",
            "maps_series_regional_data": "https://api.stlouisfed.org/geofred/series/data",
            "regional_data": "https://api.stlouisfed.org/geofred/regional/data",
            
        }
        
    def get_data(self, api_name, **kwargs):
        url = self.meta_data[api_name]
        params = {
            "api_key": self.api_key,
            "file_type": "json",
        }
        params.update(kwargs)
        res = requests.get(url, params=params, verify=False)
        data = res.json()

        key_list = [
            'categories', 'seriess', 'tags', 'releases',
            'release_dates', 'sources', 'elements', 'observations', 'vintage_dates'
        ]
        for key in key_list:
            if key in data:
                if key != 'elements':
                    return pd.DataFrame(data[key])
                else:
                    return pd.DataFrame(data[key]).T
        return data