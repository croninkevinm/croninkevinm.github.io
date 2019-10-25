"""StaticJinja build script for kmcronin.com"""
from staticjinja import Site


# def base(_template):
# _template.name = index.html
# _template.filename = C:\..\..\index.html
# return {
#     'title': 'title'
# }


if __name__ == "__main__":
    site = Site.make_site(  # pylint: disable=invalid-name
        # contexts=[('.*.html', base), ('index.html', index)],
        # contexts=[('.*.html', base)],
        mergecontexts=True,
    )
    # enable automatic reloading
    site.render(use_reloader=True)
