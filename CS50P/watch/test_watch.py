import watch
def main():
    test_parse()
def test_parse():
    watch.parse(r"""<iframe width="560" height="315" src="https://www.youtube.com/embed/xvFZjo5PgG0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>""")
if __name__ == "__main__":
    main()
