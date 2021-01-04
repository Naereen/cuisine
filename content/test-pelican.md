Title: Test de Pelican
Category: Test
Tags: test
Summary: Complete test of Pelican (in English).

[TOC]

Complete test of Pelican (in English).

----

# An exhibit of Markdown

This note demonstrates some of what [Markdown][1] is capable of doing.

*Note: Feel free to play with this page. Unlike regular notes, this doesn't automatically save itself.*

## Basic formatting

Paragraphs can be written like so. A paragraph is the basic block of Markdown. A paragraph is what text will turn into when there is no reason it should become anything else.

Paragraphs must be separated by a blank line. Basic formatting of *italics* and **bold** is supported. This *can be **nested** like* so.

## Lists

### Ordered list

1. Item 1
2. A second item
3. Number 3
4. Ⅳ

*Note: the fourth item uses the Unicode character for [Roman numeral four][2].*

### Unordered list

* An item
* Another item
* Yet another item
* And there's more...

## Paragraph modifiers

### Code block

    Code blocks are very useful for developers and other people who look at code or other things that are written in plain text. As you can see, it uses a fixed-width font.

You can also make `inline code` to add code into other things.

### Python code block

```python
def awesome(name):
    return name == 'me'
```

### OCaml code block

```ocaml
let awesome (name : str) : bool =
    name = "me"
;;
```

### GNU Bash code block

```bash
function awesome() {
    if [[ X${1} = X"me" ]]; then
        echo "yes"
    else
        echo "no"
    fi
}
```

### Quote

> Here is a quote. What this is should be self explanatory. Quotes are automatically indented when they are used.

## Headings

There are six levels of headings. They correspond with the six levels of HTML headings. You've probably noticed them already in the page. Each level down uses one more hash character.

### Headings *can* also contain **formatting**

### They can even contain `inline code`

Of course, demonstrating what headings look like messes up the structure of the page.

I don't recommend using more than three or four levels of headings here, because, when you're smallest heading isn't too small, and you're largest heading isn't too big, and you want each size up to look noticeably larger and more important, there there are only so many sizes that you can use.

## URLs

URLs can be made in a handful of ways:

* A named link to [MarkItDown][3]. The easiest way to do these is to select what you want to make a link and hit `Ctrl+L`.
* Another named link to [MarkItDown](http://www.markitdown.net/)
* Sometimes you just want a URL like <http://www.markitdown.net/>.

## Horizontal rule

A horizontal rule is a line that goes across the middle of the page.

---

It's sometimes handy for breaking things up.

## Images

Markdown can also contain images.

![images/icon.png](images/icon.png)

And raw HTML can also be included (this image is right aligned with `style="margin-right:0;"`).

<img style="display: block; margin-right: 0;" src="images/icon.png" width="50%">

## Footnote

This section is here to test the [simple-footnotes](https://github.com/pelican-plugins/simple-footnotes/) plugins.

For example, this example this text[ref]with a footnote with [a link](http://example.com)[/ref] failed with the following (cryptic) message:

```
$ make html
...
CRITICAL: TypeError: sequence item 3: expected str instance, NoneType found
...
```

See this error[ref]opened [on May 1st 2018](https://github.com/getpelican/pelican-plugins/issues/1022#issue-319066007), two years ago.[/ref]: [issue 1022](https://github.com/getpelican/pelican-plugins/issues/1022).

## Finally

There's actually a lot more to Markdown than this. See the official [introduction][4] and [syntax][5] for more information. However, be aware that this is not using the official implementation, and this might work subtly differently in some of the little things.


  [1]: http://daringfireball.net/projects/markdown/
  [2]: http://www.fileformat.info/info/unicode/char/2163/index.htm
  [3]: http://www.markitdown.net/
  [4]: http://daringfireball.net/projects/markdown/basics
  [5]: http://daringfireball.net/projects/markdown/syntax

----
