import io
import ConfigParser
from unittest import TestCase
from yaep.utils import SectionHeader


class TestSectionHeader(TestCase):
    def setUp(self):
        self.fp = io.BytesIO('foo = bar\nbaz = biz')
        self.expected = [('foo', 'bar'), ('baz', 'biz')]

    def test_needed(self):
        cp = ConfigParser.SafeConfigParser()
        self.assertRaises(
            ConfigParser.MissingSectionHeaderError,
            cp.readfp,
            self.fp
        )

    def test_header(self):
        cp = ConfigParser.SafeConfigParser()
        cp.readfp(SectionHeader(self.fp))

        assert(self.expected == cp.items(SectionHeader.header))
