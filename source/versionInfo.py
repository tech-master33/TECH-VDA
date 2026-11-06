# A part of NonVisual Desktop Access (NVDA)
# Copyright (C) 2006-2024 NV Access Limited
# This file is covered by the GNU General Public License.
# See the file COPYING for more details.

"""
This module contains localizable version information such as description, copyright and About messages etc.
As there are localizable strings at module level, this can only be imported once localization is set up via languageHandler.initialize.
To access version information for programmatic version checks before languageHandler.initialize, use the buildVersion module which contains all the non-localizable version information such as major and minor version, and version string etc.
"""

from buildVersion import *  # noqa: F403

longName = _("TECH-VDA Screen Reader")
description = _(
	"A free and open source screen reader for Microsoft Windows. "
	"TECH-VDA is an independent fork of NVDA (NonVisual Desktop Access).",
)
url = "https://github.com/tech-master33/TECH-VDA"
copyrightYears = "2006-2024"
copyright = _("Copyright (C) {years} NVDA Contributors").format(
	years=copyrightYears,
)
aboutMessage = _(
	# Translators: "About TECH-VDA" dialog box message
	"""{longName} ({name})
Version: {version} ({version_detailed})
URL: {url}
{copyright}

TECH-VDA is an independent fork of NVDA (NonVisual Desktop Access), a free and open source screen reader for Microsoft Windows.
NVDA is developed by NV Access, a non-profit organisation committed to helping and promoting free and open source solutions for blind and vision impaired people.
TECH-VDA is not affiliated with, or endorsed by, NV Access.

{name} is covered by the GNU General Public License (Version 2). You are free to share or change this software in any way you like as long as it is accompanied by the license and you make all source code available to anyone who wants it. This applies to both original and modified copies of this software, plus any derivative works.
For further details, you can view the license from the Help menu.
It can also be viewed online at: https://www.gnu.org/licenses/old-licenses/gpl-2.0.html

Upstream NVDA project: https://www.nvaccess.org""",  # noqa: E501 line too long
).format(**globals())
