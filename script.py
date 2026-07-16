import hashlib
import os
import re
import urllib.parse

from dicts import assets_checksum_map, filemap

import_path = "20260703-piwigo-notion-doc-en"
export_path = "docs"


def handle_md_link(link: str, origin_folder: str, new_folder):
    # Get path relative to import folder
    old_link_abspath = os.path.abspath(
        os.path.join(import_path, os.path.dirname(origin_folder), link)
    )
    old_link_relpath = os.path.relpath(old_link_abspath, os.path.abspath(import_path))

    # Get link from dict and make it relative to current folder
    new_link = filemap[old_link_relpath]
    new_link_rel = os.path.relpath(os.path.join(export_path, new_link), new_folder)

    return new_link_rel


def parse_md_line(line: str, old_path: str, new_path: str) -> str:
    link_match_iter = re.finditer(r"!?\[([^\[\]]*)\]\(((?:.*?\.\w+|http.*?))\)", line)
    for link_match in link_match_iter:
        # Only parse local links
        if not (
            link_match.group(2).startswith("http")
            or link_match.group(2) == "mailto:support@piwigo.com"
        ):
            # Decode local links
            link = urllib.parse.unquote(link_match.group(2), errors="strict")
            # Only read md links, map all other links to ressource
            if link.endswith(".md"):
                prefix = ""
                link = handle_md_link(link, old_path, new_path)
            else:
                prefix = "!"
                with open(
                    os.path.join(import_path, os.path.dirname(old_path), link), "rb"
                ) as img:
                    link = assets_checksum_map[hashlib.md5(img.read()).hexdigest()]
            line = line.replace(
                link_match.group(0), f"{prefix}[{link_match.group(1)}]({link})"
            )
    return line


def main():
    for old_file, new_file in filemap.items():
        oldf_path = os.path.join(import_path, old_file)
        nf_path = os.path.join(export_path, new_file)
        nf_dir = os.path.dirname(nf_path)
        os.makedirs(nf_dir, exist_ok=True)

        with open(oldf_path) as oldf:
            with open(nf_path, "w") as nf:
                for line in oldf:  # Rewrite all files
                    nf.write(parse_md_line(line, old_file, nf_dir))


if __name__ == "__main__":
    main()
