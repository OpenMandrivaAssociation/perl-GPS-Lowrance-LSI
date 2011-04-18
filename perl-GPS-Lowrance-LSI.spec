%define upstream_name    GPS-Lowrance-LSI
%define upstream_version 0.23

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 2

Summary:    Lowrance Serial Interface Protocol module in Perl
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/GPS/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Carp::Assert)
BuildRequires: perl(Parse::Binary::FixedFormat)
BuildArch: noarch
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}

%description
This module provides _very_ low-level support for the LSI (Lowrance Serial
Interface) 100 protocol used to communicate with Lowrance and Eagle GPS
devices.

(Higher-level functions and wrappers for specific commands will be provided
in other modules. This module is intentionally kept simple.)

Functions
    * lsi_query

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes README
%{_mandir}/man3/*
%perl_vendorlib/*


