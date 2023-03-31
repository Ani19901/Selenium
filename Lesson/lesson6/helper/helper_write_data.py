import logging


class WriteData:

    def get_logging(self):
        logging.basicConfig(filename="log.file.alert",
                                           level=logging.INFO,
                                           format="%(asctime)s - %(levelname)s - %(message)s",
                                           datefmt='%Y-%m-%d %H:%M:%S',
                                           filemode='w')
        return logging


    def write_data_in_txt_file(self, element_list):
        out_file = "alert_text.txt"
        with open(out_file, "w") as f:
            for i in element_list:
                f.writelines(str(i) + '\n')
