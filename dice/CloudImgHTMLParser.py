from html.parser import HTMLParser


class CloudHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        self.data = attrs[1][1]

    def handle_endtag(self, tag):
        pass

    def handle_data(self, data):
        pass


def parse_html_get_src(html_string):
    parser = CloudHTMLParser()
    parser.feed(html_string)
    return parser.data
