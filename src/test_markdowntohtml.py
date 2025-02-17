import unittest
from markdowntohtml import markdown_to_html

class markdown_to_html_test(unittest.TestCase):
    def test(self):
        test = "### here is a header"
        test2 = "and *a* **paragraph** `with` a ![link](https://to.an/image.png)"
        test3 = "- and\n - an\n- unorganised\n- list"
        test4 = "* and\n * an\n* unorganised\n* list"
        test5 = "1. and\n2. an\n3. organised\n4. list"
        test6 = "```and some code```"
        test7 = ">>> this is a quote thats\n>>> over 2 lines"


        self.assertEqual(markdown_to_html(test), "<div><h3>here is a header</h3></div>")
        self.assertEqual(markdown_to_html(test2), "<div><p>and <i>a</i> <b>paragraph</b> <code>with</code> a <img src='https://to.an/image.png' alt='link'></img></p></div>")      
        self.assertEqual(markdown_to_html(test3), "<div><ul><li>and</li><li>an</li><li>unorganised</li><li>list</li></ul></div>")
        self.assertEqual(markdown_to_html(test4), "<div><ul><li>and</li><li>an</li><li>unorganised</li><li>list</li></ul></div>")
        self.assertEqual(markdown_to_html(test5), "<div><ol><li>1. and</li><li>2. an</li><li>3. organised</li><li>4. list</li></ol></div>")
        self.assertEqual(markdown_to_html(test6), "<div><pre><code>and some code</code></pre></div>")
        self.assertEqual(markdown_to_html(test7), "<div><blockquote>this is a quote thats\nover 2 lines</blockquote></div>") 
        self.assertEqual(markdown_to_html(f"{test}\n\n{test2}"), "<div><h3>here is a header</h3><p>and <i>a</i> <b>paragraph</b> <code>with</code> a <img src='https://to.an/image.png' alt='link'></img></p></div>")
        self.assertEqual(markdown_to_html(f"{test}\n\n{test2}\n\n{test3}"), "<div><h3>here is a header</h3><p>and <i>a</i> <b>paragraph</b> <code>with</code> a <img src='https://to.an/image.png' alt='link'></img></p><ul><li>and</li><li>an</li><li>unorganised</li><li>list</li></ul></div>")
        self.assertEqual(markdown_to_html(f"{test}\n\n{test3}\n\n{test4}"), "<div><h3>here is a header</h3><ul><li>and</li><li>an</li><li>unorganised</li><li>list</li></ul><ul><li>and</li><li>an</li><li>unorganised</li><li>list</li></ul></div>")
        self.assertEqual(markdown_to_html(f"{test4}\n\n{test5}\n\n{test6}"), "<div><ul><li>and</li><li>an</li><li>unorganised</li><li>list</li></ul><ol><li>1. and</li><li>2. an</li><li>3. organised</li><li>4. list</li></ol><pre><code>and some code</code></pre></div>")
        self.assertEqual(markdown_to_html(f"{test5}\n\n{test6}\n\n{test7}"), "<div><ol><li>1. and</li><li>2. an</li><li>3. organised</li><li>4. list</li></ol><pre><code>and some code</code></pre><blockquote>this is a quote thats\nover 2 lines</blockquote></div>")

if __name__ == "__main__":
    unittest.main()