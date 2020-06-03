from rx import from_, operators as ops
import re

# Todo suffering from group_by -> flatmap issue

def words_from_file(file_name):
    file = open(file_name)

    # parse, clean, and push words in text file
    return from_(file).pipe(
        ops.flat_map(lambda s: from_(s.split())),
        ops.map(lambda w: re.sub(r'[^\w\s]', '', w)),
        ops.filter(lambda w: w != ""),
        ops.map(lambda w: w.lower())
    )


def word_counter(file_name):

    # count words using `group_by()`
    # tuple the word with the count
    return words_from_file(file_name).pipe(
        ops.group_by(lambda word: word),
        ops.flat_map(lambda grp: grp.count().map(lambda ct: (grp.key, ct)))
    )

article_file = "../resources/bbc_news_article.txt"
word_counter(article_file).subscribe(lambda w: print(w))
