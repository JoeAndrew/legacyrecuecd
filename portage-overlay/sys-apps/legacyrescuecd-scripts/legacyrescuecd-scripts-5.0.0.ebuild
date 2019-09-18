inherit eutils

DESCRIPTION="admin scripts provided with LegacyRescueCd (forked from SystemRescueCD 5.x)"
HOMEPAGE="http://www.system-rescue-cd.org"

LICENSE="GPL-2"
SLOT="0"
KEYWORDS="alpha amd64 hppa mips ppc ppc64 sparc x86"
IUSE=""

DEPEND=">=dev-lang/python-3.4.0
        >=app-shells/bash-3.1"
RDEPEND="${DEPEND}"

src_install()
{
	dosbin "${FILESDIR}"/legacyrescuecd-custom || die
	dosbin "${FILESDIR}"/legacyrescuecd-usbstick || die
	dosbin "${FILESDIR}"/legacyrescuecd-backstore || die
	dosbin "${FILESDIR}"/legacyrescuecd-pkgstats || die
	dosbin "${FILESDIR}"/legacyrescuecd-cleansys || die
	dosbin "${FILESDIR}"/autorun || die
	dosbin "${FILESDIR}"/knx-hdinstall || die
	dosbin "${FILESDIR}"/mountsys || die
	dosbin "${FILESDIR}"/sysreport || die
}
