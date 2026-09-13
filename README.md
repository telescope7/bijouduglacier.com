# bijouduglacier.com

The marketing site for **Bijou du Glacier**, a four-bedroom apartment in
car-free Saas-Fee, Valais. Live at <https://bijouduglacier.com>.

Static HTML and one stylesheet, in four languages, deployed to a Linode with
one command. No framework, no build step at serve time, no JavaScript
dependency, no tracking.

---

## Layout

```
bijou-du-glacier/
  website/          the site itself. This is what gets uploaded.
  copy/             every sentence on the site, numbered, for editing
  tools/            Python that generates website/ from copy + content files
  deploy/           Ansible: nginx, HTTPS, booking redirects, traffic report
  INSTRUCTIONS.md   start here if you are the owner, not a developer

media files combined/   the original photographs and video keyframes
Saas-Fee house.mp4      the source video the hero clip is cut from
extract_keyframes.py    pulls stills out of a video — see KEYFRAMES.md
download_airbnb_images.py
```

---

## Working on it

Nothing is required to *view* the site: open `bijou-du-glacier/website/index.html`
in a browser and every page, image and link works from disk.

To change it:

```bash
cd bijou-du-glacier/tools
python3 build_site.py     # regenerate the 17 pages from the content files
python3 audit.py          # must report 0 fail before you deploy
```

`audit.py` is the gate. It checks far more than a linter would: heading order,
alt text, image dimensions, internal links, canonicals, reciprocal hreflang,
structured data, colour contrast measured against the actual palette, CSS
specificity traps, nginx location precedence, and that the booking redirects in
the nginx template still agree with the URLs in `build_site.py`. Every check in
it exists because something broke once.

To deploy:

```bash
cd bijou-du-glacier/deploy
cp inventory.ini.example inventory.ini   # your server's address
cp vars.yml.example vars.yml             # your email, for Let's Encrypt
ansible-playbook -i inventory.ini deploy.yml
```

Both copied files are gitignored. See `deploy/README.md` for what the playbook
does and what to do when it complains.

---

## A note on the two gitignored files

This repository is public. `deploy/inventory.ini` holds the server's IP address
and `deploy/vars.yml` holds an email address; neither is committed, and the
`.example` files next to them carry placeholders instead. No password or key
appears anywhere in this repository: the traffic report's basic-auth file is
created by hand on the server with `htpasswd` and never leaves it.

---

## Requirements

- **To build:** Python 3.9+ and Pillow (`pip install Pillow`). Only needed if
  you change the copy or the images.
- **To deploy:** Ansible on your machine (`brew install ansible`), and a fresh
  Ubuntu server you can reach over SSH as root with a key.
- **To serve:** nothing. It is static files.
