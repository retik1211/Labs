from lxml import etree

def validate_xml(xml_file, xsd_file):
    try:
        # Загрузка XML и XSD
        with open(xml_file, 'r') as xml:
            xml_content = xml.read()
        with open(xsd_file, 'r') as xsd:
            xsd_content = xsd.read()

        # Парсинг XML и XSD
        xml_doc = etree.XML(xml_content)
        xsd_doc = etree.XMLSchema(etree.XML(xsd_content))

        # Валидация
        if xsd_doc.validate(xml_doc):
            print("XML-документ валиден.")
        else:
            print("XML-документ не валиден.")
            print(xsd_doc.error_log)
    except Exception as e:
        print(f"Ошибка: {e}")

# Вызов функции
validate_xml('library.xml', 'library.xsd')