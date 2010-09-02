%define upstream_name	 Image-Size
%define upstream_version 3.230

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1
Epoch:		1

Summary:	Read the dimensions of an image in several popular formats
License:	GPL
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Image/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl(Compress::Zlib)

BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

%description
Image::Size is a library based on the image-sizing code in the wwwimagesize
script, a tool that analyzes HTML files and adds HEIGHT and WIDTH tags to
IMG directives.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%clean 
rm -rf %{buildroot}

%install
rm -rf %{buildroot}
%makeinstall_std

%files
%defattr(-,root,root)
%{_bindir}/imgsize
%{_mandir}/*/*
%{perl_vendorlib}/Image
%{perl_vendorlib}/auto/Image
