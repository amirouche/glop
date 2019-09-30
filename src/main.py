input = 'new york is the big apple'.split()


def spans(lst):
    if len(lst) == 0:
        yield None
    for index in range(1, len(lst)):
        for span in spans(lst[index:]):
            if span is not None:
                yield [lst[0:index]] + span
    yield [lst]

knowledgebase = [
    ['new', 'york'],
    ['big', 'apple'],
]

out = []
scores = []

for span in spans(input):
    score = 0
    for candidate in span:
        for uid, entity in enumerate(knowledgebase):
            if candidate == entity:
                score += 1
    out.append(span)
    scores.append(score)

leaderboard = sorted(zip(out, scores), key=lambda x: x[1])

for winner in leaderboard:
    print(winner[1], ' ~ ', winner[0])
