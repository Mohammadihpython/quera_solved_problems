from bs4 import BeautifulSoup, Comment


class HTMLTools:

    @staticmethod
    def refactor_data(**values):
        data = {**values}
        tags = ["class", "id", "name", "string"]
        for key in data:
            if key not in tags:
                raise Exception("No Such Tag")
        # if "class" in data:
        #     data['class_'] = data.pop('class')
        return data

    @staticmethod
    def result_by_output_arg(result, output_arg):
        if result is None:
            return ''
        if output_arg == "name":
            return result.name
        elif output_arg == "string":
            return result.get_text()
        else:
            return result.get(output_arg)


class HTMLParser:
    def __init__(self, html_doc):
        self.html_doc = html_doc
        self.soup = BeautifulSoup(html_doc, 'html.parser')

    def set_html_doc(self, html_doc):
        self.html_doc = html_doc

    def find_first(self, output_arg: str, **finding_args: dict):
        data = HTMLTools.refactor_data(**finding_args)
        result = self.soup.find(**data)
        return HTMLTools.result_by_output_arg(result, output_arg)

    def find_all(self, n: int, output_arg: str, **finding_args):
        data = HTMLTools.refactor_data(**finding_args)
        results = self.soup.find_all(**data, limit=n, )
        return [HTMLTools.result_by_output_arg(result, output_arg) for result in results]

    def find_parent(self, output_arg, **finding_args):
        data = HTMLTools.refactor_data(**finding_args)
        result = self.soup.find(**data)
        if result is not None:
            parent = result.parent
            if parent is not None:
                return HTMLTools.result_by_output_arg(parent, output_arg)
        return None

    def find_grandparent(self, n, output_arg, **finding_args):
        data = HTMLTools.refactor_data(**finding_args)
        result = self.soup.find(**data)
        if result is not None:
            grandparent = result
            for _ in range(n):
                grandparent = grandparent.parent
                if grandparent is None:
                    raise Exception("No Such Parent")
            return HTMLTools.result_by_output_arg(grandparent, output_arg)
        return None

    def remove_comment(self, **finding_args):
        comments = self.soup.find_all(text=lambda text: isinstance(text, Comment))
        for comment in comments:
            data = HTMLTools.refactor_data(**finding_args)
            if comment.find(**data) is not None:
                comment.extract()

    def remove_all_comments(self):
        comments = self.soup.find_all(text=lambda text: isinstance(text, Comment))
        for comment in comments:
            comment.extract()

    def remove_tag(self, **finding_args):
        data = HTMLTools.refactor_data(**finding_args)
        for tag in self.soup.find_all(**data):
            tag.extract()
