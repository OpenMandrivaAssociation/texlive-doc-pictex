Name:		texlive-doc-pictex
Version:	24927
Release:	2
Summary:	A summary list of PicTeX documentation
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/info/pictex/Doc-PiCTeX.txt
License:	OTHER-FREE
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/doc-pictex.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/doc-pictex.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg

%description
A summary of available resources providing (or merely
discussing) documentation of PicTeX.

#-----------------------------------------------------------------------
%files
%doc %{_texmfdistdir}/doc/generic/doc-pictex/Doc-PiCTeX.txt

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc %{buildroot}%{_texmfdistdir}
