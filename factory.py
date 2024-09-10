from abc import ABC, abstractmethod
import json
import xml.etree.ElementTree as ET


class EditorBase(ABC):
    @abstractmethod
    def editor(self):
        pass


class XmlEditor(EditorBase):
    def __init__(self, file):
        self.file = file

    def editor(self):
        f = ET.parse(self.file)
        root = f.getroot()

        while True:
            tag_name = input('Enter the tag name: ')
            new_tag = ET.SubElement(root, tag_name)
            new_tag.text = input("Enter the tag text:\n")
            attrs = input('Enter the tag attributes:\n')
            for i in attrs.split():
                new_tag.attrib[i] = input(f"Enter the {i} attr value: ")
            flag = input("Do you want to continue? (y/n): ")
            if flag == 'n':
                f.write(self.file)
                break


class JsonEditor(EditorBase):
    def __init__(self, file):
        self.file = file

    def editor(self):
        # in this part app will get data which already saved on json file
        with open(self.file, 'r+') as file:
            file_context = file.read()
            if file_context:
                data = json.loads(file_context)
            else:
                data = {}

        # in next line reopening file with w mode is for overwriting last data
        with open(self.file, 'w+') as file:
            while True:
                key = input('Enter key to add/modify: ')
                value = input(f'Enter value of {key}: ')
                data[key] = value
                flag = input('Do you want to continue? (y/n): ')
                if flag == 'n':
                    new_context = json.dumps(data, indent=4)
                    file.write(new_context)
                    break


class Handler:
    @staticmethod
    def select_editor():
        file = input('Enter file name: ')
        file_type = file.split('.')[1]
        if file_type == 'json':
            return JsonEditor(file)
        elif file_type == 'xml':
            return XmlEditor(file)
        else:
            raise ValueError(f'editor type {file_type} is not supported')
