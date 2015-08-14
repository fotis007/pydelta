import delta as d
import os
from nose.tools import eq_

testdir = None


def setup_module():
    global testdir
    testdir = os.path.join(
        os.path.dirname(
            os.path.abspath(__file__)),
        'corpus3')


class FeatureGenerator_Test:

    def setup(self):
        self.gen = d.FeatureGenerator()

    def test_tokenize(self):
        assert list(self.gen.tokenize(["This is a", "simple test"])) \
            == ["This", "is", "a", "simple", "test"]

    def test_count_tokens(self):
        result = self.gen.count_tokens(
            ["this is a test", "testing this generator"])
        assert result["this"] == 2
        assert result["generator"] == 1
        assert result.sum() == 7

    def test_get_name(self):
        assert self.gen.get_name('foo/bar.baz.txt') == 'bar.baz'

    def test_call(self):
        df = self.gen(testdir)
        eq_(df.und.sum(), 25738.0)

class Corpus_Test:

    def parse_test(self):
        corpus = d.Corpus(testdir)
        eq_(corpus.und.sum(), 25738.0)
