class CsvConfigParser:
    def __init__(self, filepath):
        self.result_dict = {}  # result_dict to be returned
        self.file_path = filepath
        self.csv_config_reader()

    def csv_config_reader(self):
        """
        Read the CSV config file and return a dictionary with configuration sections as keys

        :return: dictionaries of section(s) which contain Configuration Key-Value pairs
        """
        print("CSV config parser started.")
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
        print(self.result_dict)
        return 0

    def get_config(self, section, key):
        """
        Provide section name to get key value pairs in section

        :param section:
        :param key:
        :return:
        """
        return self.result_dict[section][key]

    def sections(self):
        """
        Return all sections
        :return:
        """
        return list(self.result_dict.keys())

"""Test """
if __name__ == '__main__':
    parser = CsvConfigParser("sample_config.csv")
    print(parser.get_config("test1", "column1"))
    print(parser.sections())
