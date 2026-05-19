from pathlib import Path
import yaml
import bibtexparser

src = Path("references/dblp.bib")
out_dir = Path("data")
out_dir.mkdir(exist_ok=True)

with src.open(encoding="utf-8") as f:
    bib = bibtexparser.load(f)

journals = []
conferences = []

for entry in bib.entries:
    entry_type = entry.get("ENTRYTYPE", "").lower()

    item = {
        "title": entry.get("title", "").replace("{", "").replace("}", ""),
        "authors": entry.get("author", "").replace(" and ", ", "),
        "date": f"{entry.get('year', '1900')}-01-01",
        "venue": entry.get("journal") or entry.get("booktitle", ""),
        "url": entry.get("url", ""),
        "doi": entry.get("doi", "")
    }

    if entry_type == "article":
        journals.append(item)
    elif entry_type in {"inproceedings", "proceedings", "incollection"}:
        conferences.append(item)

with (out_dir / "journals.yml").open("w", encoding="utf-8") as f:
    yaml.safe_dump(journals, f, allow_unicode=True, sort_keys=False)

with (out_dir / "conferences.yml").open("w", encoding="utf-8") as f:
    yaml.safe_dump(conferences, f, allow_unicode=True, sort_keys=False)