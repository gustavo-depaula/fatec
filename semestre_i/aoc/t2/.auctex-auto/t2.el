(TeX-add-style-hook
 "t2"
 (lambda ()
   (TeX-add-to-alist 'LaTeX-provided-class-options
                     '(("article" "11pt")))
   (TeX-add-to-alist 'LaTeX-provided-package-options
                     '(("inputenc" "utf8") ("fontenc" "T1") ("ulem" "normalem") ("babel" "portuguese" "")))
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "hyperref")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "hyperimage")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "hyperbaseurl")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "nolinkurl")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "url")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "path")
   (add-to-list 'LaTeX-verbatim-macros-with-delims-local "path")
   (TeX-run-style-hooks
    "latex2e"
    "structure"
    "article"
    "art11"
    "inputenc"
    "fontenc"
    "graphicx"
    "grffile"
    "longtable"
    "wrapfig"
    "rotating"
    "ulem"
    "amsmath"
    "textcomp"
    "amssymb"
    "capt-of"
    "hyperref"
    "babel")
   (LaTeX-add-labels
    "sec:org27e9cdb"
    "sec:orgb89a338"
    "sec:org76a63db"
    "sec:org4ae3ac5"
    "sec:orge021cb4"
    "sec:org8ab3a57"
    "sec:orgf6d946b"
    "sec:orge6912fb"
    "sec:org8cc839c"
    "sec:orgf5116f2"
    "sec:org0889a44"
    "sec:org55cfa3e"
    "sec:orgf0b29bf"
    "sec:org80725f3"
    "sec:orgdd23a5c"
    "sec:org338395f"
    "sec:orgb41b5b3"
    "sec:orgae451bd"
    "sec:org16e6fc2"
    "sec:org9c9f886"
    "sec:org7c3181b"
    "sec:orgacfdffd"
    "sec:orga488b5b"
    "sec:orge55e86b"
    "sec:orgb405df6"
    "sec:orgeb9caec"
    "sec:org44421a9"
    "sec:org8238eb1"
    "sec:org6b2c3ca"
    "sec:org97f8fb5"
    "sec:orgb652a0d"
    "sec:org136ab2f"
    "sec:org583287a"
    "sec:org60ec1c2"
    "sec:org46c6a41"))
 :latex)

