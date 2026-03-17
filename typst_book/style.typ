  
#let leftCaption(it) = {
  set text(size: 8pt)
  set align(left)
  set par(justify: true)

  // Within the context of the element, you may use the counter
  context(it, {
    text(weight: "bold")[#it.supplement #it.counter.display(it.numbering).]
  })

  h(4pt)
  set text(fill: black.lighten(20%), style: "italic")
  it.body
}


#let template(
  // FRONTPAGE.
  title: "Book Title",
  subtitle: none,
  authors: "Your name",
  cover: none,            // <— path to cover "images/cover.png"
  cover_width: 12cm,    
  coverposition: 1cm,
  justification: false,

  // TOC
  ToC_depth: 2,
  show_ToC: true,

  // PREFACE
  preface: none,

  // SPECIFICATION of output
  paper-size: "a4",       // https://typst.app/docs/reference/layout/page/#parameters-paper
  margin: (),                          
  linespacing: .5em,
  show_pagenumber: false,
  margin_top: 2cm,
  margin_bottom: 2cm,
  margin_left: 20%,
  margin_right: 10%,
  logo: none,
  logo_width: 10%,
  
  font: "Libertinus Serif", 
  fontsize: 11pt,

  theme: red.darken(30%),
  colorheadings: black,
  
  // The book's content.
  body
) = {

  set page(
    numbering: none,
    paper-size,
    ) //numbering off until first chapter
  
  set heading(numbering: (..args) => {
    let nums = args.pos()
    let level = nums.len()
    if level == 1 {[#numbering("1.", ..nums)]} else {[#numbering("1.1.1", ..nums)]}
    },   
    
)

  // Figure numbering: chapter.N where N is the kind-specific count within
  // that chapter (images, exercises, tables each get their own sequence).
  set figure(numbering: (..args) => {
    let chapter = counter(heading).display((..nums) => nums.pos().at(0))
    [#chapter.#numbering("1", ..args.pos())]
  })
  

  // Configure equation numbering and spacing.
  set math.equation(numbering: (..args) => {
    let chapter = counter(heading).display((..nums) => nums.pos().at(0))
    [(#chapter.#numbering("1)", ..args.pos())]
  })
  show math.equation: set block(spacing: 1em)


  // Configure lists.
  set enum(indent: 10pt, body-indent: 9pt)
  set list(indent: 10pt, body-indent: 9pt)

  // link behaviour
  show link: set text( fill: blue.darken(30%))

// COVERPAGE
  // Title, subtitle, 
  align(center, text(17pt, weight: "bold", fill: theme, title))
  if subtitle != none {
    parbreak()
    box(text(14pt, fill: gray.darken(30%), subtitle))
  }

    if cover != none {
      v(coverposition)
      align(center, image((cover), width: cover_width))
    }

  //author
  v(1em)

  // authors in gray
  if authors != none {
  place(bottom + right,
    text(12pt, fill: gray.darken(50%), authors)
  )

  }


// PREFACE,
  if preface != none {
    pagebreak()
    place(top + left,
      text(14pt, fill: theme, "Preface")
    )
    v(1em)
    set par(justify: true)
    align(center, box(width: 70%, text(11pt, overhang: true, font:  "New Computer Modern", fill: gray.darken(30%), preface)))
  }


//OUTLINE OF THE BOOK
  pagebreak()
  if show_ToC == true {
      
    show outline.entry.where(level: 1): it => {
      v(12pt, weak: true)
      strong(it)
    }
    // setting outline in themecolor
    outline(
    title: strong(text(fill: theme, "Contents")),
    depth: ToC_depth,
    indent: auto,
  )

  }

  show heading.where(level: 1): it => {
    pagebreak()
    counter(figure).update(0)
    counter(figure.where(kind: "figure")).update(0)
    counter(figure.where(kind: "table")).update(0)
    counter(figure.where(kind: "exercise")).update(0)
    counter(figure.where(kind: "solution")).update(0)
    counter(figure.where(kind: "proof")).update(0)
    counter(math.equation).update(0)
    it
  }

  //Heading colors
  show heading: set text(colorheadings)
  

// PAGE LAYOUT OF CONTENT
  set page(
    numbering: if show_pagenumber == true {"1"} else {none},         //turn on numbering
    margin: (
      top: margin_top,
      bottom: margin_bottom,
      left: margin_left,
      right: margin_right 
      ),    //set left margin
    header: if logo != none { align(center)[#image(logo, width: logo_width)] } else { none },//include logo
  )   

  set text(
    font: font,
    size: fontsize
    )
  set par(
    leading: linespacing,
    justify: justification
    )

  counter(page).update(1)   //set number to 1

  // Input code cells (Python): themed left border, light background.
  show raw.where(block: true): it => {
    if it.lang == "python" {
      block(
        fill: luma(250),
        stroke: (left: 3pt + theme.lighten(40%)),
        inset: (x: 8pt, y: 6pt),
        radius: (right: 3pt),
        width: 100%,
        it,
      )
    } else if it.lang == none {
      // Code-cell output: dashed border, slightly darker background.
      block(
        fill: luma(242),
        stroke: (paint: luma(190), thickness: 0.8pt, dash: "dashed"),
        inset: (x: 8pt, y: 6pt),
        radius: 3pt,
        width: 100%,
        it,
      )
    } else {
      it
    }
  }

  // Render exercises and solutions as level-3 headings (no floating boxes).
  show figure.where(kind: "exercise"): it => block(width: 100%, breakable: true, [
    #heading(level: 3, numbering: none, bookmarked: false)[#it.caption]
    #it.body
  ])
  show figure.where(kind: "solution"): it => block(width: 100%, breakable: true, [
    #heading(level: 3, numbering: none, bookmarked: false)[#it.caption]
    #it.body
  ])

  // Remove floating wrappers so exercises/solutions appear inline.
  // Only target float:true places (from proof()) — leaves absolute-positioned
  // elements (cover author, etc.) and table floats untouched.
  show place.where(float: true): it => it.body

  // Display the book's contents.
  [#body]
}
