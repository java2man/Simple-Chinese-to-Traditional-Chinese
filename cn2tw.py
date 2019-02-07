import xml.etree.ElementTree as ET
import zhconv
import sys
import os

tree = ET.ElementTree(file='ChainBow.xliff')

root = tree.getroot()

print(root.tag, root.attrib)

for single_file in root:

	for single_body in single_file:

		for single_trans in single_body:

			source_text = ''

			for single_item in single_trans:

				if single_item.tag == 'source':
					source_text = single_item.text

				if single_item.tag == 'target':
					single_item.text = zhconv.convert(source_text, "zh-tw")

				print(single_item.text)

tree.write('ChainBow_tw.xliff', encoding='UTF-8')