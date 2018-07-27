class CsvConfigParser:
    def __init__(self, filepath):
        self.result_dict = {}  # result_dict to be returned
        self.file_path = filepath
        self.csv_config_reader()

    def csv_config_reader(self):
        """
        Read the CSV config file and return a dictionary with configuration sections as keys

        :return: Dictionary of dictionaries of section(s) which contain Configuration Key-Value pairs
        """
        with open(self.file_path) as f:
            contents = f.readlines()
            contents2 = [x.strip() for x in contents if (x[0] != ";" and x[0] != "#")]    # remove comments
            contents2 = filter(None, contents2)                                           # remove empty rows
            for x in contents2:
                lst = x.split(",")
                header = lst.pop(0)
                while len(lst) > 0:
                    l = lst[0]
                    # print(header, l)
                    if "=" in l:
                        pair = l.split("=")
                        if header not in self.result_dict:
                            self.result_dict[header] = {}
                        self.result_dict[header][pair[0].strip()] = pair[1].strip()
                        key = pair[0].strip()
                        val = pair[1].strip()
                    lst.pop(0)
        return 0

    def get_config(self, section, key):
        """
        Provide section and key to get corresponding value from the config-file

        :param section: the header(first element in CSV row)
        :param key: a key from the section
        :return: value of the key in section
        """
        return self.result_dict[section][key]

    def sections(self):
        """
        Return all sections

        :return: list of all section/headers in config-file
        """
        return list(self.result_dict.keys())

    def keys(self, section):
        """
        Returns the list of keys in the section

        :param section:
        :return:
        """
        return list(self.result_dict[section])


if __name__ == '__main__':
    # Call CsvConfigParser by passing config file path as arguement 
    parser = CsvConfigParser("sample.ini")

    section='test2'
    key='key_10'

    # parser.get_config(<section_name>, <key>) gives the value for the key in the section
    print("Value in {section} section for key {key} is {value}".format(section=section, key=key, value=parser.get_config(section, key)))

    # parser.sections() returns list of all sections
    print("List of headers/sections in the config file: {sections}".format(sections=parser.sections()))

    # parser.keys(<section_name>) gives a list of all keys in that section
    print("List of all keys in {section} section :".format(section=parser.keys(section)))

