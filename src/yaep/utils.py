
class SectionHeader(object):
    header = 'dummy'

    def __init__(self, fp):
        self.fp = fp
        self.sent_header = False

    def readline(self):
        if not self.sent_header:
            self.sent_header = True
            read_data = '[{}]\n'.format(self.header)
        else:
            read_data = self.fp.readline()

        return read_data
