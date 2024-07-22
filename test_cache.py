import os
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'celeryproj.settings')  # Use your actual project name
django.setup()

from django.core.cache import cache

def test_cache():
    # Set a value in the cache
    cache.set('test_key', 'test_value', timeout=60)
    
    # Get the value from the cache
    value = cache.get('test_key')
    
    # Print the value to verify it's correctly cached
    print(f"Value from cache: {value}")

if __name__ == "__main__":
    test_cache()
