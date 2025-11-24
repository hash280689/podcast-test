import yaml
import xml.etree.ElementTree as  xml_tree

#Open the feed.yaml file and read it into a var called "yaml_data"
with open ('feed.yaml', 'r') as file:
    yaml_data = yaml.safe_load(file)

#Writing the RSS Feed

#Add element of time RSS
rss_element = xml_tree.Element('rss', {'version':'2.0', 'xmlns:itunes':'http://www.itunes.com/dtds/podcast-1.0.dtd', 'xmlns:content':'http://purl.org/rss/1.0/modules/content'})

#Create sub element inside the XML treee

channel_element = xml_tree.SubElement(rss_element, 'channel')

#Create a "Title" element inside the channel element sub tree and then retrieve the actual title from the feed
xml_tree.SubElement(channel_element, 'title').text = yaml_data['title']

#Create a variable to store the output
output_tree = xml_tree.ElementTree(rss_element)

#write output tree to a file
#The encoding and declaration params generate the tag <?xml version="1.0" encoding="UTF-8"?>
output_tree.write('podcast.xml', encoding='UTF-8', xml_declaration=True)