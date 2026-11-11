"""Validate shared topic IDs and post metadata without third-party packages."""
import argparse
import json
from pathlib import Path
import re


def validate(root):
    topics=json.loads((root/'_data/topics.json').read_text())
    ids=[topic['id'] for topic in topics]
    errors=[]
    if len(ids)!=len(set(ids)) or 'all' in ids:errors.append('Topic IDs must be unique; all is reserved')
    for topic in topics:
        if not re.fullmatch(r'[a-z][a-z-]*',topic['id']):errors.append(f'Invalid topic ID: {topic["id"]}')
        for key in ['title','icon','description','back_label']:
            if not isinstance(topic.get(key),str) or not topic[key].strip():errors.append(f'{topic["id"]}: missing {key}')
    posts=list((root/'_posts').glob('*.md'))
    if not posts:errors.append('No posts found')
    for path in posts:
        parts=path.read_text().split('---',2)
        if len(parts)!=3 or parts[0].strip():
            errors.append(f'{path.name}: missing front matter');continue
        front=parts[1]
        if re.search(r'^(?:chips|track|track_icon):',front,re.M):
            errors.append(f'{path.name}: use topics only; labels/icons come from _data/topics.json')
        matches=re.findall(r'^topics:\s*\[([^]\n]*)\]\s*$',front,re.M)
        if len(matches)!=1:
            errors.append(f'{path.name}: use one inline list, e.g. topics: [ner, pii]');continue
        selected=[part.strip().strip('"\'') for part in matches[0].split(',')]
        if len(selected)!=len(set(selected)) or not all(selected):errors.append(f'{path.name}: empty or duplicate topics')
        unknown=set(selected)-set(ids)
        if unknown:errors.append(f'{path.name}: unknown topics: {sorted(unknown)}')
    return errors,len(posts),len(topics)


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root',type=Path,default=Path(__file__).resolve().parents[1])
    args=parser.parse_args()
    errors,posts,topics=validate(args.root)
    if errors:raise SystemExit('\n'.join(errors))
    print(f'Topic metadata OK: {posts} posts, {topics} filterable categories')


if __name__=='__main__':main()
