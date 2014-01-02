%define modname	Image-Size
%define modver 3.232

Summary:	Read the dimensions of an image in several popular formats
Name:		perl-%{modname}
Epoch:		1
Version:	%perl_convert_version %{modver}
Release:	1
License:	GPLv2
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{modname}
Source0:	http://www.cpan.org/modules/by-module/Image/Image-Size-%{modver}.tar.gz
BuildArch:	noarch
BuildRequires:	perl(Compress::Zlib)
BuildRequires:	perl-devel

%description
Image::Size is a library based on the image-sizing code in the wwwimagesize
script, a tool that analyzes HTML files and adds HEIGHT and WIDTH tags to
IMG directives.

%prep
%setup -qn %{modname}-%{modver}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%{_bindir}/imgsize
# %{perl_vendorlib}/Image
# %{perl_vendorlib}/auto/Image
%{_mandir}/man1/*
%{_mandir}/man3/*


