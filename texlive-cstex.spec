# revision 32249
# category Package
# catalog-ctan /macros/cstex
# catalog-date 2013-11-21 20:02:41 +0100
# catalog-license other-free
# catalog-version undef
Name:		texlive-cstex
Version:	20131121
Release:	1
Summary:	Support for Czech/Slovak languages
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/cstex
License:	OTHER-FREE
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cstex.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cstex.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg

%description
This package mirrors the macros part of the home site's
distribution of CSTeX. The licence (modified GPL) applies to
some of the additions that make it a Czech/Slovak language
distribution, rather than the distribution of a basic
Plain/LaTeX distribution.

#-----------------------------------------------------------------------
%files
%doc %{_texmfdistdir}/doc/cstex/00-README-cslatex
%doc %{_texmfdistdir}/doc/cstex/INSTALL.cslatex
%doc %{_texmfdistdir}/doc/cstex/README-csplain
%doc %{_texmfdistdir}/doc/cstex/README-cspsfont
%doc %{_texmfdistdir}/doc/cstex/README-doc
%doc %{_texmfdistdir}/doc/cstex/README-opmac
%doc %{_texmfdistdir}/doc/cstex/README.cslatex
%doc %{_texmfdistdir}/doc/cstex/cspsfonts-gen/README
%doc %{_texmfdistdir}/doc/cstex/cspsfonts-gen/fontgen
%doc %{_texmfdistdir}/doc/cstex/cspsfonts-gen/kernoff.c
%doc %{_texmfdistdir}/doc/cstex/cspsfonts-gen/mkf
%doc %{_texmfdistdir}/doc/cstex/cspsfonts-gen/mkfc
%doc %{_texmfdistdir}/doc/cstex/cspsfonts-gen/xl2.enc
%doc %{_texmfdistdir}/doc/cstex/cspsfonts-gen/xt2.enc
%doc %{_texmfdistdir}/doc/cstex/cstexman.pdf
%doc %{_texmfdistdir}/doc/cstex/cstexman.tex
%doc %{_texmfdistdir}/doc/cstex/jemny.errata
%doc %{_texmfdistdir}/doc/cstex/jemny.pdf
%doc %{_texmfdistdir}/doc/cstex/jemny.tar.gz
%doc %{_texmfdistdir}/doc/cstex/lic-gpl.eng
%doc %{_texmfdistdir}/doc/cstex/opmac-d.pdf
%doc %{_texmfdistdir}/doc/cstex/opmac-d.tex
%doc %{_texmfdistdir}/doc/cstex/opmac-u.pdf
%doc %{_texmfdistdir}/doc/cstex/opmac-u.tex
%doc %{_texmfdistdir}/doc/cstex/pdfuni-article.pdf
%doc %{_texmfdistdir}/doc/cstex/pdfuni-article.tex
%doc %{_texmfdistdir}/doc/cstex/prvni.pdf
%doc %{_texmfdistdir}/doc/cstex/prvni.tex
%doc %{_texmfdistdir}/doc/cstex/test8z.pdf
%doc %{_texmfdistdir}/doc/cstex/test8z.tex
%doc %{_texmfdistdir}/doc/cstex/testgyre8z.pdf
%doc %{_texmfdistdir}/doc/cstex/testgyre8z.tex
%doc %{_texmfdistdir}/doc/cstex/testlat.tex
%doc %{_texmfdistdir}/doc/cstex/zmeny.txt

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc %{buildroot}%{_texmfdistdir}
