# Import the xml.etree.ElementTree module
import xml.etree.ElementTree as ET

# Parse the XML file and get the ElementTree object
tree = ET.parse('country_data.xml')

# Get the root element of the tree
root = tree.getroot()

# Print the tag and attributes of the root element
print(root.tag, root.attrib)

# Iterate over the child elements of the root element
for country in root:
    # Print the name attribute and the text of the rank element for each country
    print(country.attrib['name'], country.find('rank').text)
