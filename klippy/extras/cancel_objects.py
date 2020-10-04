import os, logging


class CancelObjects:
    def __init__(self, config):

        printer = config.get_printer()
        printer.register_event_handler("klippy:file_line_read",
            self.file_line_read)
        printer.register_event_handler("klippy:process_command_line",
            self.process_command_line)

    def file_line_read(self, line):
        pass

    def process_command_line(self, line):
        pass

def load_config(config):
    return CancelObjects(config)