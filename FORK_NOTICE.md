# TECH-VDA fork notice

TECH-VDA is an independent fork of **NVDA (NonVisual Desktop Access)**, the free and open source
screen reader for Microsoft Windows.

## Attribution

* Original project: NVDA, <https://www.nvaccess.org/>
* Original source: <https://github.com/nvaccess/nvda>
* Fork source: <https://github.com/tech-master33/TECH-VDA>
* Original authors and copyright holders: NV Access and the NVDA contributors
* Fork base: NVDA 2024.4 (source tree reports 2024.4.2)

TECH-VDA is **not** affiliated with, sponsored by, or endorsed by NV Access.
The name "NVDA", the NV Access name, and related marks belong to their respective owners and are
used here only to describe the origin of this fork, as required for honest attribution.

## License

TECH-VDA is distributed under the same modified GNU General Public License version 2 as NVDA.
See [`copying.txt`](./copying.txt) for the full text.

Because this is a modified version of NVDA:

* The origin of the code is stated here and in the README and About dialog.
* The complete corresponding source code for any distributed build must be made available.
* The GPL notice and copyright notices must not be removed.

## What this fork changes

The fork changes branding and fork-specific packaging defaults, including:

* Product name: **TECH-VDA** in window titles, menus, About dialog, installer, shortcuts,
  documentation headings, and launcher metadata.
* Default install folder, Start Menu folder, desktop shortcut, uninstall registry entry,
  system configuration registry key, user configuration folder, default log file
  (`tech-vda.log`), and crash dump are namespaced as TECH-VDA so the fork can coexist
  with an installed copy of NVDA.
* Automatic update checking is **disabled** so a fork build can never download and install an
  official NVDA release over itself. A TECH-VDA update service must be configured before enabling it.
* The Windows Store/AppX package identity and display name are namespaced for TECH-VDA.

## What still comes from upstream

The vast majority of the code is unmodified NVDA. This includes the accessibility engine, speech
and braille drivers, UIA/IAccessible handling, add-on API, and translated documentation.

The following are intentionally left as upstream identifiers for compatibility and must not be
renamed without a full migration:

* Python module/package names such as `NVDAObjects`, `NVDAState`, `nvdaHelper`, and `NVDAHelperRemote.dll`.
* Executable names such as `nvda.exe`, `nvda_slave.exe`, `nvda_noUIAccess.exe`, and `nvda_UIAccess.exe`.
* Keyboard gesture tokens such as `kb:NVDA+n`. These are internal input identifiers, not branding.
* The add-on API version and add-on package format, so existing NVDA add-ons remain installable.
* Upstream changelog history and translated documentation.

## Reporting issues

* TECH-VDA-specific problems: report to the TECH-VDA project.
* Problems reproducible in unmodified NVDA: report upstream at
  <https://github.com/nvaccess/nvda/issues>.
