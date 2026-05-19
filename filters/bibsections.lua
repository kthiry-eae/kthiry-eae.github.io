function Div(el)
  if not el.classes:includes("bibsection") then
    return nil
  end

  local bibfile = el.attributes["file"]
  local cslfile = el.attributes["csl"] or ""

  if not bibfile or bibfile == "" then
    return {
      pandoc.Para({ pandoc.Str("Error: missing file attribute") })
    }
  end

  local yaml = "---\n"
  yaml = yaml .. "bibliography:\n"
  yaml = yaml .. "  - " .. bibfile .. "\n"

  if cslfile ~= "" then
    yaml = yaml .. "csl: " .. cslfile .. "\n"
  end

  yaml = yaml .. "nocite: |\n"
  yaml = yaml .. "  @*\n"
  yaml = yaml .. "---\n\n"
  yaml = yaml .. "::: {#refs}\n:::\n"

  local doc = pandoc.read(yaml, "markdown")
  local processed = pandoc.utils.citeproc(doc)

  return processed.blocks
end