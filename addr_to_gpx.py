import geopy
from geopy.geocoders import Nominatim
import xml.etree.ElementTree as ET
from xml.dom import minidom

def geocode_addresses_to_gpx(addresses, output_file='locations.gpx'):
    # Initialize the Nominatim Geocoder
    geolocator = Nominatim(user_agent="address_converter")

    # Create the root element for GPX
    gpx = ET.Element('gpx', version="1.1", creator="JSON to GPX Converter")

    # Geocode addresses
    for address in addresses:
        try:
            location = geolocator.geocode(address)
            if location:
                wpt = ET.SubElement(gpx, 'wpt', lat=str(location.latitude), lon=str(location.longitude))
                name = ET.SubElement(wpt, 'name')
                name.text = address
            else:
                print(f"No coordinates found for: {address}")
        except Exception as e:
            print(f"Error with address {address}: {e}")

    # Convert the XML to a pretty string
    xmlstr = minidom.parseString(ET.tostring(gpx, 'utf-8')).toprettyxml(indent="  ")

    # Write the GPX data to a file
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(xmlstr)

    print(f"GPX file saved as {output_file}")

# Example addresses
example_addresses = [
    "Brandenburger Tor, Berlin",
    "Marienplatz 1, München",
    "Rathaus, Hamburg"
]

# Convert addresses to GPX and save to a file
geocode_addresses_to_gpx(example_addresses)