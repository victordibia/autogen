"""Sphinx configuration file for AutoGen using Sphinx Awesome Theme."""

from __future__ import annotations

from dataclasses import asdict
import sys
from typing import Any, Dict
from pathlib import Path

from sphinx.application import Sphinx
from sphinxawesome_theme import ThemeOptions, __version__
from sphinxawesome_theme.postprocess import Icons
from sphinx.util.docfields import Field

# -- Project information -----------------------------------------------------
project = "autogen_core"
author = "Microsoft"
copyright = f"2024, {author}"
version = "0.2"

sys.path.append(str(Path(".").resolve()))
# -- General configuration ---------------------------------------------------
extensions = [
    "sphinx.ext.napoleon",
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.todo",
    "sphinx.ext.viewcode",
    "sphinx.ext.intersphinx",
    "sphinx.ext.graphviz",
    "sphinx_design",
    # "sphinx_copybutton",
    "_extension.gallery_directive",
    "myst_nb",
]

suppress_warnings = ["myst.header"]
napoleon_custom_sections = [("Returns", "params_style")]
templates_path = ["_templates"]
autoclass_content = "init"

# TODO: include all notebooks excluding those requiring remote API access.
nb_execution_mode = "off"
nb_execution_raise_on_error = True
nb_execution_timeout = 60

myst_heading_anchors = 5
myst_enable_extensions = [
    "colon_fence",
    "linkify",
    "strikethrough",
]


# -- Options for HTML output -------------------------------------------------
html_title = "AutoGen"
html_theme = "sphinxawesome_theme"
html_static_path = ["_static", "images"]
html_css_files = [
    "custom.css", "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.1.1/css/all.min.css"]
html_js_files = [""]


html_logo = "_static/images/logo/logo.svg"
html_favicon = "_static/images/logo/favicon-512x512.png"

html_baseurl = "/autogen/dev/"
announcement = '<span class="fa-solid fa-triangle-exclamation"></span> AutoGen v0.4 is a work in progress. Go <a href="https://microsoft.github.io/autogen/0.2/">here</a> to continue using v0.2 documentation.'
html_context = {
    'display_github': True,
    "github_user": "microsoft",
    "github_repo": "autogen",
    "github_version": "main",
    "doc_path": "python/packages/autogen-core/docs/src/",
    "conf_py_path": "python/packages/autogen-core/docs/src/",
    'theme_announcement': announcement,
}

pygments_style = "xcode"
# pygments_style_dark = "github-dark"

html_permalinks_icon = Icons.permalinks_icon

# Select theme for both light and dark mode
# pygments_style = "color"
# Select a different theme for dark mode
# pygments_style_dark = "PYGMENTS_THEME"

theme_options = ThemeOptions(
    show_prev_next=False,
    awesome_external_links=True,
    main_nav_links={
        # "AgentChat": "/agentchat-user-guide/index",
        # "Core": "/core-user-guide/index",
        "Docs": "/index",
        # "Packages": "/packages/index",
        # "API Reference": "/reference/index",
    },
    extra_header_link_icons={
        "Twitter": {
            "link": "https://twitter.com/pyautogen",
            "icon": (
                '<svg height="22px" style="margin-top:-2px;display:inline" '
                'viewBox="0 0 512 512" fill="currentColor" xmlns="http://www.w3.org/2000/svg">'
                '<path d="M459.37 151.716c.325 4.548.325 9.097.325 13.645 0 138.72-105.583 298.558-298.558 298.558-59.452 0-114.68-17.219-161.137-47.106 8.447.974 16.568 1.299 25.34 1.299 49.055 0 94.213-16.568 130.274-44.832-46.132-.975-84.792-31.188-98.112-72.772 6.498.974 12.995 1.624 19.818 1.624 9.421 0 18.843-1.3 27.614-3.573-48.081-9.747-84.143-51.98-84.143-102.985v-1.299c13.969 7.797 30.214 12.67 47.431 13.319-28.264-18.843-46.781-51.005-46.781-87.391 0-19.492 5.197-37.36 14.294-52.954 51.655 63.675 129.3 105.258 216.365 109.807-1.624-7.797-2.599-15.918-2.599-24.04 0-57.828 46.782-104.934 104.934-104.934 30.213 0 57.502 12.67 76.67 33.137 23.715-4.548 46.456-13.32 66.599-25.34-7.798 24.366-24.366 44.833-46.132 57.827 21.117-2.273 41.584-8.122 60.426-16.243-14.292 20.791-32.161 39.308-52.628 54.253z"/>'
                '</svg>'
            ),
        },
        "GitHub": {
            "link": "https://github.com/microsoft/agnext",
            "icon": (
                '<svg height="22px" style="margin-top:-2px;display:inline" '
                'viewBox="0 0 45 44" fill="currentColor" xmlns="http://www.w3.org/2000/svg">'
                '<path fill-rule="evenodd" clip-rule="evenodd" '
                'd="M22.477.927C10.485.927.76 10.65.76 22.647c0 9.596 6.223 17.736 '
                '14.853 20.608 1.087.2 1.483-.47 1.483-1.047 0-.516-.019-1.881-.03-3.693-6.04 '
                '1.312-7.315-2.912-7.315-2.912-.988-2.51-2.412-3.178-2.412-3.178-1.972-1.346.149-1.32.149-1.32 '
                '2.18.154 3.327 2.24 3.327 2.24 1.937 3.318 5.084 2.36 6.321 1.803.197-1.403.759-2.36 '
                '1.379-2.903-4.823-.548-9.894-2.412-9.894-10.734 0-2.37.847-4.31 2.236-5.828-.224-.55-.969-2.759.214-5.748 0 0 '
                '1.822-.584 5.972 2.226 1.732-.482 3.59-.722 5.437-.732 1.845.01 3.703.25 5.437.732 '
                '4.147-2.81 5.967-2.226 5.967-2.226 1.185 2.99.44 5.198.217 5.748 1.392 1.517 2.232 3.457 '
                '2.232 5.828 0 8.344-5.078 10.18-9.916 10.717.779.67 1.474 1.996 1.474 4.021 0 '
                '2.904-.027 5.247-.027 5.96 0 .58.392 1.256 1.493 1.044C37.981 40.375 44.2 32.24 44.2 '
                '22.647c0-11.996-9.726-21.72-21.722-21.72" fill="currentColor"/>'
                '</svg>'
            ),
        },
        "Packages": {
            "link": "/packages",
            "icon": (
                '<svg width="22" height="20" viewBox="0 0 118 105" fill="none" xmlns="http://www.w3.org/2000/svg">'
                '<path d="M17.6645 40.4581L34.2565 46.4975L51.0948 40.3685L34.5029 34.329L17.6645 40.4581ZM34.329 26.8229L50.922 32.8623L67.7593 26.7333L51.1674 20.6938L34.329 26.8229Z" fill="#F7F7F4" stroke="#CCCCCC" stroke-width="0.378666" stroke-linejoin="bevel"/>'
                '<path d="M34.329 26.8229L50.922 32.8624V52.3631L34.329 46.3247V26.8229Z" fill="#EFEEEA" stroke="#CCCCCC" stroke-width="0.378666" stroke-linejoin="bevel"/>'
                '<path d="M1 66.2116L17.592 72.2521L34.4303 66.1231L17.8373 60.0836L1 66.2116Z" fill="#F7F7F4" stroke="#CCCCCC" stroke-width="0.378666" stroke-linejoin="bevel"/>'
                '<path d="M1 66.2117L17.592 72.2522V91.753L1 85.7146V66.2117Z" fill="#EFEEEA" stroke="#CCCCCC" stroke-width="0.378666" stroke-linejoin="bevel"/>'
                '<path d="M1 38.4783L17.592 44.5189L34.4303 38.3898L17.8373 32.3503L1 38.4783Z" fill="#F7F7F4" stroke="#CCCCCC" stroke-width="0.378666" stroke-linejoin="bevel"/>'
                '<path d="M17.5919 44.5189V64.0196L34.4303 57.8916V38.3898L17.5919 44.5189Z" fill="white" stroke="#CCCCCC" stroke-width="0.378666" stroke-linejoin="bevel"/>'
                '<path d="M1 38.4783L17.592 44.5189V64.0196L1 57.9812V38.4783Z" fill="#EFEEEA" stroke="#CCCCCC" stroke-width="0.378666" stroke-linejoin="bevel"/>'
                '<path d="M17.6634 72.2725L34.2564 78.3119V97.8137L17.6645 91.7743L17.6634 72.2725Z" fill="#EFEEEA" stroke="#CCCCCC" stroke-width="0.378666" stroke-linejoin="bevel"/>'
                '<path d="M17.6634 52.5775L34.2564 58.617L51.0948 52.4879L34.5028 46.4495L17.6634 52.5775Z" fill="#F7F7F4" stroke="#CCCCCC" stroke-width="0.378666" stroke-linejoin="bevel"/>'
                '<path d="M17.6634 52.5775L34.2564 58.617V78.1188L17.6645 72.0794L17.6634 52.5775Z" fill="#EFEEEA" stroke="#CCCCCC" stroke-width="0.378666" stroke-linejoin="bevel"/>'
                '<path d="M100.917 66.1913V85.6932L117.754 79.5652V60.0634L100.917 66.1913Z" fill="white" stroke="#CCCCCC" stroke-width="0.378666" stroke-linejoin="bevel"/>'
                '<path d="M84.251 72.2521V91.7529L101.089 85.6249V66.123L84.251 72.2521Z" fill="#FFD242" stroke="#CCCCCC" stroke-width="0.378666" stroke-linejoin="bevel"/>'
                '<path d="M98.0377 77.0062C98.0378 77.4582 97.9542 77.9362 97.7917 78.413C97.6292 78.8897 97.391 79.3559 97.0907 79.7848C96.7904 80.2137 96.4338 80.5969 96.0414 80.9127C95.6489 81.2284 95.2283 81.4704 94.8036 81.6249C93.9463 81.9367 93.1241 81.8734 92.5178 81.4489C91.9116 81.0245 91.5708 80.2736 91.5705 79.3614C91.5703 78.9095 91.6539 78.4316 91.8163 77.9549C91.9787 77.4782 92.2168 77.0121 92.517 76.5832C92.8172 76.1543 93.1737 75.771 93.566 75.4552C93.9583 75.1394 94.3789 74.8973 94.8036 74.7428C95.2283 74.5882 95.6488 74.5241 96.0412 74.5542C96.4336 74.5844 96.7901 74.7081 97.0904 74.9184C97.3908 75.1287 97.629 75.4214 97.7915 75.7798C97.9541 76.1382 98.0377 76.5543 98.0377 77.0062Z" fill="white"/>'
                '<path d="M67.5865 78.3119V97.8137L84.4249 91.6847V72.1829L67.5865 78.3119Z" fill="#FFD242" stroke="#CCCCCC" stroke-width="0.378666" stroke-linejoin="bevel"/>'
                '<path d="M50.922 84.3717V103.873L67.7593 97.7444V78.2437L50.922 84.3717Z" fill="white" stroke="#CCCCCC" stroke-width="0.378666" stroke-linejoin="bevel"/>'
                '<path d="M34.329 78.3322L50.922 84.3716V103.873L34.329 97.834V78.3322Z" fill="#EFEEEA" stroke="#CCCCCC" stroke-width="0.378666" stroke-linejoin="bevel"/>'
                '<path d="M100.917 46.4975V65.9983L117.754 59.8703V40.3685L100.917 46.4975Z" fill="#FFD242" stroke="#CCCCCC" stroke-width="0.378666" stroke-linejoin="bevel"/>'
                '<path d="M84.3235 20.7632L100.917 26.8026L117.754 20.6736L101.162 14.6341L84.3235 20.7632Z" fill="#FFC91D" stroke="#CCCCCC" stroke-width="0.378666" stroke-linejoin="bevel"/>'
                '<path d="M100.917 26.8026V46.3034L117.754 40.1754V20.6736L100.917 26.8026ZM84.251 52.5572V72.058L101.089 65.93V46.4282L84.251 52.5572Z" fill="#FFD242" stroke="#CCCCCC" stroke-width="0.378666" stroke-linejoin="bevel"/>'
                '<path d="M84.251 32.8624V52.3631L101.089 46.2351V26.7333L84.251 32.8624Z" fill="#3775A9" stroke="#CCCCCC" stroke-width="0.378666" stroke-linejoin="bevel"/>'
                '<path d="M67.6591 7.12799L84.251 13.1674L101.089 7.03839L84.4974 1L67.6591 7.12799Z" fill="#2F6491" stroke="#CCCCCC" stroke-width="0.378666" stroke-linejoin="bevel"/>'
                '<path d="M84.251 13.1664V32.6682L101.089 26.5402V7.03839L84.251 13.1664Z" fill="#3775A9" stroke="#CCCCCC" stroke-width="0.378666" stroke-linejoin="bevel"/>'
                '<path d="M67.5865 58.617V78.1188L84.4249 71.9898V52.4879L67.5865 58.617Z" fill="#FFD242" stroke="#CCCCCC" stroke-width="0.378666" stroke-linejoin="bevel"/>'
                '<path d="M67.5865 38.9221V58.4239L84.4249 52.2948V32.793L67.5865 38.9221ZM50.922 64.6767V84.1785L67.7593 78.0495V58.5487L50.922 64.6767Z" fill="#3775A9" stroke="#CCCCCC" stroke-width="0.378666" stroke-linejoin="bevel"/>'
                '<path d="M34.329 58.6383L50.922 64.6767V84.1786L34.329 78.1391V58.6383ZM34.329 38.9424L50.922 44.9818L67.7593 38.8538L51.1674 32.8144L34.329 38.9424Z" fill="#2F6491" stroke="#CCCCCC" stroke-width="0.378666" stroke-linejoin="bevel"/>'
                '<path d="M50.922 44.9818V64.4836L67.7593 58.3546V38.8538L50.922 44.9818Z" fill="#3775A9" stroke="#CCCCCC" stroke-width="0.378666" stroke-linejoin="bevel"/>'
                '<path d="M34.329 38.9423L50.922 44.9818V64.4836L34.329 58.4442V38.9423ZM50.9946 13.1877L67.5865 19.2272L84.4249 13.0981L67.8319 7.05972L50.9946 13.1877Z" fill="#2F6491" stroke="#CCCCCC" stroke-width="0.378666" stroke-linejoin="bevel"/>'
                '<path d="M67.5865 19.2272V38.729L84.4249 32.5999V13.0981L67.5865 19.2272Z" fill="#3775A9" stroke="#CCCCCC" stroke-width="0.378666" stroke-linejoin="bevel"/>'
                '<path d="M50.9946 13.1877L67.5865 19.2272V38.729L50.9946 32.6895V13.1877Z" fill="#2F6491" stroke="#CCCCCC" stroke-width="0.378666" stroke-linejoin="bevel"/>'
                '<path d="M77.1065 25.4906C77.1066 25.9426 77.023 26.4206 76.8605 26.8974C76.6981 27.3741 76.4598 27.8403 76.1595 28.2692C75.8592 28.6981 75.5026 29.0813 75.1102 29.3971C74.7177 29.7128 74.2971 29.9548 73.8724 30.1093C73.4477 30.2639 73.0271 30.3279 72.6347 30.2978C72.2424 30.2677 71.8858 30.1439 71.5855 29.9336C71.2852 29.7233 71.0469 29.4306 70.8844 29.0722C70.7219 28.7138 70.6382 28.2967 70.6382 27.8448C70.6381 27.3928 70.7217 26.9148 70.8842 26.438C71.0467 25.9613 71.2849 25.4951 71.5853 25.0662C71.8856 24.6373 72.2422 24.254 72.6346 23.9383C73.027 23.6226 73.4476 23.3806 73.8724 23.2261C74.2971 23.0715 74.7176 23.0074 75.11 23.0376C75.5024 23.0677 75.8589 23.1915 76.1593 23.4018C76.4596 23.612 76.6978 23.9047 76.8603 24.2632C77.0229 24.6216 77.1065 25.0387 77.1065 25.4906Z" fill="white"/>'
                '</svg>'
            ),
        },
    },

)


html_theme_options = asdict(theme_options)

autodoc_default_options = {
    "members": True,
    "undoc-members": True,
}

intersphinx_mapping = {"python": ("https://docs.python.org/3", None)}


# def setup_to_main(
#     app: Sphinx, pagename: str, templatename: str, context, doctree
# ) -> None:
#     """Add a function that jinja can access for returning an "edit this page" link pointing to `main`."""

#     def to_main(link: str) -> str:
#         """Transform "edit on github" links and make sure they always point to the main branch.

#         Args:
#             link: the link to the github edit interface

#         Returns:
#             the link to the tip of the main branch for the same file
#         """
#         links = link.split("/")
#         idx = links.index("edit")
#         return "/".join(links[: idx + 1]) + "/main/" + "/".join(links[idx + 2:])

#     context["to_main"] = to_main


def setup(app: Sphinx) -> None:
    """Register the ``confval`` role and directive.

    This allows to declare theme options as their own object
    for styling and cross-referencing.
    """
    app.add_object_type(
        "confval",
        "confval",
        objname="configuration parameter",
        doc_field_types=[
            Field(
                "default",
                label="default",
                has_arg=True,
                names=("default",),
                bodyrolename="class",
            )
        ],
    )
