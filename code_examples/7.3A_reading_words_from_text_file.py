from rx import from_, operators as ops
import re


def words_from_file(file_name):
    file = open(file_name)

    # parse, clean, and push words in text file
    return from_(file).pipe(
        ops.flat_map(lambda s: from_(s.split())),
        ops.map(lambda w: re.sub(r'[^\w]', '', w)),
        ops.filter(lambda w: w != ""),
        ops.map(lambda w: w.lower())
    )

article_file = "../resources/bbc_news_article.txt"
words_from_file(article_file).subscribe(lambda w: print(w))
