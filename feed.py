import yaml
import xml.etree.ElementTree as  xml_tree

#Open the feed.yaml file and read it into a var called "yaml_data"
with open ('feed.yaml', 'r') as file:
    yaml_data = yaml.safe_load(file)

    #Add element of time RSS
    rss_element = xml_tree.Element('rss', {
        'version':'2.0', 
        'xmlns:itunes':'http://www.itunes.com/dtds/podcast-1.0.dtd', 
        'xmlns:content':'http://purl.org/rss/1.0/modules/content/'
    })

#Create sub element inside the XML treee
channel_element = xml_tree.SubElement(rss_element, 'channel')

#Create the link prefix (My github page)
link_prefix = yaml_data['link']

#Create a "Title" element inside the channel element sub tree and then retrieve the actual title from the feed
xml_tree.SubElement(channel_element, 'title').text = yaml_data['title']

#Do this with all of the other elements
#Note that some of the elements need the "itunes:" prefix
xml_tree.SubElement(channel_element, 'format').text = yaml_data['format']
xml_tree.SubElement(channel_element, 'subtitle').text = yaml_data['subtitle']
xml_tree.SubElement(channel_element, 'itunes:author').text = yaml_data['author']
xml_tree.SubElement(channel_element, 'description').text = yaml_data['description']

#image is referenced with href so it needs the prefix. Concat them together
xml_tree.SubElement(channel_element, 'itunes:image', {'href': link_prefix + yaml_data['image']})

xml_tree.SubElement(channel_element, 'language').text = yaml_data['language']
xml_tree.SubElement(channel_element, 'link').text = link_prefix

#Creating a sub category tag which is stored in attributes
xml_tree.SubElement(channel_element, 'itunes:category', {'text': yaml_data['category']})

#Loop through all of the podcast episodes stored in 'item' tags
for item in yaml_data['item']:
    item_element = xml_tree.SubElement(channel_element, 'item')
    xml_tree.SubElement(item_element, 'title'). text = item['title']
    
    #Add the Author tag for each item but just get it from the yaml_data rather than having to add it for each item
    xml_tree.SubElement(item_element, 'itunes:author'). text = yaml_data['author']
    
    xml_tree.SubElement(item_element, 'description'). text = item['description']
    xml_tree.SubElement(item_element, 'itunes:duration'). text = item['duration']
    xml_tree.SubElement(item_element, 'pubdate'). text = item['published']

    #Create enclosure tag. This contains the length of episode in bytes, the audio file and url
    enclosure = xml_tree.SubElement(item_element, 'enclosure', {
        'url': link_prefix + item['file'],
        'type': 'audio/mpeg',
        'length': item['length']
    })



#Create a variable to store the output
output_tree = xml_tree.ElementTree(rss_element)

#write output tree to a file
#The encoding and declaration params generate the tag <?xml version="1.0" encoding="UTF-8"?>
output_tree.write('podcast.xml', encoding='UTF-8', xml_declaration=True)