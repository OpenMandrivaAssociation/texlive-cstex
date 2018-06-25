Name:		texlive-cstex
Version:	20180306
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
%doc %{_texmfdistdir}/doc/cstex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc %{buildroot}%{_texmfdistdir}
