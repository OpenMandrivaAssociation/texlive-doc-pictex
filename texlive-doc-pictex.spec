# revision 24927
# category Package
# catalog-ctan /info/pictex/Doc-PiCTeX.txt
# catalog-date 2008-09-09 11:27:07 +0200
# catalog-license other-free
# catalog-version undef
Name:		texlive-doc-pictex
Version:	20080909
Release:	7
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

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 20080909-3
+ Revision: 751008
- Rebuild to reduce used resources

* Mon Dec 26 2011 Paulo Andrade <pcpa@mandriva.com.br> 20080909-2
+ Revision: 745207
- texlive-doc-pictex

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20080909-1
+ Revision: 718245
- texlive-doc-pictex
- texlive-doc-pictex
- texlive-doc-pictex
- texlive-doc-pictex

