import pandas as pd
import xml.etree.ElementTree as ET

def excel_to_xml(excel_path, xml_path):
    df = pd.read_excel(excel_path)
    root = ET.Element("root")
    
    for _, row in df.iterrows():
        item = ET.SubElement(root, "item")
        for col in df.columns:
            child = ET.SubElement(item, col)
            child.text = str(row[col])
    
    tree = ET.ElementTree(root)
    
    tree.write(xml_path, encoding="utf-8", xml_declaration=True)

excel_path = 'demo_database.xlsx'
xml_path = 'output.xml'
excel_to_xml(excel_path, xml_path)
