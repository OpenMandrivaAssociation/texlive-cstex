%global tl_name cstex
%global tl_revision 64149

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Support for Czech/Slovak languages
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/cstex
License:	other-free
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/cstex.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/cstex.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package mirrors the macros part of the home site's distribution of
CSTeX. The licence (modified GPL) applies to some of the additions that
make it a Czech/Slovak language distribution, rather than the
distribution of a basic Plain/LaTeX distribution.

