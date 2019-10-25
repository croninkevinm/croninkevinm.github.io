"""StaticJinja build script for kmcronin.com"""
import argparse
from staticjinja import Site


# def base(_template):
# _template.name = index.html
# _template.filename = C:\..\..\index.html
# return {
#     'title': 'title'
# }


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-B", "--build", action="store_true")
    args = parser.parse_args()

    if args.build:
        output_dir = '.'
        use_reloader = False
    else:
        output_dir = 'debug'
        use_reloader = True

    site = Site.make_site(  # pylint: disable=invalid-name
        staticpaths=["static/"],
        outpath=output_dir,
        # contexts=[('.*.html', base), ('index.html', index)],
        # contexts=[('.*.html', base)],
        mergecontexts=True,
    )
    # enable automatic reloading
    site.render(use_reloader=use_reloader)
