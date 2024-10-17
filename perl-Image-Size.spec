%define modname	Image-Size

Summary:	Read the dimensions of an image in several popular formats
Name:		perl-%{modname}
Version:	3.300
Release:	2
License:	GPLv2
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{modname}
Source0:	http://www.cpan.org/modules/by-module/Image/Image-Size-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Compress::Zlib)
BuildRequires:	perl-devel

%description
Image::Size is a library based on the image-sizing code in the wwwimagesize
script, a tool that analyzes HTML files and adds HEIGHT and WIDTH tags to
IMG directives.

%prep
%autosetup -p1 -n %{modname}-%{version}
perl Makefile.PL INSTALLDIRS=vendor

%build
%make_build

%check
make test

%install
%make_install

%files
%{_bindir}/imgsize
%{perl_vendorlib}/Image
# %{perl_vendorlib}/auto/Image
%{_mandir}/man1/*
%{_mandir}/man3/*


