Name:		texlive-latex2e-help-texinfo-fr
Version:	64228
Release:	1
Summary:	A French translation of "latex2e-help-texinfo"
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/latex2e-help-texinfo-fr
License:	pd
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/latex2e-help-texinfo-fr.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/latex2e-help-texinfo-fr.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides a complete French translation of
latex2e-help-texinfo.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/doc/latex/latex2e-help-texinfo-fr
%{_texmfdistdir}/doc
%doc %{_texmfdistdir}/doc/info
%doc %{_texmfdistdir}/doc/info/latex2e-fr.info

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
