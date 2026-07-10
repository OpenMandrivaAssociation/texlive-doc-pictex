%global tl_name doc-pictex
%global tl_revision 79618

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	A summary list of PicTeX documentation
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/info/pictex/Doc-PiCTeX.txt
License:	other-free
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/doc-pictex.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/doc-pictex.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
A summary of available resources providing (or merely discussing)
documentation of PicTeX.

