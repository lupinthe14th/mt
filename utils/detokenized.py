import io
import sys

sys.stdin = io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8')
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

for l in sys.stdin:
    pieces = ''.join(l.split())
    detokenized = ''.join(pieces).replace('\u2581', '\u0020')
    print(detokenized.strip())
