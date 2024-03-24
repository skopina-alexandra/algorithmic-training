
n = int(input())

set_common = set()

set_prev = set()

for i in range(n):
    k = int(input())
    tracks = list(input().split())

    if not set_prev:
        for track in tracks:
            set_common.add(track)
    else:
        for track in tracks:
            if track in set_prev:
                set_common.add(track)

    set_prev = set_common
    set_common = set()

print(len(set_prev))

print(' '.join(sorted(set_prev)))