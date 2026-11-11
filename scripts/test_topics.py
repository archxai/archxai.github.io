"""Topic validation regressions; runs with Python's standard library only."""
import json
from pathlib import Path
import re
import tempfile
import unittest

from check_topics import validate

ROOT=Path(__file__).resolve().parents[1]


class TopicsTest(unittest.TestCase):
    def test_all_published_post_topics_are_filterable(self):
        errors,posts,topics=validate(ROOT)
        self.assertEqual(errors,[])
        self.assertGreater(posts,0)
        self.assertEqual(topics,6)

    def test_requested_latest_post_labels(self):
        expected={
            '2026-11-11-estonian-ner-ria-follow-up.md':['ner'],
            '2026-10-22-texplorer-local-machine-learning-in-the-browser.md':['ner','pii'],
            '2026-07-20-summarisation-model-development-update.md':['summarisation'],
        }
        for name,topics in expected.items():
            front=(ROOT/'_posts'/name).read_text().split('---',2)[1]
            selected=[part.strip() for part in re.search(r'^topics: \[([^]]+)\]',front,re.M)[1].split(',')]
            self.assertEqual(selected,topics)
        catalog=json.loads((ROOT/'_data/topics.json').read_text())
        self.assertEqual(next(t['icon'] for t in catalog if t['id']=='summarisation'),'🗜️')

    def check_fixture(self,metadata,catalog=None):
        with tempfile.TemporaryDirectory(prefix='blog-topics-test-') as directory:
            root=Path(directory)
            (root/'_data').mkdir();(root/'_posts').mkdir()
            catalog=catalog or [{'id':'ner','title':'NER','icon':'📇','description':'NER posts','back_label':'NER posts'}]
            (root/'_data/topics.json').write_text(json.dumps(catalog))
            (root/'_posts/post.md').write_text('---\ntitle: Example\n'+metadata+'\n---\nUnchanged body.')
            return validate(root)[0]

    def test_unknown_topics_rejected(self):
        self.assertTrue(any('unknown topics' in e for e in self.check_fixture('topics: [ner, random-label]')))

    def test_separate_display_chips_rejected(self):
        self.assertTrue(any('use topics only' in e for e in self.check_fixture('topics: [ner]\nchips:\n  - label: Preliminary')))

    def test_empty_duplicate_or_missing_topics_rejected(self):
        for metadata in ['topics: []','topics: [ner, ner]','summary: No topics']:
            self.assertTrue(self.check_fixture(metadata),metadata)

    def test_valid_metadata_accepted(self):
        self.assertEqual(self.check_fixture('topics: [ner]'),[])


if __name__=='__main__':unittest.main()
