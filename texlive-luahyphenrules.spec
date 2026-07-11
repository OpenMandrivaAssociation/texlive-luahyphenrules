%global tl_name luahyphenrules
%global tl_revision 78101

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.1
Release:	%{tl_revision}.1
Summary:	Loading patterns in LuaLaTeX with language.dat
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/luatex/latex/luahyphenrules
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/luahyphenrules.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/luahyphenrules.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Preloading hyphenation patterns (or 'hyphen rules.) into any format
based upon LuaTeX is not required in LuaTeX and recent releases of babel
don't do it anyway. This package is addressed to those who just want to
select the languages and load their patterns by means of `language.dat`
without loading `babel`.

