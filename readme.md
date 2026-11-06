# TECH-VDA

**TECH-VDA is an independent fork of [NVDA](https://www.nvaccess.org/), the free and open source screen reader for Microsoft Windows.**

> **Fork notice:** TECH-VDA is based on NVDA 2024.4 and is maintained separately from the upstream NVDA project.
> It is **not** affiliated with, sponsored by, or endorsed by NV Access.
> NVDA is developed by [NV Access](https://www.nvaccess.org/) in collaboration with a global community of contributors.
> All original NVDA code and documentation remain the work of the NVDA contributors and are used under the terms of the GNU General Public License.

## About this fork

TECH-VDA tracks NVDA 2024.4 and is intended to provide a separate, independently branded build.
Changes in this fork are limited to branding, packaging, and fork-specific defaults; the underlying accessibility engine remains NVDA.

* Upstream project: [nvaccess.org](https://www.nvaccess.org/)
* Upstream source: [github.com/nvaccess/nvda](https://github.com/nvaccess/nvda)
* Fork source: [github.com/tech-master33/TECH-VDA](https://github.com/tech-master33/TECH-VDA)
* Fork base: NVDA 2024.4 (2024.4.2 source tree)
* License: GNU General Public License version 2 (modified), see [copying.txt](./copying.txt)

For the full fork attribution and list of changed identifiers, see [FORK_NOTICE.md](./FORK_NOTICE.md).

## Building and running

TECH-VDA uses the same build system and developer workflow as NVDA:

* Build instructions: [projectDocs/dev/buildingNVDA.md](./projectDocs/dev/buildingNVDA.md)
* Developer guide: [projectDocs/dev/readme.md](./projectDocs/dev/readme.md)
* Run from source: `runnvda.bat`
* Build: `scons.bat`
* Unit tests: `rununittests.bat`

The `include/` and `miscDeps/` submodules must be checked out before building.

## Contributing

Because this is a fork, please report TECH-VDA-specific issues to the TECH-VDA project.
Issues that also affect unmodified NVDA should be reported to the [upstream NVDA issue tracker](https://github.com/nvaccess/nvda/issues).

The NVDA project has a [Citizen and Contributor Code of Conduct](CODE_OF_CONDUCT.md). By participating in this fork you agree to abide by it.

## Acknowledgements

We extend our sincere gratitude to [SignPath](https://www.signpath.io/) for their generous support in providing code signing services to open source projects, and to NV Access and the NVDA contributors for the original screen reader this fork is built on.

## License

TECH-VDA is distributed under the same modified GNU General Public License version 2 as NVDA.
See [copying.txt](./copying.txt) for the full license text.
As required by the license, the complete corresponding source code for any distributed TECH-VDA build must be made available.
