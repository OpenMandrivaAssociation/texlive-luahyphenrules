Name:		texlive-luahyphenrules
Version:	56200
Release:	2
Summary:	Loading patterns in LuaLaTeX with language.dat
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/luahyphenrules
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/luahyphenrules.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/luahyphenrules.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Preloading hyphenation patterns (or 'hyphen rules.) into any
format based upon LuaTeX is not required in LuaTeX and recent
releases of babel don't do it anyway. This package is addressed
to those who just want to select the languages and load their
patterns by means of `language.dat` without loading `babel`.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/lualatex/luahyphenrules
%doc %{_texmfdistdir}/doc/lualatex/luahyphenrules

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
