# revision 24927
# category Package
# catalog-ctan /info/pictex/Doc-PiCTeX.txt
# catalog-date 2008-09-09 11:27:07 +0200
# catalog-license other-free
# catalog-version undef
Name:		texlive-doc-pictex
Version:	20080909
Release:	2
Summary:	A summary list of PicTeX documentation
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/info/pictex/Doc-PiCTeX.txt
License:	OTHER-FREE
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/doc-pictex.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/doc-pictex.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg

%description
A summary of available resources providing (or merely
discussing) documentation of PicTeX.

#-----------------------------------------------------------------------
%files
%doc %{_texmfdistdir}/doc/generic/doc-pictex/Doc-PiCTeX.txt
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
